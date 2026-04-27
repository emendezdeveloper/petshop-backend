from fastapi import FastAPI
from app.database import Base, engine
from app.models.product import Product
from app.routes.product import router as product_router

app = FastAPI(
    title="Petshop API",
    description="Backeend para tienda de mascotas",
    version="1.0.0",
)

@app.on_event("startup")
def startup():
    print("🚀Backend iniciado correctamente")

@app.get("/")
def read_root():
    return {"mensaje": "API de tienda de mascotas FUNCIONANDO!🚀"}

@app.get("/salud")
def health_check():
    return {"estado": "ok", "servicio": "petshop-backend"}    

app.include_router(product_router)
Base.metadata.create_all(bind=engine)    