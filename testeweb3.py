from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def ola():
    return render_template("index2.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        registro = user + " - " + senha + ' \n'

        print (registro)

        arquivo = open("registros.txt","r")
        lista = arquivo.readlines()

        #quero ver se registro está na lista
        print (lista)

        if (registro in lista):
            return "<h1>Login efetuado com sucesso</h1> <meta http-equiv='Refresh' content= '2; url=/Materias'/>"
           
        else:
            return "<h1>Login Mal sucedido</h1> <meta http-equiv='Refresh' content= '2; url=/'/>"
        
        return "<h1>Login efetuado com sucesso</h1>"
    
    return "<h1> Teste </h1>"

@app.route("/Materias", methods = ["POST", "GET"])
def Materias():
    Disciplina = ""
    if request.method  == "POST":
        Disciplina = request.form["fname"]

        Materias = Disciplina + ' \n'

        print (Materias)

        arquivo = open("Materia.txt","a")
        arquivo.writelines(Materias)

        return "<h1>Cadastro de materia realizado com sucesso!! agora joga ai mano tmj🤝 </h1> <meta http-equiv='Refresh' content= '2; url=https://games.cdn.famobi.com/html5games/b/bubble-tower-3d/v050/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=1385d98a-b5f2-4339-bce7-b99a8dd2e8b0&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=773&original_ref=https%3A%2F%2Fhtml5games.com%2FGame%2FBubble-Tower-3D%2F1385d98a-b5f2-4339-bce7-b99a8dd2e8b0'/>"

    return render_template('Materias.html')

@app.route("/cadastro")
def hello():
    return render_template('index3.html')

@app.route("/registro", methods = ["POST", "GET"])
def registro():
    user = ""
    senha = ""
    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        registro = user + " - " + senha + ' \n'
        
        print (registro)

        arquivo = open("registros.txt","a")
        arquivo.writelines(registro)

        return "<h1>Cadastro realizado com sucesso</h1> <meta http-equiv='Refresh' content= '1; url=http://127.0.0.1:5000'/>"

app.run()