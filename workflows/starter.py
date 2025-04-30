"""
Starter file to work with the Metabase API.
"""

import json
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
    
    try:
        # Insert API logic here....
        # response = mb.get("/api/database/7")
        # print(json.dumps(response, indent=4))

        response = mb.clone_card_new_database(source_dashboard_id=SOURCE_DASHBOARD_ID,
                                    destination_collection_id=DESTINATION_COLLECTION_ID)
        print(json.dumps(response, indent=4))

    except Exception as e:
        print(f"\nERROR during execution: {str(e)}")
        import traceback
        traceback.print_exc() 