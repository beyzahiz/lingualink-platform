import os
from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

# Şifreleme algoritması olarak bcrypt 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT imzalamak için kullanılacak gizli anahtar ve algoritma ayarları
SECRET_KEY = os.getenv("SECRET_KEY", "CokGizliBirStandartAnahtarMvpIcin")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7 # Token 7 gün boyunca geçerli olsun 

# 1. Ham şifreyi alıp hash'e dönüştüren fonksiyon (Kayıt esnasında kullanacağız)
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# 2. Girilen şifre ile veritabanındaki hash'in uyuşup uyuşmadığını doğrulayan fonksiyon (Giriş esnasında kullanacağız)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# 3. Giriş başarılı olduğunda kullanıcıya özel JWT üreten fonksiyon
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    
    # Token'ın geçerlilik süresi (son kullanma tarihi) 
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    
    # Veriyi SECRET_KEY kullanarak şifreliyoruz ve imzalı bir token string'i üretiyoruz
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt