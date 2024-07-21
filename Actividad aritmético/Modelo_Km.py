class modelo_kilometro:
    def __init__(self):
        self.kilometro = None
        self.milla = None
        
    def get_kilometro(self):
        return self.kilometro

    def get_milla(self):
        return self.milla
    
    def set_kilometro(self, datokilometro):
        self.kilometro = datokilometro

    def set_milla(self,datomilla):
        self.milla= datomilla
        
    def imprimir_datos(self):
        aux = "Kilómetros a millas son: " + str(self.get_milla())
        return aux