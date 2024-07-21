class modelo_paralelogramo:
    def __init__(self):
        self.base = None
        self.altura = None
        self.area = None
        
    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def get_area(self):
        return self.area
    
    def set_base(self, datobase):
        self.base = datobase

    def set_altura(self,datoaltura):
        self.altura = datoaltura

    def set_area(self,datoarea):
        self.area = datoarea
        
    def imprimir_datos(self):
        aux = "El area del paralelogramo es " + str(self.get_area())
        return aux