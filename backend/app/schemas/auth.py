from pydantic import BaseModel, EmailStr, Field

# Kullanıcı kayıt olurken göndermek zorunda olduğu veriler (register)
class UserRegister(BaseModel):
    email: EmailStr # Geçerli bir email formatı olması zorunluluğu
    password: str = Field(..., min_length=6, description="Şifre en az 6 karakter olmalıdır")
    name: str | None = None

# Kullanıcı giriş yaparken göndereceği veriler (login)
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Kullanıcı başarıyla giriş yaptığında dönecek cevap formatı
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"