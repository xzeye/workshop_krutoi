from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel, Field
from app.models import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    full_name = Column(String(128), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

class UserBase(BaseModel):
    username: str = Field(min_length=2, max_length=64)
    is_active: bool = True
    full_name: str | None = Field(default=None, max_length=128)

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=64)

class UserUpdate(UserBase):
    username: str | None = Field(default=None, min_length=2, max_length=64)
    password: str | None = Field(default=None, min_length=8, max_length=64)
    full_name: str | None = Field(default=None, max_length=128)

class UserOut(UserBase):
    id: int
    model_config = {'from_attributes': True}