from app import db
from sqlalchemy_utils import ChoiceType

class Client(db.Model):
    __tablename__ = "clients"

    SEX_CHOICES = [
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
        (u'N', u'Nenhuma das opções')
    ]

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    data_nascimento = db.Column(db.Datetime)
    profession = db.Column(db.String(30))
    sex = db.Column(ChoiceType=SEX_CHOICES)