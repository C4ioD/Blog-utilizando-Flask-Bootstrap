from app_blog import db, login_manager
from datetime import datetime 
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
  return Usuario.query.get(int(id_usuario))


class Usuario(db.Model, UserMixin):
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String, nullable = False, unique=True)
  email = db.Column(db.String, nullable = False, unique=True)
  senha = db.Column(db.String, nullable=False)
  foto_perfil = db.Column(db.String, default='default.jpg')
  posts = db.relationship('Post', backref='autor', lazy= True)
  cursos = db.Column(db.String, nullable = False, default='Não informado')

  def contar_posts(self):
    return len(self.posts)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer , db.ForeignKey('usuario.id'), nullable= False)
  titulo = db.Column(db.String, nullable = False)
  descricao = db.Column(db.String, nullable = False)
  data_criacao = db.Column(db.DateTime, nullable= False , default= datetime.utcnow)
