import os
import json
from dotenv import load_dotenv
from datetime import date

from api.rest import call_lr
from storage.gcs import upload_blob




def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    base_url = 'https://api.lobbyregister.bundestag.de/rest/v2/'
    endpoint = 'registerentries'
    header = {"Authorization":f"ApiKey {api_key}"}
    params = {"cursor":None}
    response = []
    response.extend(call_lr(base_url=base_url, endpoint=endpoint, header=header, params=params))

    json_str = json.dumps(response)

    with open("json_str.json", "w") as f:
        f.write(json_str)

    upload_blob(bucket_name='lrw-weu-bucket01',
                source_string= json_str,
                destination_blob_name=f'{date.today()}_lrw_results.json',
                project_id='lobbyregisterwatch')


if __name__ == "__main__":
    main()
