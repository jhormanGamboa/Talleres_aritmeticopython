class modelo_cantidad:
    def __init__(self):
        self.cantidad = None
        self.interez = None
        
    def get_cantidad(self):
        return self.cantidad

    def get_interez(self):
        return self.interez
    
    def set_cantidad(self, datocantidad):
        self.cantidad = datocantidad

    def set_interez(self,datointerez):
        self.interez = datointerez
        
    def imprimir_datos(self):
        aux = "El interez es del 5% sonbre la cantidad: " + str(self.get_interez())
        return aux