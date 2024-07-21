class modelo_promedio:
    def __init__(self):
        self.num1 = None
        self.num2= None
        self.promedio = None
        
    def get_numero1(self):
        return self.num1

    def get_numero2(self):
        return self.num2

    def get_promedio(self):
        return self.promedio
    
    def set_numero1(self, datonumero1):
        self.num1 = datonumero1

    def set_numero2(self,datonumero2):
        self.num2 = datonumero2

    def set_promedio(self,datopromedio):
        self.promedio = datopromedio
        
    def imprimir_datos(self):
        aux = "El promedio de los numeros es: " + str(self.get_promedio())
        return aux