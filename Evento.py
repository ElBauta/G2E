# buscar dataclasses
from datetime import datetime, date

class Evento:

    def __init__(self, nombre, fecha, hora, ubicacion, categoria, descripcion = ""):

        self.nombre = nombre 
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion 
        self.descripcion = descripcion
        self.categoria = categoria

    def __str__(self):
        texto = (f"Evento: {self.nombre}\n"
                 f"Fecha: {self.fecha}\n"
                 f"Hora: {self.hora}\n"
                 f"Ubicacion: {self.ubicacion}\n")

        if self.descripcion != "":
            texto += f"Descripcion: {self.descripcion}\n"

        texto += f"Categoria: {self.categoria}"

        return texto

    def to_dict(self):
        return{
            "nombre" : self.nombre,
            "fecha" : self.fecha.strftime("%d/%m/%Y"),
            "hora" : self.hora,
            "ubicacion" : self.ubicacion,
            "descripcion" : self.descripcion,
            "categoria" : self.categoria
        }
    @staticmethod
    def from_dict(d):
        fecha = datetime.strptime(d["fecha"], "%d/%m/%Y").date()
        return Evento(d["nombre"], fecha, d["hora"], d["ubicacion"], d["categoria"], d["descripcion"])