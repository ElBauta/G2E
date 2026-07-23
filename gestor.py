import evento
from datetime import datetime, date

def crear_evento():
    nombre = input("introduzca nombre del evento: ")

    fecha = None
    
    while fecha == None:

        fecha_texto = input("Que dia sera (DD/MM/AAAA)?: ")
        
        try:
            fecha_intento = datetime.strptime(fecha_texto, "%d/%m/%Y").date()
            if fecha_intento < date.today():
                print("no puedes crear un evento en el pasado")
            else:
                fecha = fecha_intento
        except ValueError:
            print("formato de fecha invalido")

    hora = input("Hora del evento: ")
    ubicacion = input("donde tendra lugar?: ")
    descripcion = input("quiere intoducir una descripcion?: ")
    categoria = input("categoria del evento: ")

    event = evento.Evento(nombre, fecha, hora, ubicacion, categoria, descripcion)
    return event