from flask import render_template, request, url_for, redirect
from models.database import db, Estudante

def init_app(app):
    @app.route('/')
    def index():
        estudantes = Estudante.query.all()
        return render_template('index.html', estudantes=estudantes)


    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            estudante = Estudante(request.form['nome'], request.form['idade'])
            db.session.add(estudante)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add.html')


    @app.route('/edit/<int:id>', methods=['GET','POST'])
    def edit(id):
        estudante =  Estudante.query.get(id)
        if request.method == 'POST':
            estudante.nome = request.form['nome']
            estudante.idade = request.form['idade']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit.html',estudante=estudante)


    @app.route('/delete/<int:id>')
    def delete(id):
        estudante = Estudante.query.get(id)
        db.session.delete(estudante)
        db.session.commit()
        return redirect(url_for('index'))