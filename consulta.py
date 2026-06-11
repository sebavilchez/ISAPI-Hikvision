import requests
from requests.auth import HTTPDigestAuth

DVR_IP = "192.168.0.212"
USER = "admin"
PASS = "Admin@23646"
TIMEOUT = 5


def obtener_informacion_dispositivo(ip, usuario, clave):
    url = f"http://{ip}/ISAPI/ContentMgmt/Storage/hdd"
    auth = HTTPDigestAuth(usuario, clave)

    try:
        respuesta = requests.get(url, auth=auth, timeout=TIMEOUT)

        if respuesta.status_code == 200:
            return respuesta.text
        else:
            return f"Error: {respuesta.status_code}\n{respuesta.text}"

    except requests.exceptions.RequestException as e:
        return f"Error de red: {e}"


if __name__ == "__main__":
    resultado = obtener_informacion_dispositivo(DVR_IP, USER, PASS)
    print(resultado)
