from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class MunicipioIn(BaseModel):
    nombre: str

class DepartamentoIn(BaseModel):
    nombre: str
    municipios: List[str]

class SubregionIn(BaseModel):
    nombre: str
    departamentos: List[DepartamentoIn]


class Subregion(Base):
    __tablename__ = 'subregion'  # ✅ Coincide con tu SQL
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    departamentos = relationship('Departamento', cascade="all, delete", back_populates='subregion')

class Departamento(Base):
    __tablename__ = 'subregion_departamento'  # ✅ Coincide con tu SQL
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    subregion_id = Column(Integer, ForeignKey('subregion.id'))  # ✅ FK corregida

    subregion = relationship('Subregion', back_populates='departamentos')
    municipios = relationship('Municipio', cascade="all, delete", back_populates='departamento')

class Municipio(Base):
    __tablename__ = 'subregion_municipio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    subregion_departamento_id = Column(Integer, ForeignKey('subregion_departamento.id'))  # Renombrado correctamente

    departamento = relationship('Departamento', back_populates='municipios')
