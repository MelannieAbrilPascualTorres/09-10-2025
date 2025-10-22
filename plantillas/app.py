from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_muy_secreta_muy_larga_y_dificil_de_adivinar'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/registro')
def crear_cuenta():
    return render_template('registro.html')

@app.route('/registrando')
def registrando():
    return ""
@app.route('/registrame', methods = ("GET", "POST"))
def registrame():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        genero = request.form['genero']
        cuenta = request.form['cuenta']
        contra = request.form['contra']
        confirmar = request.form['confirmar']

        error = None
        if contra != confirmar:
            error = "La contraseña no coincide"

        if error != None:
            flash(error)
            return render_template('registro.html')
        else:
            flash(f"¡Registro exitoso para el usuario: {nombre} {apellido}!")
            return render_template('index.html')
    

@app.route('/sesion')
def iniciar_sesion():
    return render_template('sesion.html')

if __name__=='__main__':
    app.run(debug=True)
