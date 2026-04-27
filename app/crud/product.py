from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

# CREATE
def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# READ ALL
def get_products(db: Session):
    return db.query(Product).all()

# READ ONE
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# UPDATE
def update_product(db: Session, product_id: int, product_data: ProductCreate):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None

    for key, value in product_data.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

# DELETE
def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None

    db.delete(product)
    db.commit()
    return product