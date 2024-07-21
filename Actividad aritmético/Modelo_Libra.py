class modelo_libra:
    def __init__(self):
        self.libra = None
        self.kilogramo= None
        
    def get_libra(self):
        return self.libra

    def get_kilogramo(self):
        return self.kilogramo
    
    def set_libra(self, datolibra):
        self.libra = datolibra

    def set_kilogramo(self,datokilogramo):
        self.kilogramo = datokilogramo
        
    def imprimir_datos(self):
        aux = "Las libras a kilogramos es: " + str(self.get_kilogramo())
        return aux