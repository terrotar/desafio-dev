from app.config import db

from sqlalchemy.ext.hybrid import hybrid_property


class File(db.Model):
    __tablename__ = "Documento"
    id = db.Column("id_Documento", db.Integer, autoincrement=True, primary_key=True)
    __filename = db.Column("Nome_Documento", db.String, unique=False, nullable=False)
    __id_user = db.Column("id_Usuario", db.Integer, db.ForeignKey('Usuario.id_Usuario'), nullable=False)
    __id_transaction = db.Column("id_Transacao", db.Integer, db.ForeignKey('Tipo_Transacao.id_Transacao'), nullable=False)
    __date = db.Column("Data", db.Date, unique=False, nullable=False)
    __time = db.Column("Hora", db.Time, unique=False, nullable=False)
    __value = db.Column("Valor", db.Float, unique=False, nullable=False)
    __cpf = db.Column("CPF", db.String, unique=False, nullable=False)
    __card_number = db.Column("Numero_Cartao", db.String, unique=False, nullable=False)
    __owner = db.Column("Dono", db.String, unique=False, nullable=False)
    __store = db.Column("Loja", db.String, unique=False, nullable=False)

    def __init__(self, filename, id_user, id_transaction, date, time, value, cpf, card_number, owner, store):
        self.__filename = filename
        self.__id_user = id_user
        self.__id_transaction = id_transaction
        self.__date = date
        self.__time = time
        self.__value = value
        self.__cpf = cpf
        self.__card_number = card_number
        self.__owner = owner
        self.__store = store

    # GETTERS and SETTERS

    # filename
    @hybrid_property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        self.__filename = filename

    # id_user
    @hybrid_property
    def id_user(self):
        return self.__id_user

    # id_transaction
    @hybrid_property
    def id_transaction(self):
        return self.__id_transaction

    @id_transaction.setter
    def id_transaction(self, id_transaction):
        self.__id_transaction = id_transaction

    # date
    @hybrid_property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    # time
    @hybrid_property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    # value
    @hybrid_property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    # cpf
    @hybrid_property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # card_number
    @hybrid_property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, card_number):
        self.__card_number = card_number

    # owner
    @hybrid_property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    # store
    @hybrid_property
    def store(self):
        return self.__store

    @store.setter
    def store(self, store):
        self.__store = store
