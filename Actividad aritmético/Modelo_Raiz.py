class modelo_raiz:
    def __init__(self):
        self.num1 = None
        self.total = None
        
    def get_numero1(self):
        return self.num1

    def get_total(self):
        return self.total
    
    def set_numero1(self, datonumero1):
        self.num1 = datonumero1


    def set_total(self,datototal):
        self.total = datototal
        
    def imprimir_datos(self):
        aux = "La raíz del número es: " + str(self.get_total())
        return aux