import requests
import time

def medir_velocidad_internet(duracion_minutos):
    url = "http://ipv4.download.thinkbroadband.com/200MB.zip"  # URL de un archivo para descargar y subir
    duracion_segundos = duracion_minutos * 60

    # Desactivar la verificación del certificado SSL
    requests.packages.urllib3.disable_warnings()

    # Medir velocidad de bajada
    start_time = time.time()
    total_bytes_bajada = 0
    while time.time() - start_time < duracion_segundos:
        response = requests.get(url, verify=False)
        total_bytes_bajada += len(response.content)
        porcentaje_avance = (time.time() - start_time) / duracion_segundos * 100
        print(f"Avance de la prueba velocidad de bajada: {porcentaje_avance:.2f}%")
    end_time = time.time()
    download_speed = total_bytes_bajada / (end_time - start_time) / 10**6  # Convertir a Mbps
    print(f"Velocidad de bajada: {download_speed:.2f} Mbps")

    # Medir velocidad de subida
    # start_time = time.time()
    # total_bytes_subida = 0
    # while time.time() - start_time < duracion_segundos:
    #     response = requests.post(url, data=response.content, verify=False)
    #     total_bytes_subida += len(response.content)
    #     porcentaje_avance = (time.time() - start_time) / duracion_segundos * 100
    #     print(f"Avance de la prueba velocidad de subida: {porcentaje_avance:.2f}%")
    # end_time = time.time()
    # upload_speed = total_bytes_subida / (end_time - start_time) / 10**6  # Convertir a Mbps
    # print(f"Velocidad de subida: {upload_speed:.2f} Mbps")

    # Medir latencia
    start_time = time.time()
    response = requests.head(url, verify=False)
    end_time = time.time()
    latency = (end_time - start_time) * 1000  # Convertir a milisegundos
    print(f"Latencia: {latency:.2f} ms")

medir_velocidad_internet(2)  # Duración de la prueba en minutos (por ejemplo, 5 minutos)
