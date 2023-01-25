from flask import Flask

app = Flask(__name__)

def rota_customizada():
    return "<h1>Página de contato</h1>"   

#É uma forma de criar rotas sem o @app.route("/teste"). Dos parâmetros: (URL, endpoint, view function)    
app.add_url_rule("/contato","teste", rota_customizada)

if __name__ == '__main__':
    app.run(debug=True)