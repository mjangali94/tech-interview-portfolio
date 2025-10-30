from fastapi import FastAPI
from database import session, engine
from data import products as products_dummy_data
from routes import product_routes, category_routes, user_router
from models import products as product_model
from models import user as user_model
app = FastAPI()


# product_model.Base.metadata.drop_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)



#initializing db with some dummy values
def init_db():
    db =session()
    existing_count = db.query(product_model.Product).count()
    if existing_count == 0:
        for product in products_dummy_data:
            db.add(product_model.Product(**product.model_dump()))
        db.commit()
        print("Database initialized with sample products.")
    db.close()

init_db()


app.include_router(product_routes.router)
app.include_router(category_routes.router)

app.include_router(user_router.router)

