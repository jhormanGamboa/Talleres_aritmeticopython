from Modelo_Piramide import Datos
from Vista_Piramide import vista_piramide

class controlador_piramide:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_piramide = self.objvista.obtener_datos()
        longitud_base,ancho_base,altura = datos_piramide
        self.objmodelo.set_longitudbase(longitud_base)
        self.objmodelo.set_anchobase(ancho_base)
        self.objmodelo.set_altura(altura)
        self.calcular_volumen()
        
    def calcular_volumen(self):
        longitud_base = self.objmodelo.get_longitudbase()
        ancho_base = self.objmodelo.get_anchobase()
        altura = self.objmodelo.get_altura()
        volumen = (longitud_base * ancho_base * altura)
        self.objmodelo.set_volumen(volumen)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = Datos()
objvista = vista_piramide()
objcontrolador = controlador_piramide(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()