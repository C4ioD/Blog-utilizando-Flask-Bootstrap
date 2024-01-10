from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, EqualTo, Length, DataRequired


class Formlogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(),Email()])
  senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
  botao_submit_login = SubmitField('Entrar')
  lembrar_user = BooleanField('Lembrar Senha')
  

class FormCriarConta(FlaskForm):
  username = StringField('Nome do Usuario', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(message='Campo obrigatório'), Email(message='E-mail invalido')])
  senha = PasswordField('Senha', validators=[DataRequired(message='Campo obrigatório'),Length(min=6,max=20, message='Senha deve possuir de 6 a 20 caracteres')])
  confirmar_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(),Length(6,20), EqualTo(senha, message='Senhas divergentes')])
  botao_criar_conta = SubmitField('Criar Conta')