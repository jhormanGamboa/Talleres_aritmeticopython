class modelo_circuloR:
    def __init__(self):
        self.radio = None
        self.area = None
        
    def get_radio(self):
        return self.radio
    
    def get_area(self):
        return self.area
    
    def set_radio(self,datoradio):
        self.radio = datoradio
        
    def set_area(self,datoarea):
        self.area = datoarea
        
    def imprimir_datos(self):
        aux = "el area del circulo es:" +str (self.get_area())
        return aux