class Evento:

    def __init__(self, nombre, fecha, hora, ubicacion, descripcion, categoria):

        self.nombre = nombre 
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion 
        self.descripcion = descripcion
        self.categoria = categoria

    def __str__(self):

        return (f"{self.nombre}, es el {self.fecha}, a las {self.hora}, en {self.ubicacion}, esta es la descripcion adjunta {self.descripcion}, y la categoria {self.categoria}")