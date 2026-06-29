from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False) # Giriş için benzersiz olmalı
    password_hash = Column(String, nullable=False) #hashlenecek
    name = Column(String, nullable=True)
    photo_url = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    city = Column(String, nullable=True)
    university = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # Kayıt tarihi otomatik alınır