from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin():
    return "<h1>Bem-vindo, administrador!</h1>"

@app.route("/guest/<guest>")
def guest(guest):
    return "<hp>Bem-vindo, convidado de nome <b>%s</b>!</p>" %guest

#Envia para uma determinada URL, de acordo com o nome inserido
@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest=name))

if __name__ == '__main__':
    app.run(debug=True)