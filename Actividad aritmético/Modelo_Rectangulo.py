class modelo_rectangulo:
    def __init__(self):
        self.longitud = None
        self.ancho = None
        self.area = None

    def get_longitud(self):
        return self.longitud
  
    def get_ancho(self):
        return self.ancho
  
    def get_area(self):
        return self.area
  
    def set_longitud(self, datolongitud):
        self.longitud = datolongitud

    def set_ancho(self, datoancho):
        self.ancho = datoancho

    def set_area(self, datoarea):
        self.area = datoarea

    def imprimir_datos(self):
        aux = "El área del rectángulo es: " + str(self.get_area())
        return aux