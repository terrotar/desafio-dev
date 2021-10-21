from app.config import db
from sqlalchemy.ext.hybrid import hybrid_property


class Transaction(db.Model):
    __tablename__ = "Tipo_Transacao"
    id = db.Column("id_Transacao", db.Integer, primary_key=True)
    __description = db.Column("Descricao", db.String, unique=True, nullable=False)
    __nature = db.Column("Natureza", db.String, nullable=False)
    __signal = db.Column("Sinal", db.String, unique=False, nullable=False)

    # Relationship
    files = db.relationship('File', backref='transaction', lazy=True)

    def __init__(self, description, nature, signal):
        self.__description = description
        self.__nature = nature
        self.__signal = signal

    # GETTERS and SETTERS

    # description
    @hybrid_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    # nature
    @hybrid_property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature):
        self.__nature = nature

    # signal
    @hybrid_property
    def signal(self):
        return self.__signal

    @signal.setter
    def signal(self, signal):
        self.__signal = signal
