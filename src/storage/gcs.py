from google.cloud import storage, exceptions


def authenticate_implicit_with_adc(project_id: str = "lobbyregisterwatch") -> None:
    """
    When interacting with Google Cloud Client libraries, the library can auto-detect the
    credentials to use.

    // TODO(Developer):
    //  1. Before running this sample,
    //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    //  2. Replace the project variable.
    //  3. Make sure that the user account or service account that you are using
    //  has the required permissions. For this sample, you must have "storage.buckets.list".
    Args:
        project_id: The project id of your Google Cloud project.
    """

    # This snippet demonstrates how to list buckets.
    # *NOTE*: Replace the client created below with the client required for your application.
    # Note that the credentials are not specified when constructing the client.
    # Hence, the client library will look for credentials using ADC.
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")


def upload_blob(bucket_name, source_string, destination_blob_name, project_id):
  """Uploads a file to the bucket."""
  storage_client = storage.Client(project_id)
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_string(source_string)

def download_blob(bucket_name, blob_name, project_id):
    storage_client = storage.Client(project_id)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    try:
        return blob.download_as_string()
    except exceptions.NotFound:
        return None
    except Exception as e:
        raise e
