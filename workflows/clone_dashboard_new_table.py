"""
Test script to clone a dashboard using the combined dashboard cloning script.
"""

import os
from dotenv import load_dotenv
from metabase_api import Metabase_API

# Load environment variables
load_dotenv()

DOMAIN = os.getenv('DOMAIN')
API_KEY = os.getenv('API_KEY')

# Initialize Metabase API connection
mb = Metabase_API(
    domain=DOMAIN,
    api_key=API_KEY
)

# Dashboard source settings
# SOURCE_DASHBOARD_NAME = os.getenv('SOURCE_DASHBOARD_NAME')
SOURCE_DASHBOARD_ID = os.getenv('SOURCE_DASHBOARD_ID')
# SOURCE_COLLECTION_NAME = os.getenv('SOURCE_COLLECTION_NAME')
SOURCE_COLLECTION_ID = os.getenv('SOURCE_COLLECTION_ID')

# Dashboard destination settings
DESTINATION_DASHBOARD_NAME = os.getenv('DESTINATION_DASHBOARD_NAME')
# DESTINATION_COLLECTION_NAME = os.getenv('DESTINATION_COLLECTION_NAME')
DESTINATION_COLLECTION_ID = os.getenv('DESTINATION_COLLECTION_ID')

# Target database settings
TARGET_DATABASE_ID = os.getenv('TARGET_DATABASE_ID')

# Additional dashboard cloning options
# POSTFIX = os.getenv('DESTINATION_DASHBOARD_NAME')
# DEEPCOPY = os.getenv('DEEPCOPY')

if __name__ == "__main__":
    print(f"Testing deep dashboard cloning for dashboard {SOURCE_DASHBOARD_ID}")
    print(f"Destination collection: {DESTINATION_COLLECTION_ID}")
    
    try:
        # Insert call to clone dashboard here
        new_dashboard_id = mb.clone_dashboard_new_database(source_dashboard_id=SOURCE_DASHBOARD_ID,
                                            source_collection_id=SOURCE_COLLECTION_ID,
                                            destination_dashboard_name=DESTINATION_DASHBOARD_NAME,
                                            destination_collection_id=DESTINATION_COLLECTION_ID,
                                            targ  et_database_id=TARGET_DATABASE_ID)
        
        print(f"\nSUCCESS! Your cloned dashboard is available at: {DOMAIN}/dashboard/{new_dashboard_id}")
        
    except Exception as e:
        print(f"\nERROR during cloning: {str(e)}")
        import traceback
        traceback.print_exc() 