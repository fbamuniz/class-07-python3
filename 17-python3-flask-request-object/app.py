from flask import Flask, request
import json

#No browser, digite: http://127.0.0.1:5000/?nome=Teste&idade=10

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    #print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    #return json.dumps(request.args)
    #return json.dumps([t1, t2])
    return json.dumps([t1['idade'], t2['nome']])

if __name__ == '__main__':
    app.run(debug=True)