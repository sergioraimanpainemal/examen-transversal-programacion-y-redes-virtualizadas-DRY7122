import sqlite3
import bcrypt
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = "examen_usuarios.db"

def init_db():
    """Crea la base de datos y la tabla si no existen, e inserta los integrantes oficiales."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    
    # Datos oficiales del equipo (jveas, sraiman, fmoya)
    integrantes = {
        "jveas": "jveas123",
        "sraiman": "sraiman123",
        "fmoya": "fmoya123"
    }
    
    for user, pwd in integrantes.items():
        # Generar el hash seguro usando bcrypt
        salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(pwd.encode('utf-8'), salt).decode('utf-8')
        try:
            cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", (user, pwd_hash))
        except sqlite3.IntegrityError:
            pass # Si el usuario ya existe en la BD, no lo duplica
            
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    """Ruta del sitio web para validar usuarios mediante peticiones POST."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM usuarios WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    
    if row and bcrypt.checkpw(password.encode('utf-8'), row[0].encode('utf-8')):
        return jsonify({"status": "success", "message": f"Usuario {username} verificado con exito."}), 200
    else:
        return jsonify({"status": "error", "message": "Credenciales invalidas."}), 401

if __name__ == '__main__':
    init_db()
    # Inicia el servidor web en el puerto solicitado 5800
    app.run(host='0.0.0.0', port=5800, debug=True)
