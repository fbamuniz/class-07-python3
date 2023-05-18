from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username']=='admin' and request.form['password'] == 'admin':
            return redirect(url_for('sucesso'),code=200) #redirecionamento manual 
            #return redirect(url_for('sucesso'),code=302) #redirecionamento automático               
        else:
            abort(401) #não autorizado     
    else:
        abort(403) #proibe o GET, clicando direto na URL e dando ENTER

@app.route('/sucesso')
def sucesso():
    return 'sucesso'

if __name__ == '__main__':
    app.run(debug=True)