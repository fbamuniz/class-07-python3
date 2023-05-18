from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Estudante" com os atributos: id, nome e idade. 
class Estudante(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade