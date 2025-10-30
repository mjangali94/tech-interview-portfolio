from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

import schemas.products
from models.products import Product as ProductModel
from models.products import Category as ProductCategoryModel
from models import products
from database import get_db

router =APIRouter(prefix="/category", tags=["category"])

@router.get("/")
async def get_categories(db:Session=Depends(get_db)):
    categories = db.query(ProductCategoryModel).all()
    return categories

@router.post("/")
async def create_category(category: schemas.products.Category, db:Session=Depends(get_db)):
    new_category = db.add(ProductCategoryModel(**category.model_dump()))
    db.commit()
    return new_category

@router.put("/")
async def update_category(category: schemas.products.Category, db:Session=Depends(get_db)):
    category_db = db.query(ProductCategoryModel).filter(ProductCategoryModel.id == category.id).first()
    if category_db is None:
        raise HTTPException(status_code=404, detail="Category not found")
    else:
        category_db.name = category.name
        db.commit()
        return category_db





