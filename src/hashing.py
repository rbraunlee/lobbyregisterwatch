import hashlib

def hash_content(content: str) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def has_changed(content: str, previous_hash: str | None) -> bool:
    return hash_content(content) != previous_hash

def load_previous_hash(bucket_name: str, blobl_name: str, project_id: str) -> str | None:
    raise NotImplementedError

def save_hash(bucket_name: str, blob_name: str, hash_value: str, project_id: str) -> None:
    raise NotImplementedError
