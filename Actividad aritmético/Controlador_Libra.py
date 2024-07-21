from Modelo_Libra import modelo_libra
from Vista_Libra import vista_libra

class controlador_libra:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_libra = self.objvista.obtener_datos()
        libra = datos_libra
        self.objmodelo.set_libra(libra)
        self.calcular()
        
    def calcular(self):
        libra = self.objmodelo.get_libra()
        kilogramo = libra * 0.45359237
        self.objmodelo.set_kilogramo(kilogramo)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_libra()
objvista = vista_libra()
objcontrolador = controlador_libra(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()