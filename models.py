from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from database import Base


class Producto(Base):
    __tablename__ = 'PRODUCTO'

    CODIGO = Column(String, primary_key=True, index=True)
    CANTIDADINTERNA = Column(Integer)
    CATEGORIA = Column(String)
    CODIGOPRINCIPAL = Column(String)
    FECHA = Column(Date)
    IMPUESTO = Column(String)
    NOMBRE = Column(String)
    NOMBREPRINCIPAL = Column(String)
    PRECIOCAJA = Column(Float)
    PRECIOCAJA12 = Column(Float)
    PRECIOUNITARIO = Column(Float)
    PRECIOUNITARIO12 = Column(Float)
    PRECIOVENTACAJA = Column(Float)
    PRECIOVENTAUNIDAD = Column(Float)
    REPRESENTACION = Column(String)
    STOCKPAQUETE = Column(Float)
    STOCKUNIDAD = Column(Float)
    PROVEEDOR_RUC = Column(String)
    PROMOCION = Column(String)
