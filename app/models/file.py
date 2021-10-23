from app.config import db

from sqlalchemy.ext.hybrid import hybrid_property


class File(db.Model):
    __tablename__ = "Documento"
    id = db.Column("id_Documento", db.Integer, autoincrement=True, primary_key=True)
    __filename = db.Column("Documento", db.String, unique=False, nullable=False)
    __id_user = db.Column("id_Usuario", db.Integer, db.ForeignKey('Usuario.id_Usuario'), nullable=False)
    __id_store = db.Column("id_Loja", db.Integer, db.ForeignKey('Loja.id_Loja'), nullable=False)
    __id_transaction = db.Column("id_Transacao", db.Integer, db.ForeignKey('Transacao.id_Transacao'), nullable=False)
    __date = db.Column("Data", db.Date, unique=False, nullable=False)
    __time = db.Column("Hora", db.Time, unique=False, nullable=False)
    __value = db.Column("Valor", db.Float, unique=False, nullable=False)
    __card_number = db.Column("Cartao", db.String, unique=False, nullable=False)

    def __init__(self, filename, id_user, id_store, id_transaction, date, time, value, card_number):
        self.__filename = filename
        self.__id_user = id_user
        self.__id_store = id_store
        self.__id_transaction = id_transaction
        self.__date = date
        self.__time = time
        self.__value = value
        self.__card_number = card_number

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

    # id_store
    @hybrid_property
    def id_store(self):
        return self.__id_store

    # id_transaction
    @hybrid_property
    def id_transaction(self):
        return self.__id_transaction

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

    # card_number
    @hybrid_property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, card_number):
        self.__card_number = card_number
