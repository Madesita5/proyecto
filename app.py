from flask import Flask, request
import datetime

# Inicializa la aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<html><body><h1>Haz clic en el enlace para registrar tu información</h1>
              <a href="/log">Haz clic aquí</a></body></html>'''

@app.route('/log')
def log():
    # Obtener la IP del visitante, considerando la cabecera X-Forwarded-For si está presente
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now()

    # Especifica la ruta donde guardar el archivo
    archivo = 'C:/Users/Madel/app/ips_capturadas.txt'  # Usando barras inclinadas para evitar problemas

    # Escribir la información en el archivo de texto
    with open(archivo, 'a') as file:
        # Aquí es donde debía estar la indentación
        file.write(f'{timestamp} - IP: {user_ip}, User-Agent: {user_agent}\n')

    return f'<h1>Información registrada:</h1><p>Tu IP y agente de usuario han sido registrados.</p>'

# Esta línea es importante para que Flask reconozca el archivo como la aplicación
if __name__ == '__main__':
    app.run(debug=True)
