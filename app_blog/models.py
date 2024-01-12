from app_blog import db
from datetime import datetime

class Usuario(db.Model):
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String, nullable = False, unique=True)
  email = db.Column(db.String, nullable = False, unique=True)
  senha = db.Column(db.String, nullable=False)
  foto_perfil = db.Column(db.String, default='default.jpg')
  posts = db.relationship('Post', backref='autor', lazy= True)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer , db.ForeignKey('usuario.id'), nullable= False)
  titulo = db.Column(db.String, nullable = False)
  descricao = db.Column(db.String, nullable = False)
  data_criacao = db.Column(db.DateTime, nullable= False , default= datetime.utcnow)
  cursos = db.Column(db.String, nullable = False, default='Não informado')
