from pydantic import EmailStr
from sqlalchemy import Column, String, Integer, ForeignKey, Float,Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String,unique=True, index=True)
    username:Mapped[str] = mapped_column(String,unique=True, index=True)
    email:Mapped[EmailStr] = mapped_column(String,unique=True, index=True)
    password:Mapped[str] = mapped_column(String,unique=True, index=True)
    is_active:Mapped[bool] = mapped_column(Boolean)

    orders=relationship("Order", back_populates="user")