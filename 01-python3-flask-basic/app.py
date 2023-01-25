from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crud')
def crud():
    return render_template('crud.html')

if __name__ == '__main__':
    app.run(debug=True)