from flask import Flask

app = Flask(__name__)


@app.route("/home")
def hello_world():
    return "<h1>Hello World</h1>"


@app.route("/login")
def hello_login():
    return "<h1>Essa seria a pagina de login acessado pela url</h1>"


@app.route("/check out")
def hello_check():
    return "<h1>Essa seria a pagina de checkout acessado pela url</h1>"
