class modelo_piramide:
    def __init__(self):
        self.longitudbase = None
        self.volumen = None
        
    def get_longitudbase(self):
        return self.longitudbase

    def get_volumen(self):
        return self.volumen
    
    def set_longitudbase(self, datolongitud):
        self.longitudbase = datolongitud

    def set_volumen(self,volumen):
        self.volumen = volumen



class Datos(modelo_piramide):
    def __init__(self):
        super().__init__()
        self.anchobase = None
        self.altura = None

    def get_anchobase(self):
        return self.anchobase

    def get_altura(self):
        return self.altura

    def set_anchobase(self,datoancho):
        self.anchobase = datoancho

    def set_altura(self,datoaltura):
        self.altura = datoaltura
        
    def imprimir_datos(self):
        aux = "El volumen de la piramide es: " + str(self.get_volumen())
        return aux