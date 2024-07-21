from Modelo_Hr import modelo_hora
from Vista_Hr import vista_hora

class controlador_hora:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_hora = self.objvista.obtener_datos()
        hora = datos_hora
        self.objmodelo.set_hora(hora)
        self.calcular_hora()
        
    def calcular_hora(self):
        hora = self.objmodelo.get_hora()
        minuto = hora * 60
        self.objmodelo.set_minuto(minuto)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_hora()
objvista = vista_hora()
objcontrolador = controlador_hora(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()