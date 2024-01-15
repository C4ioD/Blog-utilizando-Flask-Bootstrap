from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, EqualTo, Length, DataRequired, ValidationError
import email_validator
from flask_login import current_user
from app_blog.models import Usuario

class Formlogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(),Email()])
  senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
  botao_submit_login = SubmitField('Entrar')
  lembrar_user = BooleanField('Lembrar Senha')

class FormEditarPerfil(FlaskForm):
  username = StringField('Nome do Usuario', validators=[DataRequired(message='Campo obrigatório')])
  email = StringField('E-mail', validators=[DataRequired(),Email()])
  foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png'])])
  botao_submit_edit_login = SubmitField('Salvar')
  
  def validate_email (self, email):
      usuario = Usuario.query.filter_by(email=email.data).first()
      if usuario:
        raise ValidationError ('E-mail já cadastrado')

  def validate_username(self, username):
      usuario = Usuario.query.filter_by(username= username.data).first()
      if usuario:
        raise ValidationError('Usuario já cadastrado. Insira um novo')
  

class FormCriarConta(FlaskForm):
  username = StringField('Nome do Usuario', validators=[DataRequired(message='Campo obrigatório')])
  email = StringField('E-mail', validators=[DataRequired(message='Campo obrigatório'), Email(message='E-mail invalido')])
  senha = PasswordField('Senha', validators=[DataRequired(message='Campo obrigatório'),Length(min=6,max=20, message='Senha deve possuir de 6 a 20 caracteres')])
  confirmar_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo("senha", message='Senhas divergentes')])
  botao_criar_conta = SubmitField('Criar Conta')

  def validate_email (self, email):
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario:
      raise ValidationError ('E-mail já cadastrado')
    
  def validate_username(self, username):
    usuario = Usuario.query.filter_by(username= username.data).first()
    if usuario:
      raise ValidationError('Usuario já cadastrado. Cadastre-se com outro usuario.')
