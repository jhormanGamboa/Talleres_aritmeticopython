class modelo_parimpar:
    def __init__(self):
        self.num1 = None
        self.par_impar = None
        
    def get_numero1(self):
        return self.num1

    def get_par_impar(self):
        return self.par_impar
    
    def set_numero1(self, datonumero1):
        self.num1 = datonumero1

    def set_par_impar(self, datopar_impar):
        self.par_impar = datopar_impar
        
    def imprimir_datos(self):
        aux = f"El número {self.num1} es {self.par_impar}"
        return aux