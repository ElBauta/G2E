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

def eliminar_evento(l1):
    adel = input("nombre del evento que deseas eliminar: ")

    for e in l1:
        if e.nombre == adel:
            l1.remove(e)
            print ("Evento eliminado")
            return

    print("No se encontro ningun evento con ese nombre")

def edit_event(l2):

    pice = input("que evento quieres editar?: ")
    picu = input("que quieres editar del evento?: nombre, fecha, hora, ubicacion, categoria, descripcion: ")
    
    for a in l2:
        if pice == a.nombre:
            pici = input("nuevo valor: ")
            setattr(a, picu, pici)
            print("Evento actualizado")
            return
    print ("ese evento no existe")

def list_event(l3):
    if not l3:
        print ("No hay elementos en la lsita")
        return
    for i in l3:
        print (i)
        print ("-" * 30)   