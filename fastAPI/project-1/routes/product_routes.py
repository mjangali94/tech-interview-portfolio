from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.products import Product
from typing import Optional
from models.products import Product as ProductModel
from database import get_db
router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
async def get_products(db:Session = Depends(get_db)):
    db_products = db.query(ProductModel).all()
    return db_products


@router.get("/{product_id}")
async def get_product(product_id: int, db:Session=Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        return {"message": "Product not found"}
    else:
        return product


@router.post("/")
async def create_product(product: Product, db:Session=Depends(get_db)):
    db.add(ProductModel(**product.model_dump()))
    db.commit()
    return product


@router.put("/")
async def update_product(product_id:int, product: Product, db:Session=Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.available = product.available
        db.commit()
        return product
    else:
        return {"message": "Product not found"}



@router.delete("/")
async def delete_product(product_id: int, db:Session=Depends(get_db)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted"}
    else:
        return {"message": "Product not found"}


@router.get("/search")
async def search_products(
        name: Optional[str] = None,
        description: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        db:Session=Depends(get_db)):
    query = db.query(ProductModel)
    if name:
        db_product = query.filter(ProductModel.name.ilike(f"%{name}%"))
    elif description:
        db_product = query.filter(ProductModel.description.ilike(f"%{description}%"))
    elif min_price:
        db_product = query.filter(ProductModel.price > min_price)
    elif max_price:
        db_product = query.filter(ProductModel.price < max_price)

    results = db_product.all()
    return results

@router.get("/paginated")
async def get_products_paginated(skip:int =0, limit:int=10, db:Session=Depends(get_db)):
    query = db.query(ProductModel).offset(skip).limit(limit).all()
    return {
        "page_start":skip,
        "page_length":limit,
        "products":query
        }


