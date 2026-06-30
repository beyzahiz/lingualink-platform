import os
import bcrypt  # Doğrudan modern bcrypt paketi
from datetime import datetime, timedelta, timezone
from jose import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "CokGizliBirStandartAnahtarMvpIcin")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7

# 1. Şifreyi hash'leyen fonksiyon
def hash_password(password: str) -> str:
    # bcrypt, string yerine byte verisi kabul ettiği için önce encode 
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Veritabanına kaydetmek için tekrar string (utf-8) formatı
    return hashed.decode('utf-8')

# 2. Şifreyi doğrulayan fonksiyon
def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes)

# 3. JWT üreten fonksiyon 
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt