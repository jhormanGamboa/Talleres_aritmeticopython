from Modelo_Circulo import modelo_circuloR
from Vista_Circulo import vista_circuloR

class controlador_circulo:
    
    def __init__(self,objmodelo,objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_circulo = self.objvista.obtener_datos()
        self.objmodelo.set_ancho(datos_circulo[0])
        self.objmodelo.set_area(datos_circulo[1])
        self.calcular_area
        
    def calcular_area(self):
        radio = self.objmodelo.get_radio()
        area = self.objmodelo.get_radio()
        area = 3.14159265359 *(radio*radio)
        self.objmodelo.set_area(area)
        mensaje = self.objmodelo.imiprir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True
    
    objmodelo = modelo_circuloR()
    objvista = vista_circuloR()
    objcontrolador=controlador_circulo(objmodelo,objvista)
    objvista.crear_ventana()
    objvista.crear_boton()
    objvista.boton.config(command=objcontrolador.tomardatos)
    objvista.iniciar()