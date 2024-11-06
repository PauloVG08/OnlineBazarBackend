from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product, Sale
from pydantic import BaseModel

router = APIRouter()

@router.get("/api/items")
def search_items(q: str, db: Session = Depends(get_db)):
    products = db.query(Product).filter(
        (Product.title.ilike(f"%{q}%")) | (Product.description.ilike(f"%{q}%"))
    ).all()
    
    if not products:
        raise HTTPException(status_code=404, detail="No se encontraron productos")
    
    return products

@router.get("/api/items/{id}")
def get_item(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product

class SaleRequest(BaseModel):
    product_id: int
    title: str
    description: str
    price: float
    thumbnail: str

@router.post("/api/addSale")
def add_sale(sale_request: SaleRequest, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == sale_request.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    sale = Sale(
        product_id=sale_request.product_id,
        title=sale_request.title,
        description=sale_request.description,
        price=sale_request.price,
        thumbnail=sale_request.thumbnail,
    )

    try:
        db.add(sale)
        db.commit()
        return {"success": True}
    except Exception as e:
        db.rollback()
        print("Error al registrar la venta:", e)
        return {"success": False}

@router.get("/api/sales/")
def get_sales(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    return sales
