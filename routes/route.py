from flask import render_template, request
from server import app
from database.db import *

@app.route("/home")
def home_page():
    connectionSQL()
    return render_template("home.html")
    
@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/consult", methods=["get"])
def consult_page():
    return render_template("consult.html")
    
@app.route("/register_user", methods=["post"])
def register_user():
    data_user = request.form
    print(request.form)
    id, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"]
    try:
        insert_user(id, name, lastname, birthday)
        return "Usuario creado exitosamente"
    except Exception as err:
        return f"Error al registrar nuevo usuario: {err}"
        
@app.route("/get_user", methods=["GET"])
def get_user():
    id = request.args.get('id')
    print(f"Id de consulta:", id)
    try:
        result = consult_user(id)
        print(f"Resultado:", result)
        return render_template('consult.html', result=result)  
    except Exception as err:
       return render_template('consult.html', error="No se encontró ningún usuario con el ID proporcionado.")
