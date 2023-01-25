from flask import Flask
from controllers import routes
from models.database import db
import os

app = Flask(__name__, template_folder='views')
routes.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'models/estudantes.sqlite3')
    
if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)  
    