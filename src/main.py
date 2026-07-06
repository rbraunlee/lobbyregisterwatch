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

# dict_keys(['$schema', 'source', 'sourceUrl', 'sourceDate', 'jsonDocumentationUrl', 'searchParameters', 'resultCount', 'totalResultCount', 'cursor', 'results'])   sum = 0
    response = requests.get(os.path.join(base_url, endpoint), params=params, headers = header)
    print(response.json()['sourceDate'])
    results = response.json()["results"]
    # df = pd.json_normalize(results)
    # print(df[:5])
    # df.to_json("key_type_overview.json", orient="records")
    # print(df.columns)



    while True:
        response = requests.get(os.path.join(base_url, endpoint), params=params, headers = header)
        tmp =response.json()
        sum +=tmp["resultCount"]
        print(sum)
        if tmp["results"] ==[]:
            break
        results.append(tmp["results"])
        cursor = tmp["cursor"]
        if params["cursor"] ==cursor:
            break
        params = {"cursor":cursor}

    json_str = json.dumps(results)
    # with open("result.json", "w") as f:
    #     f.write(json_str)


    upload_blob(bucket_name='lrw-weu-bucket01',
                source_string= json_str,
                destination_blob_name=f'{date.today()}_lrw_results.json',
                project_id='lobbyregisterwatch')


if __name__ == "__main__":
    main()
