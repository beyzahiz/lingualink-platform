from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.auth import UserRegister, UserLogin, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"] # Swagger dokümantasyonunda bu endpointleri gruplamak için
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    # 1. Bu email adresiyle daha önce kayıt olunmuş mu kontrol et
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bu email adresi zaten kullanımda."
        )
    
    # 2. Şifreyi hash'le ve yeni kullanıcı objesini oluştur
    hashed_pwd = hash_password(user_data.password)
    new_user = User(
        email=user_data.email,
        password_hash=hashed_pwd,
        name=user_data.name
    )
    
    # 3. Veritabanına kaydet ve kaydı onayla
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Kullanıcı başarıyla oluşturuldu", "user_id": new_user.id}


@router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    # 1. Kullanıcıyı email adresine göre veritabanında ara
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Hatalı email veya şifre."
        )
    
    # 2. Girilen şifre veritabanındaki hash ile uyuşuyor mu kontrol et
    if not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Hatalı email veya şifre."
        )
    
    # 3. Bilgiler doğruysa kullanıcı için bir JWT (access token) üret
    # Token içerisine kullanıcının id'sini koyuyorum kim olduğunu isteklerden anlayabilmek için
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}