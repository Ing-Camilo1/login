from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.static_folder = 'sources/static'

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='$uP3rS3cr3tP@ssw0rd!',
        database='user_management'
    )

@app.route('/')
def index():
    # Si el usuario está logueado, redirigir a la página principal
    if 'user_id' in session:
        return redirect(url_for('principal'))
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    full_name = data.get('nombre')
    email = data.get('email')
    password = data.get('password')
    
    if not full_name or not email or not password:
        return jsonify({'success': False, 'message': 'Faltan datos'})

    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = "INSERT INTO Usuarios (nombre_completo, correo_electronico, contrasena) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (full_name, email, password))
        cnx.commit()
        return jsonify({'success': True, 'message': 'Registro exitoso'})
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'success': False, 'message': 'Error en la base de datos'})
    finally:
        cursor.close()
        cnx.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Faltan datos'})

    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = "SELECT id, nombre_completo, correo_electronico, contrasena FROM Usuarios WHERE correo_electronico = %s AND contrasena = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    cnx.close()

    if user:
        # Guardar el ID del usuario en la sesión
        session['user_id'] = user[0]
        return jsonify({'success': True, 'redirect': '/principal'})
    else:
        return jsonify({'success': False, 'message': 'Credenciales inválidas'})

@app.route('/recover', methods=['POST'])
def recover():
    data = request.form
    full_name = data.get('nombre')
    email = data.get('email')
    password = data.get('password')

    if not full_name or not email or not password:
        return jsonify({'success': False, 'message': 'Faltan datos'})

    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = "UPDATE Usuarios SET contrasena = %s WHERE correo_electronico = %s AND nombre_completo = %s"
    try:
        cursor.execute(query, (password, email, full_name))
        cnx.commit()
        return jsonify({'success': True, 'message': 'Contraseña restablecida'})
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'success': False, 'message': 'Error en la base de datos'})
    finally:
        cursor.close()
        cnx.close()

@app.route('/principal')
def principal():
    # Asegurarse de que el usuario esté logueado
    if 'user_id' not in session:
        return redirect(url_for('index'))

    cnx = get_db_connection()
    cursor = cnx.cursor()

    query = "SELECT nombre_completo, correo_electronico, contrasena FROM Usuarios WHERE id = %s"
    cursor.execute(query, (session['user_id'],))
    user = cursor.fetchone()
    cnx.close()

    if user:
        return render_template('principal.html', usuario={
            'nombre': user[0],
            'correo': user[1],
            'password': user[2]
        })
    else:
        return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    # Eliminar el ID del usuario de la sesión
    session.pop('user_id', None)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
