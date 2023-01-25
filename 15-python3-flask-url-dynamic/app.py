from flask import Flask

app = Flask(__name__)

#Cria uma rota simples
@app.route("/hello/")
#Cria uma rota simples com uma ID (digite qualquer coisa)
@app.route("/hello/<nome>")
#O parâmetro da função deve ser a ID
def hello(nome):
    #O resultado é mostrado nas chaves
    return "<h1>Hello {}</h1>".format(nome)
 
@app.route("/blog/")
#Precisa informar no parâmetro o tipo do dado, ex: <float:postID>
@app.route("/blog/<int:postID>")
def blog(postID=-1):
    if postID >= 0:
        return "Mostrando notícia, código: {}".format(postID)
    else:
        return "Mostrando todas as notícias!"

if __name__ == '__main__':
    app.run(debug=True)
