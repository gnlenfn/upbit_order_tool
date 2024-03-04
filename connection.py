import jwt
import hashlib
import os
import uuid
from urllib.parse import urlencode, unquote

from model import Order

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']


def get_authorize(query: str):
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query,
        'query_hash_algorithm': 'SHA512'
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorization = f'Bearer {jwt_token}'
    headers = {"Authorization": authorization}

    return headers


def hash_query(query: dict):
    query_string = unquote(urlencode(query, doseq=True)).encode("utf-8")
    m = hashlib.sha512()
    m.update(query_string)

    return m.hexdigest()
