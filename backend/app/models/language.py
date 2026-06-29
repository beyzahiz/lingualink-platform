import enum
from sqlalchemy import Column, Integer, ForeignKey, Enum, Boolean
from app.database import Base

class LanguageEnum(enum.Enum):
    EN = "EN"
    DE = "DE"
    ES = "ES"
    FR = "FR"

class LevelEnum(enum.Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

class UserLanguage(Base):
    __tablename__ = "user_languages"

    id = Column(Integer, primary_key=True, index=True)
    # Foreignkeyle bu dilin hangi kullanıcıya ait olduğunu bağlanıyor
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    language = Column(Enum(LanguageEnum), nullable=False)
    level = Column(Enum(LevelEnum), nullable=False)
    is_learning = Column(Boolean, default=True, nullable=False) # Öğreniyor mu yoksa öğretiyor mu ayrımı