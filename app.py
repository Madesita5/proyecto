from flask import Flask, request
import datetime

app = Flask(__name__)

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

    # Especificar la ruta completa donde guardar el archivo
    log_file_path = r'C:\Users\Madel\ips_capturadas.txt'

    # Guardar en el archivo de texto
    with open(log_file_path, 'a') as file:
        file.write(log_entry)

    return "Información guardada con éxito."

if __name__ == '__main__':
    app.run(debug=True)
