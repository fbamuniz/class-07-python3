from flask import render_template

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html',**locals())

    @app.route('/crud')
    def crud():
        return render_template('crud.html')