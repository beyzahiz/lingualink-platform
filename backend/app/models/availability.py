from sqlalchemy import Column, Integer, ForeignKey, String, Time
from app.database import Base

class Availability(Base):
    __tablename__ = "availabilities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    day_of_week = Column(String, nullable=False)  
    start_time = Column(Time, nullable=False)     
    end_time = Column(Time, nullable=False)       