import os
import json
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import date

from storage.gcs import upload_blob





def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    base_url = 'https://api.lobbyregister.bundestag.de/rest/v2'
    endpoint = 'registerentries'
    header = {"Authorization":f"ApiKey {api_key}"}
    params = {"cursor":None}

    upload_blob(bucket_name='lrw-weu-bucket01',
                source_string= json_str,
                destination_blob_name=f'{date.today()}_lrw_results.json',
                project_id='lobbyregisterwatch')


if __name__ == "__main__":
    main()
