#Métodos HTTP (GET, POST, PUT, DELETE, HEAD, PATCH) e outros
from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='public')

@app.route('/add',methods=["GET","POST"])
def add():
    #Serve para controlar as requisições
    if request.method == "POST":
        return dumps(request.form)
    return "Utilizado GET"

if __name__ == '__main__':
    app.run(debug=True)