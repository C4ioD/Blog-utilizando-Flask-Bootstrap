
from app_blog import app, db
from app_blog.forms import Formlogin, FormCriarConta
from app_blog.models import Usuario, Post
from flask import render_template, url_for, request, redirect , flash
import email_validator

lista_usuarios = ['caio','jamila','luiz']

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login():
  form_login= Formlogin()
  if form_login.validate_on_submit():
    flash ( f'Login realizado com sucesso no e-mail: {form_login.email.data}', 'alert-success' )
    return redirect(url_for('home'))

  return render_template("login.html" , form_login=form_login)

@app.route('/criarconta' , methods=['GET','POST'])
def criar_conta():
  form_criar_conta = FormCriarConta()
  if form_criar_conta.validate_on_submit():
    usuario = Usuario(username=form_criar_conta.username.data, email=form_criar_conta.email.data, senha=form_criar_conta.senha.data)
    db.session.add(usuario)
    db.session.commit()
    flash(f'Conta criada com sucesso no e-mail: {form_criar_conta.email.data}', 'alert-success')
    return redirect(url_for('home'))
  return render_template('criarconta.html', form_criar_conta = form_criar_conta)

@app.route("/contatos")
def contatos():
  return render_template("contatos.html")

@app.route("/usuarios")
def usuarios():
  usuarios = lista_usuarios
  return render_template("usuarios.html", usuarios=usuarios) 

