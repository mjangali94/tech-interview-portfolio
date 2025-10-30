from sqlalchemy import Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from schemas.products import Product


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = 'category'
    id :Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True)
    products:Mapped[list["Product"]] = relationship("Product", back_populates="category",cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "product"

    id:Mapped[int] =mapped_column(Integer, primary_key=True, index=True)
    name:Mapped[str] =mapped_column(String)
    description:Mapped[str] =mapped_column(String)
    price:Mapped[float] =mapped_column(Float)
    available:Mapped[bool] =mapped_column(Boolean)
    category_id:Mapped[int | None] =mapped_column(ForeignKey("category.id"))
    category:Mapped["Category"] =relationship("Category", back_populates="products")
