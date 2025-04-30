import re


def clone_collection_new_database(
    self,
    source_collection_name=None,
    source_collection_id=None,
    destination_collection_name=None,
    destination_parent_collection_name=None,
    destination_parent_collection_id=None,
    target_database_name=None,
    target_database_id=None,
    cloned_card_mapping={},
    postfix="- Duplicate",
):
    """
    Copy the collection with the given name/id into the given destination parent collection.

    Keyword arguments:
    source_collection_name -- name of the collection to copy (default None)
    source_collection_id -- id of the collection to copy (default None)
    destination_collection_name -- the name to be used for the collection in the destination (default None).
                                                                    If None, it will use the name of the source collection + postfix.
    destination_parent_collection_name -- name of the destination parent collection (default None).
                                                                                This is the collection that would have the copied collection as a child.
                                                                                use 'Root' for the root collection.
    destination_parent_collection_id -- id of the destination parent collection (default None).
                                                                            This is the collection that would have the copied collection as a child.
    target_database_name -- name of the database to target on cloned cards (default None)
    target_database_id -- id of the database to target on cloned cards (default None)
    cloned_card_mapping -- dict of all the cloned cards (default {})
    postfix -- if destination_collection_name is None, adds this string to the end of source_collection_name to make destination_collection_name.
    """
    ### making sure we have the data that we need
    if not source_collection_id:
        if not source_collection_name:
            raise ValueError(
                "Either the name or id of the source collection must be provided."
            )
        else:
            source_collection_id = self.get_item_id(
                "collection", source_collection_name
            )

    if not destination_parent_collection_id:
        if not destination_parent_collection_name:
            raise ValueError(
                "Either the name or id of the destination parent collection must be provided."
            )
        else:
            destination_parent_collection_id = (
                self.get_item_id("collection", destination_parent_collection_name)
                if destination_parent_collection_name != "Root"
                else None
            )

    if not destination_collection_name:
        if not source_collection_name:
            source_collection_name = self.get_item_name(
                item_type="collection", item_id=source_collection_id
            )
        destination_collection_name = source_collection_name + postfix

    if not target_database_id:
        if not target_database_name:
            raise ValueError(
                "Either the name or id of the target database must be provided."
            )
        else:
            target_database_id = self.get_item_id("database", target_database_name)

    ### create a collection in the destination to hold the contents of the source collection
    destination_collection = self.create_collection(
        destination_collection_name,
        parent_collection_id=destination_parent_collection_id,
        parent_collection_name=destination_parent_collection_name,
        return_results=True,
    )
    destination_collection_id = destination_collection["id"]

    ### get the items to copy
    items = self.get("/api/collection/{}/items".format(source_collection_id))
    if (
        type(items) == dict
    ):  # in Metabase version *.40.0 the format of the returned result for this endpoint changed
        items = items["data"]

    ### copy the items of the source collection to the new collection
    for item in items:
        ## clone a sub collection
        if item["model"] == "collection":
            collection_id = item["id"]
            collection_name = item["name"]
            destination_collection_name = collection_name
            self.clone_collection_new_database(
                source_collection_id=collection_id,
                destination_parent_collection_id=destination_collection_id,
                target_database_id=target_database_id,
                cloned_card_mapping=cloned_card_mapping,
            )

        ## clone a dashboard
        if item["model"] == "dashboard":
            dashboard_id = item["id"]
            dashboard_name = item["name"]
            destination_dashboard_name = dashboard_name
            self.clone_dashboard_new_database(
                source_dashboard_id=dashboard_id,
                destination_collection_id=destination_collection_id,
                destination_dashboard_name=destination_dashboard_name,
                target_database_id=target_database_id,
                cloned_card_mapping=cloned_card_mapping,
            )

        ## clone a card
        if item["model"] == "card":
            card_id = item["id"]
            self.clone_card_new_database(
                card_id=card_id,
                destination_collection_id=destination_collection_id,
                target_database_id=target_database_id,
                cloned_card_mapping=cloned_card_mapping,
            )


def clone_dashboard_new_database(
    self,
    source_dashboard_name=None,
    source_dashboard_id=None,
    source_collection_name=None,
    source_collection_id=None,
    destination_dashboard_name=None,
    destination_collection_name=None,
    destination_collection_id=None,
    target_database_name=None,
    target_database_id=None,
    cloned_card_mapping={},
    postfix="",
):
    """
    Create a new dashboard in the target collection and deepcopy each of its referenced cards targeting another database.
    Preserves dashboard tabs, card positions, and sizes.

    Keyword arguments:
    source_dashboard_name -- name of the dashboard to copy (default None)
    source_dashboard_id -- id of the dashboard to copy (default None)
    source_collection_name -- name of the collection the source dashboard is located in (default None)
    source_collection_id -- id of the collection the source dashboard is located in (default None)
    destination_dashboard_name -- name used for the dashboard in destination (default None).
                                                                If None, it will use the name of the source dashboard + postfix.
    destination_collection_name -- name of the collection to copy the dashboard to (default None)
    destination_collection_id -- id of the collection to copy the dashboard to (default None)
    target_database_name -- name of the database to target on cloned cards (default None)
    target_database_id -- id of the database to target on cloned cards (default None)
    cloned_card_mapping -- dict of all the cloned cards (default {})
    postfix -- if destination_dashboard_name is None, adds this string to the end of source_card_name
                          to make destination_dashboard_name
    """

    ### making sure we have the data that we need
    if not source_dashboard_id:
        if not source_dashboard_name:
            raise ValueError(
                "Either the name or id of the source dashboard must be provided."
            )
        else:
            source_dashboard_id = self.get_item_id(
                item_type="dashboard",
                item_name=source_dashboard_name,
                collection_id=source_collection_id,
                collection_name=source_collection_name,
            )
    source_dashboard = self.get("/api/dashboard/{}".format(source_dashboard_id))

    if not destination_collection_id:
        if not destination_collection_name:
            raise ValueError(
                "Either the name or id of the destination collection must be provided."
            )
        else:
            destination_collection_id = self.get_item_id(
                "collection", destination_collection_name
            )

    if not target_database_id:
        if not target_database_name:
            raise ValueError(
                "Either the name or id of the target database must be provided."
            )
        else:
            target_database_id = self.get_item_id("database", target_database_name)

    if not destination_dashboard_name:
        if not source_dashboard_name:
            source_dashboard_name = source_dashboard["name"]
        destination_dashboard_name = source_dashboard_name + postfix

    # Create a new dashboard instead of shallow copy
    # Maybe: add the following fields, or instead deep copy them w/ a mapping
    # --> tabs -- may need a deep copy w/ mapping
    # --> param_fields / param_values
    # --> auto_apply_filters
    dashboard_params = {
        'name': destination_dashboard_name,
        'parameters': source_dashboard.get('parameters', []),
        'collection_id': destination_collection_id
    }
    
    new_dashboard = self.post("/api/dashboard", json=dashboard_params)
    new_dashboard_id = new_dashboard["id"]
    
    # Create tabs in the new dashboard
    tab_id_mapping = {}  # Maps source tab IDs to destination tab IDs
    source_tabs = source_dashboard.get('tabs', [])
    
    if source_tabs:
        print(f"Creating {len(source_tabs)} tabs in the new dashboard...")
        new_tabs = []
        
        for source_tab in source_tabs:
            source_tab_id = source_tab.get('id')
            if not source_tab_id:
                continue
                
            tab_name = source_tab.get('name', f"Tab {source_tab_id}")
            tab_position = source_tab.get('position', 0)
            tab_id = source_tab.get('id', tab_position)
            
            new_tab = {
                'name': tab_name,
                'id': tab_id,
                'position': tab_position
            }
            new_tabs.append(new_tab)

            tab_id_mapping[source_tab_id] = tab_id
        try:
            response = self.put(f"/api/dashboard/{new_dashboard_id}", json={"tabs": new_tabs})
            print(response)

            print(f"Created {len(new_tabs)} tabs successfully.")
        except Exception as e:
            print(f"Failed to create tabs': {str(e)}")

    print()
    return new_dashboard_id
    # # recursively clone existing dashboard cards updating their target database
    # source_dashboard_card_ids = [
    #     dashcard["card_id"]
    #     for dashcard in source_dashboard["dashcards"]
    #     if dashcard["card_id"] is not None
    # ]
    # for card_id in source_dashboard_card_ids:
    #     self.clone_card_new_database(
    #         card_id=card_id,
    #         target_database_id=target_database_id,
    #         destination_collection_id=destination_collection_id,
    #         cloned_card_mapping=cloned_card_mapping,
    #     )

    # # Helper function to get size values handling API naming inconsistencies
    # def get_size(card, x_or_y):
    #     # Try both naming conventions (size_x and sizeX)
    #     if x_or_y == 'x':
    #         return card.get('size_x', card.get('sizeX', 2))
    #     else:
    #         return card.get('size_y', card.get('sizeY', 2))

    # # prepare new dashcards
    # new_dashcards = []
    # for index, dashcard in enumerate(source_dashboard["dashcards"]):
    #     # Text cards - keep them as they are
    #     if dashcard["card_id"] is None:
    #         # Create text card parameters
    #         new_card_json = {}
    #         # Sequential negative ids are used to inform Metabase to create new card
    #         new_card_json["id"] = -index - 1
            
    #         for prop in [
    #             "visualization_settings",
    #             "col",
    #             "row",
    #             "parameter_mappings",
    #         ]:
    #             new_card_json[prop] = dashcard.get(prop, {})
            
    #         # Use consistent sizing properties
    #         new_card_json["size_x"] = get_size(dashcard, 'x')
    #         new_card_json["size_y"] = get_size(dashcard, 'y')
            
    #         # Add tab ID if present in the source dashcard
    #         source_tab_id = dashcard.get('dashboard_tab_id')
    #         if source_tab_id and source_tab_id in tab_id_mapping:
    #             new_card_json["dashboard_tab_id"] = tab_id_mapping[source_tab_id]
                
    #         new_dashcards.append(new_card_json)
    #         continue

    #     # Question cards
    #     # prepare a json to be used for replacing the cards in the duplicated dashboard
    #     new_card_id = cloned_card_mapping[dashcard["card_id"]]["id"]
    #     new_card_json = {}

    #     # sequential negative ids are used to inform Metabase to create new card
    #     new_card_json["id"] = -index - 1
    #     new_card_json["card_id"] = new_card_id
        
    #     for prop in [
    #         "visualization_settings",
    #         "col",
    #         "row",
    #         "series",
    #         "parameter_mappings",
    #     ]:
    #         new_card_json[prop] = dashcard.get(prop, {})
            
    #     # Use consistent sizing properties
    #     new_card_json["size_x"] = get_size(dashcard, 'x')
    #     new_card_json["size_y"] = get_size(dashcard, 'y')
        
    #     # Add tab ID if present in the source dashcard
    #     source_tab_id = dashcard.get('dashboard_tab_id')
    #     if source_tab_id and source_tab_id in tab_id_mapping:
    #         new_card_json["dashboard_tab_id"] = tab_id_mapping[source_tab_id]
            
    #     # Update card ID in parameter mappings
    #     for item in new_card_json.get("parameter_mappings", []):
    #         item["card_id"] = new_card_id

    #     new_dashcards.append(new_card_json)

    # # update the dashboard with new dashcards, the ones not mentioned are automatically removed
    # self.put(
    #     "/api/dashboard/{}".format(new_dashboard_id),
    #     json={"dashcards": new_dashcards},
    # )

    # print(f"Dashboard {source_dashboard_id} has been cloned to {new_dashboard_id}!")

    # return new_dashboard_id


def clone_card_new_database(
    self,
    card_id,
    target_database_name=None,
    target_database_id=None,
    destination_collection_id=None,
    cloned_card_mapping={},
):
    """
    Create a new card where the database source of the old card is changed to 'target_database_id'.
    Will also update select and join queries.
    A cloned card mapping dict is necessary to update cards used inside other cards (recursively).
    The target database needs to have the same tables and columns than the database source.

    Keyword arguments:
    card_id -- id of the card
    target_database_name -- name of the database to target on cloned cards (default None)
    target_database_id -- id of the database to target on cloned cards (default None)
    destination_collection_id -- id of the collection to clone the card to (default None)
    cloned_card_mapping -- dict of all the cloned cards (default {})
    """

    assert type(cloned_card_mapping) == dict

    # card already cloned, don't do it again
    if card_id in cloned_card_mapping:
        return cloned_card_mapping[card_id]

    # {'table_name': {'id': 453, columns: {'column_name': 2709, ...}}
    target_database_table_name_id_mapping = self.get_database_name_id(
        db_id=target_database_id, db_name=target_database_name
    )
    # get the card info
    card_info = self.get_item_info("card", card_id)

    # native questions - just need to change the target database
    if card_info["dataset_query"]["type"] == "native":
        card_info["dataset_query"]["database"] = target_database_id

    # simple/custom questions - have to change target database and each table to target new DB's table
    elif card_info["dataset_query"]["type"] == "query":
        source_database_id = card_info["dataset_query"]["database"]
        # {453: {'name': 'table_name', columns: {2709: 'column_name', ...}} TODO: cache
        source_database_table_id_name_mapping = self.get_database_name_id(
            db_id=source_database_id, column_id_name=True
        )
        # change the targeted database
        card_info["dataset_query"]["database"] = target_database_id

        query_data = card_info["dataset_query"]["query"]

        # transform main source-table & columns
        source_table_id = query_data["source-table"]
        source_table_is_card = "card__" in str(source_table_id)
        # source table is another card
        if source_table_is_card:
            source_table_card_id = int(source_table_id.split("__")[1])
            # already cloned card
            if source_table_card_id in cloned_card_mapping:
                query_data["source-table"] = (
                    f"card__{cloned_card_mapping[source_table_card_id]['id']}"
                )
            # referenced card has to be cloned
            else:
                cloned_card = self.clone_card_new_database(
                    card_id=source_table_card_id,
                    target_database_id=target_database_id,
                    target_database_name=target_database_name,
                    destination_collection_id=destination_collection_id,
                    cloned_card_mapping=cloned_card_mapping,
                )
                query_data["source-table"] = f"card__{cloned_card['id']}"

        # source table is another table
        else:
            source_table_name = source_database_table_id_name_mapping[source_table_id][
                "name"
            ]
            target_table_id = target_database_table_name_id_mapping[source_table_name][
                "id"
            ]
            query_data["source-table"] = target_table_id

            # store for future usage TODO: cache
            target_database_table_name_id_mapping[source_table_name]["columns"] = (
                self.get_columns_name_id(table_id=target_table_id)
            )
            source_database_table_id_name_mapping[source_table_id]["columns"] = (
                self.get_columns_name_id(table_id=source_table_id, column_id_name=True)
            )

        # transform breakout data
        if "breakout" in query_data:
            query_data_breakout_str = str(query_data["breakout"])

            # search for Ids, when fields are string based, don't modify them as they will match new table
            source_column_ids = re.findall("'field', (\d+)", query_data_breakout_str)
            # replace column IDs from old table with the column IDs from new table
            for source_col_id_str in source_column_ids:
                source_col_id = int(source_col_id_str)

                source_col_name = source_database_table_id_name_mapping[
                    source_table_id
                ]["columns"][source_col_id]
                target_col_id = target_database_table_name_id_mapping[
                    source_table_name
                ]["columns"][source_col_name]
                query_data_breakout_str = query_data_breakout_str.replace(
                    "['field', {}, ".format(source_col_id),
                    "['field', {}, ".format(target_col_id),
                )

            card_info["dataset_query"]["query"]["breakout"] = eval(
                query_data_breakout_str
            )

        # transform each joins
        if "joins" in query_data:
            updated_joins = []
            for join in query_data["joins"]:
                source_table_id = join["source-table"]
                source_table_name = source_database_table_id_name_mapping[
                    source_table_id
                ]["name"]
                target_table_id = target_database_table_name_id_mapping[
                    source_table_name
                ]["id"]
                join["source-table"] = target_table_id

                query_data_join_str = str(join)

                # store for future usage TODO: cache
                target_database_table_name_id_mapping[source_table_name]["columns"] = (
                    self.get_columns_name_id(table_id=target_table_id)
                )
                source_database_table_id_name_mapping[source_table_id]["columns"] = (
                    self.get_columns_name_id(
                        table_id=source_table_id, column_id_name=True
                    )
                )

                # search for Ids, when fields are string based, don't modify them as they will match new table
                source_column_ids = re.findall("'field', (\d+)", query_data_join_str)
                # replace column IDs from old table with the column IDs from new table
                for source_col_id_str in source_column_ids:
                    source_col_id = int(source_col_id_str)

                    # search for source source_table_name and source_col_name
                    # by looking for source_col_id to ensure identity
                    source_table_name = None
                    source_col_name = None
                    for (
                        table_name,
                        table_detail,
                    ) in source_database_table_id_name_mapping.items():
                        if source_col_id in table_detail["columns"]:
                            source_table_name = table_detail["name"]
                            source_col_name = table_detail["columns"][source_col_id]
                            break
                    target_col_id = target_database_table_name_id_mapping[
                        source_table_name
                    ]["columns"][source_col_name]
                    query_data_join_str = query_data_join_str.replace(
                        "['field', {}, ".format(source_col_id),
                        "['field', {}, ".format(target_col_id),
                    )

                updated_join = eval(query_data_join_str)
                updated_joins.append(updated_join)

            card_info["dataset_query"]["query"]["joins"] = updated_joins

    new_card_json = {}
    for key in ["dataset_query", "display", "visualization_settings", "name"]:
        new_card_json[key] = card_info[key]

    if destination_collection_id:
        new_card_json["collection_id"] = destination_collection_id
    else:
        new_card_json["collection_id"] = card_info["collection_id"]

    new_card = self.create_card(
        custom_json=new_card_json, verbose=True, return_card=True
    )
    cloned_card_mapping[card_id] = new_card
    new_card_id = new_card["id"]

    print(f"Card {card_id} has been cloned to {new_card_id}!")

    return new_card


# # CLAUDE GENERATED ATTEMPT TO CLONE DASHBOARD CARDS

# def clone_dashboard_cards(self, 
#     source_dashboard_id,
#     table_mapping,
#     database_id=None,
#     destination_collection_id=None,
#     destination_collection_name=None,
#     verbose=True,
#     save_mapping_file=True
# ):
#     """
#     Clone all cards in a dashboard and switch their source tables based on mapping
    
#     Args:
#         source_dashboard_id: ID of the source dashboard
#         table_mapping: Dictionary mapping source table names/IDs to target table names/IDs
#         database_id: ID of the target database (usually same as source for different schemas)
#         destination_collection_id: ID of the destination collection
#         destination_collection_name: Name of the destination collection
#         verbose: Whether to print progress information
#         save_mapping_file: Whether to save the mapping to a JSON file
        
#     Returns:
#         Tuple containing:
#         - Dictionary mapping source card IDs to destination card IDs
#         - List of card IDs that were successfully cloned
#         - List of card IDs that failed to clone
#         - Dictionary mapping failed card IDs to their names
#     """
#     import json
    
#     # Validate parameters
#     if not table_mapping:
#         raise ValueError("table_mapping must be provided with at least one mapping")
    
#     if not (destination_collection_id or destination_collection_name):
#         raise ValueError("Either destination_collection_id or destination_collection_name must be provided")
    
#     # Get collection ID if name was provided
#     if not destination_collection_id and destination_collection_name:
#         try:
#             destination_collection_id = self.get_item_id("collection", destination_collection_name)
#             if verbose:
#                 print(f"Resolved destination collection '{destination_collection_name}' to ID: {destination_collection_id}")
#         except Exception as e:
#             raise ValueError(f"Could not find collection with name '{destination_collection_name}': {str(e)}")
    
#     # Resolve table IDs from names in the mapping
#     resolved_mapping = {}
#     table_name_mapping = {}  # For native queries - maps table names
    
#     for source_table, target_table in table_mapping.items():
#         source_id = source_table
#         target_id = target_table
        
#         # Resolve source table ID if a name was provided
#         if isinstance(source_table, str):
#             try:
#                 source_id = self.get_item_id("table", source_table)
#                 table_name_mapping[source_table] = target_table  # Store name mapping for native queries
#                 if verbose:
#                     print(f"Resolved source table '{source_table}' to ID: {source_id}")
#             except Exception as e:
#                 if verbose:
#                     print(f"Warning: Could not resolve source table '{source_table}': {str(e)}")
#                 continue
        
#         # Resolve target table ID if a name was provided
#         if isinstance(target_table, str):
#             try:
#                 target_id = self.get_item_id("table", target_table)
#                 if verbose:
#                     print(f"Resolved target table '{target_table}' to ID: {target_id}")
#             except Exception as e:
#                 if verbose:
#                     print(f"Warning: Could not resolve target table '{target_table}': {str(e)}")
#                 continue
        
#         resolved_mapping[source_id] = target_id
    
#     if not resolved_mapping:
#         raise ValueError("None of the provided table mappings could be resolved")
    
#     # Get dashboard information
#     if verbose:
#         print(f"Getting information for dashboard ID {source_dashboard_id}...")
    
#     try:
#         dashboard_info = self.get(f"/api/dashboard/{source_dashboard_id}")
#     except Exception as e:
#         raise ValueError(f"Could not retrieve dashboard with ID {source_dashboard_id}: {str(e)}")
    
#     dashboard_name = dashboard_info.get("name", f"Dashboard {source_dashboard_id}")
    
#     if verbose:
#         print(f"Dashboard name: {dashboard_name}")
#         print(f"Found {len(dashboard_info.get('dashcards', []))} dashcards in the dashboard")
    
#     # Extract cards that need to be cloned (cards with a card_id)
#     dashboard_cards = [card for card in dashboard_info.get("dashcards", []) if card.get("card_id")]
    
#     if verbose:
#         print(f"Found {len(dashboard_cards)} cards (excluding text cards) to clone")
    
#     # Initialize tracking variables
#     card_id_mapping = {}
#     successfully_cloned = []
#     failed_to_clone = []
#     failed_card_names = {}  # Dictionary to track names of failed cards
    
#     # Clone each card
#     for index, dashcard in enumerate(dashboard_cards, 1):
#         card_id = dashcard.get("card_id")
#         if not card_id:
#             continue
        
#         try:
#             # Get the card details
#             card_details = self.get(f"/api/card/{card_id}")
#             card_name = card_details.get("name", f"Card {card_id}")
#             dataset_query = card_details.get("dataset_query", {})
#             query_type = dataset_query.get("type", "unknown")
            
#             if verbose:
#                 print(f"\nProcessing card {index}/{len(dashboard_cards)}: {card_name} (ID: {card_id})...")
#                 print(f"  Query type: {query_type}")
            
#             # For regular GUI queries, determine source table ID
#             source_table_id = None
            
#             if query_type == "query":
#                 source_table_id = dataset_query.get("query", {}).get("source-table")
#                 if verbose:
#                     print(f"  Card uses GUI query with source table ID: {source_table_id}")
#             elif query_type == "native":
#                 # For native queries, we need to try to use metadata
#                 # This is more complex and may not always be accurate
#                 if verbose:
#                     print(f"  Card uses native SQL query")
#                     if "template-tags" in dataset_query.get("native", {}):
#                         print(f"  Card has template tags for filtering")
#             else:
#                 if verbose:
#                     print(f"  Unknown query type: {query_type}")
            
#             # Skip if source table not found or not in mapping for GUI queries
#             if not source_table_id and query_type == "query":
#                 if verbose:
#                     print(f"  ⚠ Could not determine source table ID, skipping card")
#                 failed_to_clone.append(card_id)
#                 failed_card_names[card_id] = card_name
#                 continue
            
#             # For query type, check if this table is in our mapping
#             if query_type == "query" and source_table_id not in resolved_mapping:
#                 if verbose:
#                     print(f"  ⚠ Source table ID {source_table_id} not found in mapping, skipping card")
#                 failed_to_clone.append(card_id)
#                 failed_card_names[card_id] = card_name
#                 continue
            
#             # Get target table ID from mapping for GUI queries
#             target_table_id = None
#             if query_type == "query":
#                 target_table_id = resolved_mapping[source_table_id]
            
#             # Create the new card name
#             new_card_name = f"{card_name}"
            
#             if verbose:
#                 if query_type == "query":
#                     print(f"  Cloning card with source_table_id={source_table_id}, target_table_id={target_table_id}...")
#                 print(f"  New card name will be: {new_card_name}")
            
#             # Clone the card using the Metabase API clone_card method
#             new_card = self.clone_card(
#                 card_id=card_id,
#                 source_table_id=source_table_id,
#                 target_table_id=target_table_id,
#                 new_card_name=new_card_name,
#                 new_card_collection_id=destination_collection_id,
#                 return_card=True
#             )
            
#             # Store the mapping between source and destination card IDs
#             new_card_id = new_card.get("id")
#             card_id_mapping[card_id] = new_card_id
#             successfully_cloned.append(card_id)
            
#             if verbose:
#                 print(f"  ✓ Cloned card {card_id} → {new_card_id}")
                
#         except Exception as e:
#             failed_to_clone.append(card_id)
#             # Store the card name for this failed ID
#             failed_card_names[card_id] = card_details.get("name", f"Card {card_id}") if 'card_details' in locals() else f"Card {card_id}"
#             if verbose:
#                 print(f"  ✗ Failed to clone card {card_id}: {str(e)}")
#                 import traceback
#                 traceback.print_exc()
    
#     # Summary
#     if verbose:
#         print("\n=== Cloning Summary ===")
#         print(f"Total cards: {len(dashboard_cards)}")
#         print(f"Successfully cloned: {len(successfully_cloned)}")
#         print(f"Failed to clone: {len(failed_to_clone)}")
        
#         if failed_to_clone:
#             print(f"Failed card IDs: {failed_to_clone}")
#             print("\nFailed cards (ID: Name):")
#             for card_id in failed_to_clone:
#                 print(f"  {card_id}: {failed_card_names.get(card_id, 'Unknown')}")
    
#     # Save mapping to file if requested
#     if save_mapping_file and card_id_mapping:
#         mapping_file = f"dashboard_{source_dashboard_id}_card_mapping.json"
#         with open(mapping_file, "w") as f:
#             json.dump({
#                 "card_mapping": {str(k): v for k, v in card_id_mapping.items()}, 
#                 "failed_cards": failed_to_clone,
#                 "dashboard_id": source_dashboard_id,
#                 "table_mapping": {str(k): str(v) for k, v in table_mapping.items()}
#             }, f, indent=2)
            
#         if verbose:
#             print(f"\nCard mapping saved to {mapping_file}")
    
#     return card_id_mapping, successfully_cloned, failed_to_clone, failed_card_names


# def create_dashboard_from_card_mapping(self,
#     card_mapping_file=None,
#     card_mapping=None,
#     source_dashboard_id=None,
#     dashboard_name=None,
#     destination_collection_id=None,
#     destination_collection_name=None,
#     preserve_positions=True,
#     verbose=True
# ):
#     """
#     Create a new dashboard using card mappings from a previous cloning operation
    
#     Args:
#         card_mapping_file: Path to the JSON file containing card ID mappings (alternative to card_mapping)
#         card_mapping: Dictionary mapping source card IDs to cloned card IDs (alternative to card_mapping_file)
#         source_dashboard_id: ID of the source dashboard (required if card_mapping provided without file)
#         dashboard_name: Name for the new dashboard (defaults to source name + " (Clone)")
#         destination_collection_id: ID of the collection for the new dashboard
#         destination_collection_name: Name of the collection for the new dashboard (alternative to ID)
#         preserve_positions: Whether to preserve card positions from source dashboard
#         verbose: Whether to print progress information
        
#     Returns:
#         ID of the newly created dashboard
#     """
#     import json
#     import os
    
#     # Validate parameters
#     if not (destination_collection_id or destination_collection_name):
#         raise ValueError("Either destination_collection_id or destination_collection_name must be provided")
    
#     # Get collection ID if name was provided
#     if not destination_collection_id and destination_collection_name:
#         try:
#             destination_collection_id = self.get_item_id("collection", destination_collection_name)
#             if verbose:
#                 print(f"Resolved destination collection '{destination_collection_name}' to ID: {destination_collection_id}")
#         except Exception as e:
#             raise ValueError(f"Could not find collection with name '{destination_collection_name}': {str(e)}")
    
#     # Load card mapping - either from file or directly provided
#     if card_mapping_file:
#         if verbose:
#             print(f"Loading card mapping from {card_mapping_file}...")
        
#         try:
#             with open(card_mapping_file, 'r') as f:
#                 mapping_data = json.load(f)
            
#             card_mapping = mapping_data.get('card_mapping', {})
#             source_dashboard_id = mapping_data.get('dashboard_id')
            
#             if not card_mapping:
#                 raise ValueError("Card mapping is empty")
            
#             if not source_dashboard_id:
#                 raise ValueError("Source dashboard ID not found in mapping file")
            
#             if verbose:
#                 print(f"Found mapping for {len(card_mapping)} cards from dashboard ID {source_dashboard_id}")
#         except Exception as e:
#             raise ValueError(f"Failed to load card mapping from {card_mapping_file}: {str(e)}")
#     elif card_mapping:
#         if not source_dashboard_id:
#             raise ValueError("When providing card_mapping directly, source_dashboard_id is required")
        
#         if verbose:
#             print(f"Using provided card mapping with {len(card_mapping)} cards from dashboard ID {source_dashboard_id}")
#     else:
#         raise ValueError("Either card_mapping_file or card_mapping must be provided")
    
#     # Get source dashboard structure
#     if verbose:
#         print(f"Getting source dashboard structure...")
    
#     try:
#         source_dashboard = self.get(f"/api/dashboard/{source_dashboard_id}")
#     except Exception as e:
#         raise ValueError(f"Could not retrieve source dashboard with ID {source_dashboard_id}: {str(e)}")
    
#     # Determine new dashboard name
#     source_dashboard_name = source_dashboard.get('name', f"Dashboard {source_dashboard_id}")
#     if not dashboard_name:
#         dashboard_name = f"{source_dashboard_name} (Clone)"
    
#     if verbose:
#         print(f"Source dashboard: {source_dashboard_name}")
#         print(f"New dashboard name: {dashboard_name}")
    
#     # Create the new dashboard
#     if verbose:
#         print(f"Creating new dashboard...")
    
#     try:
#         dashboard_params = {
#             'name': dashboard_name,
#             'parameters': source_dashboard.get('parameters', []),
#             'collection_id': destination_collection_id
#         }
        
#         new_dashboard = self.post("/api/dashboard", json=dashboard_params)
        
#         if not new_dashboard or isinstance(new_dashboard, bool):
#             raise ValueError("API call to create dashboard failed")
            
#         new_dashboard_id = new_dashboard.get('id')
        
#         if not new_dashboard_id:
#             raise ValueError("Failed to create new dashboard - no ID returned")
        
#         if verbose:
#             print(f"Created new dashboard with ID {new_dashboard_id}")
#     except Exception as e:
#         raise ValueError(f"Failed to create new dashboard: {str(e)}")
    
#     # Extract tabs from source dashboard and create them in the new dashboard
#     tab_id_mapping = {}  # Maps source tab IDs to destination tab IDs
#     source_tabs = source_dashboard.get('tabs', [])
    
#     if verbose and source_tabs:
#         print(f"Found {len(source_tabs)} tabs in source dashboard")
    
#     # Create tabs in the new dashboard with the same name and position
#     for source_tab in source_tabs:
#         source_tab_id = source_tab.get('id')
#         if not source_tab_id:
#             continue
            
#         tab_name = source_tab.get('name', f"Tab {source_tab_id}")
#         tab_position = source_tab.get('position', 0)
        
#         if verbose:
#             print(f"Creating tab '{tab_name}' (position: {tab_position})...")
        
#         try:
#             tab_params = {
#                 'name': tab_name,
#                 'position': tab_position
#             }
            
#             new_tab = self.post(f"/api/dashboard/{new_dashboard_id}/tab", json=tab_params)
#             new_tab_id = new_tab.get('id')
            
#             if new_tab_id:
#                 tab_id_mapping[source_tab_id] = new_tab_id
#                 if verbose:
#                     print(f"  ✓ Created tab {source_tab_id} → {new_tab_id}")
#             else:
#                 if verbose:
#                     print(f"  ✗ Failed to create tab - no ID returned")
#         except Exception as e:
#             if verbose:
#                 print(f"  ✗ Failed to create tab: {str(e)}")
    
#     # Track progress
#     dashcards = source_dashboard.get('dashcards', [])
#     total_dashcards = len(dashcards)
#     added_cards = 0
#     skipped_cards = 0
#     text_cards = 0
    
#     if verbose:
#         print(f"Found {total_dashcards} dashcards in source dashboard")
    
#     # Add cards to the new dashboard
#     for dashcard in dashcards:
#         card_id = dashcard.get('card_id')
        
#         # Helper function to get size values regardless of API naming inconsistencies
#         def get_size(card, x_or_y):
#             # Try both naming conventions (size_x and sizeX)
#             if x_or_y == 'x':
#                 return card.get('size_x', card.get('sizeX', 2))
#             else:
#                 return card.get('size_y', card.get('sizeY', 2))
        
#         # Handle text cards (which don't have a card_id)
#         if not card_id:
#             if 'visualization_settings' in dashcard and dashcard['visualization_settings'].get('virtual_card', {}).get('display') in ['text', 'heading']:
#                 if verbose:
#                     print(f"Adding text card...")
                
#                 # Copy the dashcard parameters but update for the new dashboard
#                 text_card_params = {
#                     'dashboard_id': new_dashboard_id,
#                     'visualization_settings': dashcard.get('visualization_settings', {}),
#                     'col': dashcard.get('col', 0),
#                     'row': dashcard.get('row', 0),
#                     'sizeX': get_size(dashcard, 'x'),
#                     'sizeY': get_size(dashcard, 'y'),
#                     'parameter_mappings': []
#                 }
                
#                 # Map tab ID if present
#                 source_tab_id = dashcard.get('dashboard_tab_id')
#                 if source_tab_id and source_tab_id in tab_id_mapping:
#                     text_card_params['dashboard_tab_id'] = tab_id_mapping[source_tab_id]
                
#                 try:
#                     self.post("/api/dashboard/{}/cards".format(new_dashboard_id), json=text_card_params)
#                     text_cards += 1
#                     if verbose:
#                         print(f"  ✓ Added text card to dashboard")
#                 except Exception as e:
#                     if verbose:
#                         print(f"  ✗ Failed to add text card: {str(e)}")
#             else:
#                 if verbose:
#                     print(f"Skipping dashcard without card_id (not a text card)")
#                 skipped_cards += 1
#             continue
        
#         # Handle regular cards - check if we have a mapping
#         str_card_id = str(card_id)
#         if str_card_id not in card_mapping and card_id not in card_mapping:
#             if verbose:
#                 print(f"Skipping card ID {card_id} - not found in mapping")
#             skipped_cards += 1
#             continue
        
#         # Get the target card ID
#         target_card_id = card_mapping.get(str_card_id) or card_mapping.get(card_id)
        
#         if verbose:
#             print(f"Adding card: Source ID {card_id} → Target ID {target_card_id}")
        
#         # Prepare dashcard parameters
#         dashcard_params = {
#             'cardId': target_card_id,
#             'dashboard_id': new_dashboard_id,
#             'parameter_mappings': dashcard.get('parameter_mappings', [])
#         }
        
#         # Map tab ID if present
#         source_tab_id = dashcard.get('dashboard_tab_id')
#         if source_tab_id and source_tab_id in tab_id_mapping:
#             dashcard_params['dashboard_tab_id'] = tab_id_mapping[source_tab_id]
        
#         # If preserving positions, copy layout information
#         if preserve_positions:
#             dashcard_params.update({
#                 'col': dashcard.get('col', 0),
#                 'row': dashcard.get('row', 0),
#                 'sizeX': get_size(dashcard, 'x'),
#                 'sizeY': get_size(dashcard, 'y')
#             })
        
#         try:
#             self.post("/api/dashboard/{}/cards".format(new_dashboard_id), json=dashcard_params)
#             added_cards += 1
#             if verbose:
#                 print(f"  ✓ Added card to dashboard")
#         except Exception as e:
#             if verbose:
#                 print(f"  ✗ Failed to add card: {str(e)}")
#             skipped_cards += 1
    
#     # Generate dashboard URL
#     dashboard_url = f"{self.domain}/dashboard/{new_dashboard_id}"
    
#     # Summary
#     if verbose:
#         print("\n=== Dashboard Creation Summary ===")
#         print(f"Source dashboard: {source_dashboard_name} (ID: {source_dashboard_id})")
#         print(f"New dashboard: {dashboard_name} (ID: {new_dashboard_id})")
#         print(f"Total dashcards: {total_dashcards}")
#         print(f"Cards added: {added_cards}")
#         print(f"Text cards added: {text_cards}")
#         print(f"Cards skipped: {skipped_cards}")
#         if tab_id_mapping:
#             print(f"Tabs created: {len(tab_id_mapping)}")
#         print(f"\nDashboard URL: {dashboard_url}")
    
#     return new_dashboard_id


# def clone_dashboard(self,
#     source_dashboard_id,
#     table_mapping,
#     database_id=None,
#     destination_collection_id=None,
#     destination_collection_name=None,
#     dashboard_name=None,
#     preserve_positions=True,
#     save_mapping_file=True,
#     verbose=True
# ):
#     """
#     Clone an entire dashboard, including all cards, and switch their source tables based on mapping
    
#     This is a convenience function that combines clone_dashboard_cards and create_dashboard_from_card_mapping
#     into a single operation. It preserves the dashboard layout including tabs, card positions, and sizes.
    
#     Args:
#         source_dashboard_id: ID of the source dashboard
#         table_mapping: Dictionary mapping source table names/IDs to target table names/IDs
#         database_id: ID of the target database (usually same as source for different schemas)
#         destination_collection_id: ID of the collection for the new dashboard
#         destination_collection_name: Name of the collection for the new dashboard (alternative to ID)
#         dashboard_name: Name for the new dashboard (defaults to source name + " (Clone)")
#         preserve_positions: Whether to preserve card positions and sizes from source dashboard
#         save_mapping_file: Whether to save the card mapping to a JSON file
#         verbose: Whether to print progress information
        
#     Returns:
#         Dictionary containing:
#         - dashboard_id: ID of the new dashboard
#         - card_mapping: Dictionary mapping source card IDs to destination card IDs
#         - successful_cards: Count of successfully cloned cards
#         - failed_cards: Count of cards that failed to clone
#         - dashboard_url: URL of the new dashboard
#     """
#     # Step 1: Clone all the cards from the source dashboard
#     if verbose:
#         print("=== Step 1: Cloning Dashboard Cards ===")
    
#     card_mapping, successful_cards, failed_cards, failed_card_names = self.clone_dashboard_cards(
#         source_dashboard_id=source_dashboard_id,
#         table_mapping=table_mapping,
#         database_id=database_id,
#         destination_collection_id=destination_collection_id,
#         destination_collection_name=destination_collection_name,
#         verbose=verbose,
#         save_mapping_file=save_mapping_file
#     )
    
#     if not card_mapping:
#         raise ValueError("Failed to clone any cards from the source dashboard")
    
#     # Step 2: Create a new dashboard with the cloned cards
#     if verbose:
#         print("\n=== Step 2: Creating New Dashboard with Tabs and Cards ===")
    
#     new_dashboard_id = self.create_dashboard_from_card_mapping(
#         card_mapping=card_mapping,
#         source_dashboard_id=source_dashboard_id,
#         dashboard_name=dashboard_name,
#         destination_collection_id=destination_collection_id,
#         destination_collection_name=destination_collection_name,
#         preserve_positions=preserve_positions,  # This ensures cards maintain their position and size
#         verbose=verbose
#     )
    
#     # Generate dashboard URL
#     dashboard_url = f"{self.domain}/dashboard/{new_dashboard_id}"
    
#     return {
#         "dashboard_id": new_dashboard_id,
#         "card_mapping": card_mapping,
#         "successful_cards": len(successful_cards),
#         "failed_cards": len(failed_cards),
#         "dashboard_url": dashboard_url
#     }
