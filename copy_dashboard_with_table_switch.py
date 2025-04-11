from metabase_api import Metabase_API
from typing import Dict, Optional, Union, List
from dotenv import load_dotenv
import os
import json

load_dotenv()

def copy_dashboard_with_table_mapping(
    mb: Metabase_API,
    source_dashboard_name: Optional[str] = None,
    source_dashboard_id: Optional[int] = None,
    source_collection_name: Optional[str] = None,
    source_collection_id: Optional[int] = None,
    destination_dashboard_name: Optional[str] = None,
    destination_collection_name: Optional[str] = None,
    destination_collection_id: Optional[int] = None,
    table_name_mapping: Dict[str, str] = None,
    ignore_these_filters: Optional[List[str]] = None,
    postfix: str = '',
    verbose: bool = False
) -> int:
    """
    Copy a dashboard while switching the underlying tables for all cards based on table name mapping.

    This function combines copy_dashboard with clone_card to create a dashboard copy
    where cards are using different target tables instead of the source tables.

    Args:
        mb: Metabase API instance
        source_dashboard_name: Name of the dashboard to copy
        source_dashboard_id: ID of the dashboard to copy
        source_collection_name: Name of the collection the source dashboard is in
        source_collection_id: ID of the collection the source dashboard is in
        destination_dashboard_name: Name for the new dashboard
        destination_collection_name: Name of the destination collection
        destination_collection_id: ID of the destination collection
        table_name_mapping: Dictionary mapping source table names to target table names
        ignore_these_filters: List of filter names to not migrate
        postfix: String to append to dashboard name if destination_dashboard_name is None
        verbose: Whether to print detailed information

    Returns:
        ID of the newly created dashboard
    """
    # Validate parameters - need table mapping
    if not table_name_mapping:
        raise ValueError("table_name_mapping must be provided as a dictionary mapping source to target table names")
    
    # Get source dashboard ID if only name was provided
    if not source_dashboard_id:
        if not source_dashboard_name:
            raise ValueError('Either the name or id of the source dashboard must be provided.')
        else:
            source_dashboard_id = mb.get_item_id(
                item_type='dashboard',
                item_name=source_dashboard_name,
                collection_id=source_collection_id,
                collection_name=source_collection_name
            )

    # Get destination collection ID if only name was provided
    if not destination_collection_id:
        if not destination_collection_name:
            raise ValueError('Either the name or id of the destination collection must be provided.')
        else:
            destination_collection_id = mb.get_item_id('collection', destination_collection_name)

    # Set destination dashboard name if not provided
    if not destination_dashboard_name:
        if not source_dashboard_name:
            source_dashboard_name = mb.get_item_name(item_type='dashboard', item_id=source_dashboard_id)
        destination_dashboard_name = source_dashboard_name + postfix

    # Get the source dashboard details
    source_dashboard = mb.get(f'/api/dashboard/{source_dashboard_id}')
    
    # Create a new empty dashboard in the destination collection
    new_dashboard_json = {
        'name': destination_dashboard_name,
        'collection_id': destination_collection_id
    }
    res = mb.post('/api/dashboard', json=new_dashboard_json)
    new_dashboard_id = res['id']
    
    if verbose:
        print(f"Created new empty dashboard '{destination_dashboard_name}' with ID {new_dashboard_id}")
    
    # Create a collection for the cloned cards
    cards_collection_json = {
        'name': destination_dashboard_name + "'s cards",
        'color': '#509EE3',
        'parent_id': destination_collection_id
    }
    res = mb.post('/api/collection/', json=cards_collection_json)
    cards_collection_id = res['id']
    
    if verbose:
        print(f"Created cards collection '{cards_collection_json['name']}' with ID {cards_collection_id}")
    
    # Get all cards in the source dashboard (excluding text boxes)
    card_ids = [card['card_id'] for card in source_dashboard['dashcards'] if card['card_id'] is not None]
    
    # Cache for table ID lookups to avoid repeated API calls
    table_id_cache = {}
    
    # Clone each card with the new table and create a mapping
    card_id_mapping = {}
    for card_id in card_ids:
        if verbose:
            print(f"Processing card ID {card_id}...")
            
        # Get card details to determine its source table
        card_details = mb.get(f'/api/card/{card_id}')
        
        # Get the source table name
        source_table_id = None
        card_query = card_details.get('dataset_query', {})
        if card_query.get('type') == 'query':
            source_table_id = card_query.get('query', {}).get('source-table')
        elif card_query.get('type') == 'native':
            # For native queries, we need to parse the SQL to find the table name
            # This is more complex, but we'll look for table names in the query
            sql_query = card_query.get('native', {}).get('query', '')
            
            # Try to find table names in the SQL
            for source_table_name in table_name_mapping.keys():
                if source_table_name in sql_query:
                    if verbose:
                        print(f"  Found table reference to '{source_table_name}' in native query")
                    
                    # Get or cache the table IDs
                    if source_table_name not in table_id_cache:
                        try:
                            table_id_cache[source_table_name] = mb.get_item_id('table', source_table_name)
                        except:
                            if verbose:
                                print(f"  Could not find table ID for '{source_table_name}'")
                            continue
                            
                    source_table_id = table_id_cache[source_table_name]
                    break
        
        if not source_table_id:
            if verbose:
                print(f"  Could not determine source table for card {card_id}, skipping...")
            continue
            
        # Get the source table name
        if str(source_table_id) not in table_id_cache.values():
            source_table_name = mb.get_item_name('table', source_table_id)
        else:
            # Find the key for this value in the cache
            source_table_name = next(
                (name for name, id in table_id_cache.items() if id == source_table_id), 
                None
            )
            if not source_table_name:
                source_table_name = mb.get_item_name('table', source_table_id)
                
        if verbose:
            print(f"  Card uses source table: '{source_table_name}' (ID: {source_table_id})")
            
        # Check if this source table has a mapping
        if source_table_name not in table_name_mapping:
            if verbose:
                print(f"  No mapping defined for table '{source_table_name}', skipping card...")
            continue
            
        target_table_name = table_name_mapping[source_table_name]
        
        # Get or cache the target table ID
        if target_table_name not in table_id_cache:
            try:
                table_id_cache[target_table_name] = mb.get_item_id('table', target_table_name)
            except:
                if verbose:
                    print(f"  Could not find target table '{target_table_name}', skipping card...")
                continue
                
        target_table_id = table_id_cache[target_table_name]
        
        if verbose:
            print(f"  Cloning card with table switch: '{source_table_name}' -> '{target_table_name}'")
            
        # Use clone_card to create a copy with the target table
        try:
            cloned_card = mb.clone_card(
                card_id=card_id,
                source_table_id=source_table_id,
                source_table_name=source_table_name,
                target_table_id=target_table_id,
                target_table_name=target_table_name,
                new_card_collection_id=cards_collection_id,
                ignore_these_filters=ignore_these_filters,
                return_card=True
            )
            
            card_id_mapping[card_id] = cloned_card['id']
            
            if verbose:
                print(f"  Card {card_id} cloned as {cloned_card['id']}")
        except Exception as e:
            if verbose:
                print(f"  Error cloning card: {str(e)}")
            continue
    
    # Add cards to the new dashboard
    for dashcard in source_dashboard['dashcards']:
        # Copy text cards directly
        if dashcard['card_id'] is None:
            if verbose:
                print(f"Adding text card to dashboard...")
                
            text_card_json = {
                'cardId': None,
                'row': dashcard['row'],
                'col': dashcard['col'],
                'size_x': dashcard['size_x'],
                'size_y': dashcard['size_y'],
                'visualization_settings': dashcard['visualization_settings']
            }
            mb.post(f'/api/dashboard/{new_dashboard_id}/cards', json=text_card_json)
        else:
            # Add cloned cards
            if dashcard['card_id'] in card_id_mapping:
                if verbose:
                    print(f"Adding card {dashcard['card_id']} → {card_id_mapping[dashcard['card_id']]} to dashboard...")
                
                card_json = {
                    'cardId': card_id_mapping[dashcard['card_id']],
                    'row': dashcard['row'],
                    'col': dashcard['col'],
                    'size_x': dashcard['size_x'],
                    'size_y': dashcard['size_y'],
                    'visualization_settings': dashcard['visualization_settings'],
                    'series': dashcard.get('series', [])
                }
                
                # Copy parameter mappings with updated card IDs
                parameter_mappings = []
                for mapping in dashcard.get('parameter_mappings', []):
                    new_mapping = mapping.copy()
                    new_mapping['card_id'] = card_id_mapping[dashcard['card_id']]
                    parameter_mappings.append(new_mapping)
                
                card_json['parameter_mappings'] = parameter_mappings
                
                mb.post(f'/api/dashboard/{new_dashboard_id}/cards', json=card_json)
    
    # Copy dashboard parameters
    if 'parameters' in source_dashboard:
        params_update = {'parameters': source_dashboard['parameters']}
        mb.put(f'/api/dashboard/{new_dashboard_id}', json=params_update)
        
        if verbose:
            print(f"Copied {len(source_dashboard['parameters'])} dashboard parameters")
    
    return new_dashboard_id 


if __name__ == "__main__":
    # GET API key from .env
    api_key = os.getenv('API_KEY')
    
    mb = Metabase_API(domain='https://bc-metabase-sandbox.up.railway.app', api_key=api_key)
    
    # Define the table name mappings
    table_mapping = {
        "jobs": "jobs_topcoat", 
        "jobs_cost_items_ted": "jobs_cost_items_topcoat", 
        "latest_job_costs": "latest_job_costs_topcoat"
    }
    
    # Copy dashboard with table mapping
    new_dashboard_id = copy_dashboard_with_table_mapping(
        mb=mb,
        source_dashboard_id=9,
        source_collection_id=5,
        destination_collection_id=34,
        destination_dashboard_name="Topcoat Demo",
        table_name_mapping=table_mapping,
        verbose=True
    )

    print(f"Created new dashboard with ID: {new_dashboard_id}")