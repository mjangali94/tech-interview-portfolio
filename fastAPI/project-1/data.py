# list of products with 4 products like phones, laptops, pens, tables
from schemas.products import Product


products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50,available=True),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30,available=True),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100,available=True),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20,available=True),
]
