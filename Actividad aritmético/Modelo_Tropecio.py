class modelo_trapecio:
    def __init__(self):
        self.baseMayor = None
        self.baseMenor = None
        self.altura = None
        self.area = None
        
    def get_baseMayor(self):
        return self.baseMayor

    def get_baseMenor(self):
        return self.baseMenor
    
    def get_altura(self):
        return self.altura
    
    def get_area(self):
        return self.area
    
    def set_baseMayor(self, baseMayor):
        self.baseMayor = baseMayor

    def set_baseMenor(self, baseMenor):
        self.baseMenor = baseMenor
        
    def set_altura(self, altura):
        self.altura = altura
    
    def set_area(self, area):
        self.area = area
        
    def imprimir_datos(self):
        return f"Área del trapecio: {self.get_area()}"