from flask import render_template

def init_app(app):
    @app.route('/')
    def index():
        nome = "Fred"
        sobrenome = "Barbosa"
        return render_template('index.html', 
                               pNome=nome, 
                               pSobrenome=sobrenome
                               )

    @app.route('/crud')
    def crud():
        return render_template('crud.html')