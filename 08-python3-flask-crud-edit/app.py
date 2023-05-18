from flask import Flask
from controllers import routes
from models.database import db
import os

app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Permite let um determinado path
basedir = os.path.abspath(os.path.dirname(__file__))
# É o path do SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'models/estudantes.sqlite3')
    
if __name__ == '__main__':
    # Verifica no início da aplicação se o BD já existe. Caso contrário ele criará o BD.
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)  
    