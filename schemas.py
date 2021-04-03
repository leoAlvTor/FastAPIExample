from datetime import date
from pydantic import BaseModel


class Product(BaseModel):
    CODIGO = str
    CANTIDADINTERNA = int
    CATEGORIA = str
    CODIGOPRINCIPAL = str
    FECHA = date
    IMPUESTO = str
    NOMBRE = str
    NOMBREPRINCIPAL = str
    PRECIOCAJA = float
    PRECIOCAJA12 = float
    PRECIOUNITARIO = float
    PRECIOUNITARIO12 = float
    PRECIOVENTACAJA = float
    PRECIOVENTAUNIDAD = float
    REPRESENTACION = str
    STOCKPAQUETE = float
    STOCKUNIDAD = float
    PROVEEDOR_RUC = str
    PROMOCION = str

    class Config:
        orm_mode = True
