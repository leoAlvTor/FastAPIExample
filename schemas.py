from datetime import date
from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    CODIGO: str
    CANTIDADINTERNA: int
    CATEGORIA: str
    CODIGOPRINCIPAL: str
    FECHA: date
    IMPUESTO: str
    NOMBRE: str
    NOMBREPRINCIPAL: str
    PRECIOCAJA: float
    PRECIOCAJA12: float
    PRECIOUNITARIO: float
    PRECIOUNITARIO12: float
    PRECIOVENTACAJA: float
    PRECIOVENTAUNIDAD: float
    REPRESENTACION: str
    STOCKPAQUETE: float
    STOCKUNIDAD: Optional[float] = 0
    PROVEEDOR_RUC: str
    PROMOCION: Optional[str] = 'NA'

    class Config:
        orm_mode = True
