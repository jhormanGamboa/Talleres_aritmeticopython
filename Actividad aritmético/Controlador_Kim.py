from Modelo_Kim import modelo_kilometro
from Vista_Kim import vista_kilometro

class controlador_kilometro:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_kilometro = self.objvista.obtener_datos()
        kilometro = datos_kilometro
        self.objmodelo.set_kilometro(kilometro)
        self.calcular()
        
    def calcular(self):
        kilometro = self.objmodelo.get_kilometro()
        millas = self.objmodelo.get_milla()
        millas = kilometro * 0.621371
        self.objmodelo.set_milla(millas)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_kilometro()
objvista = vista_kilometro()
objcontrolador = controlador_kilometro(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()