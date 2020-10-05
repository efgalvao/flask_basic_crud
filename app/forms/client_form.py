from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email


class ClientForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = EmailField("email", validators=[Email(), DataRequired()])
    dob = DateField("date_of_birth", validators=[DataRequired()])
    profession = StringField("profession", validators=[DataRequired()])
    gender = SelectField("gender", validators=[DataRequired()], choices=[('M', 'Masculino'), ('F', 'Feminino'),
                                                                         ('N', 'Nenhuma das opções')])
