class modelo_triangulo:
    def __init__(self):
        self.altura = None
        self.base = None
        self.area = None

    def get_altura(self):
        return self.altura

    def get_base(self):
        return self.base

    def get_area(self):
        return self.area

    def set_altura(self, datoaltura):
        self.altura = datoaltura

    def set_base(self, datobase):
        self.base = datobase

    def set_area(self, datoarea):
        self.area = datoarea

    def guardarDatos(self, datos):
        self.set_base(datos[0])
        self.set_altura(datos[1])
        self.set_area(datos[2])

    def imprimirDatos(self):
        aux = "El área del triángulo es: " + str(self.get_area())
        return aux