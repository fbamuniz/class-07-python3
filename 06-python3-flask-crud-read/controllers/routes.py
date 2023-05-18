from flask import render_template, request, url_for, redirect
from models.database import db, Estudante

def init_app(app):
    @app.route('/')
    def index():
        # Armazena em "estudantes" todos os valores, como em um SELECT e encaminha para index.html
        estudantes = Estudante.query.all()
        return render_template('index.html', estudantes=estudantes)