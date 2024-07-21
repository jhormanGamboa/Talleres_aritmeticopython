class modelo_gradoC:
    def __init__(self):
        self.celisius = None
        self.fahrentheit = None
        
    def get_celsius(self):
        return self.celisius
    
    def get_fahrentheit(self):
        return self.fahrentheit
    
    def set_celsius(self, datocelcius):
        self.celisius = datocelcius
        
    def set_fahrentheit(self, datofarentheit):
        self.fahrentheit = datofarentheit
        
    def imprimir_datos(self):
        aux = "los grados Celsius a fahrentheit son: " + str(self.get_fahrentheit())
        return aux