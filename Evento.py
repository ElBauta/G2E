class Evento:

    def __init__(self, nombre, fecha, hora, ubicacion, descripcion, categoria):

        self.nombre = nombre 
        self.fecha = fecha
        self.hora = hora
        self.ubicacion = ubicacion 
        self.descripcion = descripcion
        self.categoria = categoria

    def __str__(self):

        return (f"Evento: {self.nombre}\n"
                f"Fecha: {self.fecha}\n"
                f"Hora: {self.hora}\n"
                f"Ubicacion: {self.ubicacion}\n"
                f"Descripcion: {self.descripcion}\n"
                f"Categoria: {self.categoria}")