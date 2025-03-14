from flask import Flask, request, send_file, jsonify
import datetime
import os
import requests

app = Flask(__name__)

# Función para obtener la ubicación usando la IP
def get_location_by_ip(ip):
    try:
        # Usamos el servicio ipinfo.io para obtener la ubicación basada en la IP
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        data = response.json()

        # Extraemos la ubicación (ciudad, región y país)
        location = data.get('city', 'Desconocida') + ', ' + data.get('region', 'Desconocida') + ', ' + data.get('country', 'Desconocido')
        return location
    except Exception as e:
        return f"Error al obtener ubicación: {str(e)}"

# Ruta principal
@app.route('/')
def capture_ip():
    # Obtener la IP del cliente
    client_ip = request.remote_addr

    # Obtener detalles del agente de usuario (User-Agent)
    user_agent = request.headers.get('User-Agent')

    # Obtener la fecha y hora actual
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Obtener la ubicación de la IP
    location = get_location_by_ip(client_ip)

    # Formatear los datos a guardar
    log_entry = f"{timestamp} - IP: {client_ip} - Ubicación: {location} - User-Agent: {user_agent}\n"

    # Especificar la ruta completa donde guardar el archivo
    log_file_path = 'ips_capturadas.txt'

    # Guardar en el archivo de texto
    try:
        with open(log_file_path, 'a') as file:
            file.write(log_entry)
    except Exception as e:
        return jsonify({"message": f"Error al guardar la información: {str(e)}"})

    return "Información capturada y guardada exitosamente."

# Ruta para descargar el archivo con las IPs capturadas
@app.route('/download')
def download_file():
    log_file_path = 'ips_capturadas.txt'
    
    # Verifica si el archivo existe y luego permite la descarga
    if os.path.exists(log_file_path):
        return send_file(log_file_path, as_attachment=True)
    else:
        return "Archivo no encontrado."

if __name__ == '__main__':
    app.run(debug=True)
