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