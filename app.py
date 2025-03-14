from flask import Flask, request, redirect, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def portal():
    ip_cliente = request.remote_addr
    mac_cliente = request.headers.get('X-Forwarded-For', 'MAC_DESCONOCIDA')
    user_agent = request.headers.get('User-Agent')

    # Obtener ubicación aproximada con una API de geolocalización
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_cliente}')
        geo_data = response.json()
        location = {
            "country": geo_data.get("country"),
            "city": geo_data.get("city"),
            "lat": geo_data.get("lat"),
            "lon": geo_data.get("lon")
        }
    except:
        location = {"error": "No se pudo obtener la ubicación"}

    # Guardar en archivo
    with open("ips_capturadas.txt", "a") as f:
        f.write(f"IP: {ip_cliente} | MAC: {mac_cliente} | Navegador: {user_agent} | Ubicación: {location}\n")

    return jsonify({
        "ip": ip_cliente,
        "mac": mac_cliente,
        "navegador": user_agent,
        "ubicacion": location
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
