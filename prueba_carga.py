import threading
import time
import urllib.request


def prueba_carga(total=100):
    url = "http://localhost:8000/api/albumes/"
    tiempos, errores = [], []

    def pedir():
        t = time.time()
        try:
            with urllib.request.urlopen(url, timeout=10) as respuesta:
                respuesta.read()
            tiempos.append(time.time() - t)
        except OSError as e:
            errores.append(str(e))

    inicio = time.time()
    hilos = [threading.Thread(target=pedir) for _ in range(total)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    total_t = time.time() - inicio
    print(f"Peticiones: {total} | Exitosas: {len(tiempos)} | Errores: {len(errores)}")
    if tiempos:
        print(f"Tiempo promedio: {sum(tiempos)/len(tiempos)*1000:.0f} ms")
        print(f"Tiempo máximo:   {max(tiempos)*1000:.0f} ms")
    print(f"Duración total:  {total_t:.2f} s")
