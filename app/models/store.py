from app.config import db

from sqlalchemy.ext.hybrid import hybrid_property


class Store(db.Model):
    __tablename__ = "Loja"
    id = db.Column("id_Loja", db.Integer, autoincrement=True, primary_key=True)
    __owner = db.Column("Dono", db.String, unique=False, nullable=False)
    __cpf = db.Column("CPF", db.String, unique=False, nullable=False)
    __name = db.Column("Nome", db.String, unique=True, nullable=False)
    __balance = db.Column("Saldo", db.Float, unique=False, nullable=False)

    # Relationship
    files = db.relationship('File', backref='store', lazy=True)

    def __init__(self, owner, cpf, name, balance):
        self.__owner = owner
        self.__cpf = cpf
        self.__name = name
        self.__balance = balance

    # GETTERS and SETTERS

    # owner
    @hybrid_property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    # cpf
    @hybrid_property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # name
    @hybrid_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # balance
    @hybrid_property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance
