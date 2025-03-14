from flask import Flask, request, send_file
import datetime
import os

app = Flask(__name__)

@app.route('/')
def capture_ip():
    # Obtener la IP del cliente, considerando si hay un proxy
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Obtener detalles del agente de usuario (User-Agent)
    user_agent = request.headers.get('User-Agent')

    # Obtener la fecha y hora actual
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Formatear los datos a guardar
    log_entry = f"{timestamp} - IP: {client_ip} - User-Agent: {user_agent}\n"

    # Especificar la ruta completa donde guardar el archivo
    log_file_path = 'ips_capturadas.txt'

    # Guardar en el archivo de texto
    try:
        with open(log_file_path, 'a') as file:
            file.write(log_entry)
    except Exception as e:
        return f"Error al guardar el archivo: {str(e)}"

    return "Información guardada exitosamente en ips_capturadas.txt"

@app.route('/download')
def download_file():
    log_file_path = 'ips_capturadas.txt'
    
    # Verifica si el archivo existe y luego permite la descarga
    if os.path.exists(log_file_path):
        return send_file(log_file_path, as_attachment=True)
    else:
        return "Archivo no encontrado."

@app.route('/count')
def count_requests():
    log_file_path = 'ips_capturadas.txt'
    
    # Contar el número de registros en el archivo
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
            request_count = len(lines)
    except FileNotFoundError:
        return "El archivo no existe aún."

    return f"El número total de solicitudes es: {request_count}"

if __n
