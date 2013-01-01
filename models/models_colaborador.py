#coding: utf-8

from sqlalchemy import Column, Integer, String
from database import Base

class Colaborador(Base):
    __tablename__ = 'tbl_colaboradores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    tipo = Column(String(30)) # Funcionario, PJ, Estagiario
    departamento = Column(String(30))

    def __init__(self, nome, tipo, departamento):
        self.nome = nome
        self.tipo = tipo
        self.departamento = departamento

    def __repr__(self):
       return "<Colaborador('%s', '%s','%s', '%s')>" % (self.id, self.nome, self.tipo, self.departamento)