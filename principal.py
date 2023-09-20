from datetime import date
from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="",
    database="consultorio1"
)
cursor = conexion.cursor()

def calcularEdad(fecha):
    aa = int(fecha[0,4])
    mm = int(fecha[5,7])
    dd = int(fecha[8,10])
    hoy = date()
    dh = hoy.day()
    mh = hoy.month()
    ah = hoy.year()
    edad = ah-aa
    return edad

def calcularIMC(esta,peso):
    imc = peso/(esta**2)
    return imc

@app.route("/pacientes")
def pacientes():
    sql="SELECT * FROM pacientes"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    conexion.commit()
    for paciente in resultado:
        paciente.append(calcularEdad(paciente[2]))
        paciente.append(calcularIMC(paciente[3],paciente[4]))
    # Aquí vendrá el backend de consulta
    # de los pacientes (resultado)

    return render_template("pacientes.html, res=resultado")
# En res, le llegará al template un array donde cada fila
# sera un paciente y tendrá 8 columnas con la siguiente 
# información: documento, nombre, nacimiento, estatura,
# peso, tiposangre, edad, imc

if __name__=="__main__":
    app.run(host="0.0.0.0", port="9000", debug=True)
