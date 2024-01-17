
from app_blog import app, db , bcrypt
from app_blog.forms import Formlogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from app_blog.models import Usuario, Post
from flask import render_template, url_for, request, redirect , flash
from flask_login import login_user, logout_user, login_required, current_user
from PIL import Image
import secrets
import os


lista_usuarios = ['caio','jamila','luiz']

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login():
  form_login= Formlogin()

  if form_login.validate_on_submit():
    usuario = Usuario.query.filter_by(email=form_login.email.data).first()
    if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
      login_user(usuario, remember=form_login.lembrar_user.data)
      flash(f'Login realizado com Sucesso no e-mail {form_login.email.data}','alert-success')
      par_next = request.args.get('next')
      if par_next:
        return redirect(par_next)
      else:
        return redirect(url_for('home'))
    else:
      flash( f'Falha no login! E-mail ou Senha incorretos', 'alert-danger')

  return render_template("login.html" , form_login=form_login)

@app.route('/criarconta' , methods=['GET','POST'])
def criar_conta():
  form_criar_conta = FormCriarConta()

  if form_criar_conta.validate_on_submit():
    senhacrypt = bcrypt.generate_password_hash(str(form_criar_conta.senha.data))
    usuario = Usuario(username=form_criar_conta.username.data, email=form_criar_conta.email.data, senha=senhacrypt)
    db.session.add(usuario)
    db.session.commit()
    flash(f'Conta criada com sucesso no e-mail: {form_criar_conta.email.data}', 'alert-success')
    return redirect(url_for('home'))
  
  return render_template('criarconta.html', form_criar_conta = form_criar_conta)

@app.route("/contatos")
def contatos():
  return render_template("contatos.html")

@app.route("/usuarios", methods=['GET','POST'])
@login_required
def usuarios():
  usuarios = Usuario.query.all()
  return render_template("usuarios.html", usuarios=usuarios) 


@app.route('/sair')
@login_required
def sair():
  logout_user()
  flash(f'Logout feito com sucesso. Até Logo!','alert-success')
  return redirect(url_for('login'))


@app.route('/perfil')
@login_required
def perfil():
  foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
  return render_template('perfil.html', foto_perfil=foto_perfil)

def salvar_imagem(imagem):
  codigo = secrets.token_hex(8)
  nome, extensao = os.path.splitext(imagem.filename)
  nome_arquivo = nome + codigo + extensao
  caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
  tamanho = (200,200)
  imagem_reduzida = Image.open(imagem)
  imagem_reduzida.thumbnail(tamanho)
  imagem_reduzida.save(caminho_completo)
  return nome_arquivo





@app.route('/perfil/editar',methods=['GET','POST'])
@login_required
def editar_perfil():
  form_edit_perfil = FormEditarPerfil()

  def atualizar_len(form):
      lista = []
      for campo in form:
        if "bo_" in campo.name:
          if campo.data:
            lista.append(campo.label.text)
      return ";".join(lista)
  
  if form_edit_perfil.validate_on_submit():
    current_user.username = form_edit_perfil.username.data
    current_user.email = form_edit_perfil.email.data
    if form_edit_perfil.foto_perfil.data:
      nome_imagem = salvar_imagem(form_edit_perfil.foto_perfil.data)
      current_user.foto_perfil = nome_imagem
    current_user.cursos = atualizar_len(form_edit_perfil)
    db.session.commit()
    flash('Perfil atualizado com sucesso!', 'alert-success')
    return redirect(url_for('perfil'))
  elif request.method == 'GET':
    form_edit_perfil.username.data = current_user.username
    form_edit_perfil.email.data = current_user.email
  foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
  return render_template('editarperfil.html', foto_perfil=foto_perfil, form_edit_perfil=form_edit_perfil)



@app.route('/post')
def post():
  posts = Post.query.all()
  return render_template('post.html', posts=posts)

@app.route('/post/criar', methods=['GET','POST'])
@login_required
def criar_post():
  form_post = FormCriarPost()
  if form_post.validate_on_submit():
    post = Post(titulo=form_post.titulo.data, descricao=form_post.descricao.data, autor=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Post criado com Sucesso!', 'alert-success')
    return redirect(url_for('post'))
  return render_template('criarpost.html', form_post=form_post)

