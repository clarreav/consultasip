import ipinfo
import time
import asyncio


# Metodo para la consulta de informacion sobre una IP.
def consultaip(token, ip):
    # Inicializacion del handler
    handler = ipinfo.getHandler(token)
    # Obtencion de los datos de la IP
    details = handler.getDetails(ip)
    # Conversion del objeto Detalles a diccionario
    diccionario = dict(details.all)
    return diccionario, time.perf_counter()

# Metodo para consulta paralela de IPs por forma de batch
def consultabatch(token, ips):
    # Inicializacion del handler
    handler = ipinfo.getHandler(token)
    # Obtencion de los datos del diccionario de las IPs
    batch = handler.getBatchDetails(ips).values()
    return batch, time.perf_counter()


def main():
    print("###Consultas de IP con ipinfo API###", end="\n")
    # Token de acceso para el API
    access_token = 'ACCESS_TOKEN'
    # Lista de ips de prueba
    ip_address = ['216.239.36.21', '1.1.1.1', '8.8.8.8', '4.4.4.4']
    # Almacenamiento de los diccionarios con la informacion de cada ip para la lectura secuencial
    listadetalle = []
    # Tiempo de ejecucion de la consulta secuencial
    tiemposec = 0
    # lectura de cada ip de la lista de prueba para la consulta con el modulo ipinfo
    for ip in ip_address:
        diccionario, tiempo = consultaip(access_token, ip)
        listadetalle.append(diccionario)
        tiemposec += tiempo
    # Consulta paralela por medio de batch de ips
    diccionario1, tiempo = consultabatch(access_token, ip_address)

    # Parseo de la data
    print("Consula Secuencial", end="\n")
    for detalle in listadetalle:
        for k, v in detalle.items():
            print(k, v)
        print("\n")
    print("Consulta Paralela", end="\n")
    for detalle in diccionario1:
        for k, v in detalle.items():
            print(k, v)
        print("\n")
    print("El tiempo de la consulta secuencial es: ", tiemposec)
    print("El tiempo de la consulta batch es: ", tiempo)


if __name__ == "__main__":
    main()
