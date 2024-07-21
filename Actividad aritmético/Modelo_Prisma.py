class modelo_prisma:
    def __init__(self):
        self.base = None
        self.altura = None
        
    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura
    
    def set_base(self, datobase):
        self.base = datobase

    def set_altura(self,datoaltura):
        self.altura = datoaltura

class datos(modelo_prisma):
    def __init__(self):
        super().__init__()
        self.ancho = None
        self.volumen = None

    def get_ancho(self):
        return self.ancho

    def get_volumen(self):
        return self.volumen

    def set_ancho(self,datoancho):
        self.ancho = datoancho

    def set_volumen(self,datovolumen):
        self.volumen = datovolumen
        
    def imprimir_datos(self):
        aux = "El volumen del prisma es: " + str(self.get_volumen())
        return aux