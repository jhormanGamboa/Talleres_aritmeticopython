from Modelo_Cnt import modelo_cantidad
from Vista_Cnt import vista_cantidad

class controlador_cantidad:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_cantidad = self.objvista.obtener_datos()
        cantidad = datos_cantidad
        self.objmodelo.set_cantidad(cantidad)
        self.calcular_cantidad()
        
    def calcular_cantidad(self):
        cantidad = self.objmodelo.get_cantidad()
        interez = self.objmodelo.get_interez()
        interez = cantidad * 0.05
        self.objmodelo.set_interez(interez)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_cantidad()
objvista = vista_cantidad()
objcontrolador = controlador_cantidad(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()