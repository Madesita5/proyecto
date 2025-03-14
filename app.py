from flask import Flask, request, redirect, render_template_string
import requests

app = Flask(__name__)

# Función para obtener IP pública y ubicación
def obtener_ip_y_ubicacion():
    ip_publica = requests.get('https://api.ipify.org').text
    # Usamos ipinfo.io para obtener la ubicación
    respuesta = requests.get(f'https://ipinfo.io/{ip_publica}/json')
    data = respuesta.json()
    return ip_publica, data.get('city', 'Desconocida'), data.get('region', 'Desconocida'), data.get('country', 'Desconocido')

# Página principal
@app.route('/')
def inicio():
    return render_template_string("""
        <h1>Bienvenido al portal de inicio de sesión de Gmail</h1>
        <p>Haz clic en el siguiente enlace para proceder:</p>
        <a href="/capturar_datos">Ir al inicio de sesión de Gmail</a>
    """)

# Ruta que captura la IP pública, ubicación y otros datos
@app.route('/capturar_datos')
def capturar_datos():
    ip, ciudad, region, pais = obtener_ip_y_ubicacion()
    # Simulamos la redirección a una página legítima
    return render_template_string(f"""
        <h1>Iniciando sesión...</h1>
        <p>Tu IP pública es: {ip}</p>
        <p>Ubicación: {ciudad}, {region}, {pais}</p>
        <p>Gracias por visitar el portal.</p>
    """)

# Redirigir a una URL más creíble
@app.route('/inicio_sesion')
def redirigir():
    return redirect("https://accounts.google.com/ServiceLogin")

if __name__ == '__main__':
    app.run(debug=True)
