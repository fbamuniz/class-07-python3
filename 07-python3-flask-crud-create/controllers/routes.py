from flask import render_template, request, url_for, redirect
from models.database import db, Estudante

def init_app(app):
    @app.route('/')
    def index():
        estudantes = Estudante.query.all()
        return render_template('index.html', estudantes=estudantes)

    # O GET é usado para abrir a página add.html e o POST para salvar os dados
    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            estudante = Estudante(request.form['nome'], request.form['idade'])
            db.session.add(estudante)
            db.session.commit()
            return redirect(url_for('index'))
        # Necessário para abrir a página de cadastro
        return render_template('add.html')