from datetime import datetime, timedelta, timezone
import jwt
from pwdlib import PasswordHash

SECRET_KEY = '98d8e6d9a64f920d770eb3b81e9badd6ddf334184f1d92c3ec53e839afab53ec'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({'exp': expire})

    encode_jwt = jwt.encode(
        payload = to_encode,
        key = SECRET_KEY,
        algorithm = ALGORITHM
    )
    return encode_jwt