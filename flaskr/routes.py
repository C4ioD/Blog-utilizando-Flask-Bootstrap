
from flaskr import app
from flaskr.forms import Formlogin, FormCriarConta
from flask import render_template, url_for, request

lista_usuarios = ['caio','jamila','luiz']

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login():
  form_login= Formlogin()
  form_criar_conta = FormCriarConta()
  return render_template("login.html" , form_login=form_login, form_criar_conta=form_criar_conta)

@app.route("/contatos")
def contatos():
  return render_template("contatos.html")

@app.route("/usuarios")
def usuarios():
  usuarios = lista_usuarios
  return render_template("usuarios.html", usuarios=usuarios) 

