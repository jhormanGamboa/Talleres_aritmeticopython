class modelo_hora:
    def __init__(self):
        self.minuto = None
        self.hora = None
        
    def get_hora(self):
        return self.hora

    def get_minuto(self):
        return self.minuto
    
    def set_hora(self, datohora):
        self.hora = datohora


    def set_minuto(self,datominuto):
        self.minuto = datominuto
        
    def imprimir_datos(self):
        aux = "De hora a minuto es: " + str(self.get_minuto())
        return aux