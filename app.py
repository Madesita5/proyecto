from flask import Flask, request
import datetime
import os

app = Flask(__name__)

# Define the path where you want to store the file
file_path = os.path.join(os.path.expanduser("~"), "ips_capturadas.txt")  # Guardará en tu directorio de usuario

@app.route('/')
def capture_ip():
    # Obtener la IP del cliente
    client_ip = request.remote_addr

    # Obtener detalles del agente de usuario (User-Agent)
    user_agent = request.headers.get('User-Agent')

    # Obtener la fecha y hora actual
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Formatear los datos a guardar
    log_entry = f"{timestamp} - IP: {client_ip} - User-Agent: {user_agent}\n"

    # Guardar en el archivo de texto en la ruta especificada
    with open(file_path, 'a') as file:
        file.write(log_entry)

    return "Información guardada con éxito."

if __name__ == '__main__':
    app.run(debug=True)
