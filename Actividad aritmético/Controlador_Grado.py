from Modelo_Grado import modelo_gradoC
from Vista_Grado import vista_gradoC

class controlador_gradoC:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_grado = self.objvista.obtener_datos()
        self.objmodelo.set_celsius(datos_grado)
        self.calcular_grado()
        
    def calcular_grado(self):
        celsius = self.objmodelo.get_celsius()
        fahrenheit = (celsius*9/5)+32
        self.objmodelo.set_fahrentheit(fahrenheit)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_gradoC()
objvista = vista_gradoC()
objcontrolador = controlador_gradoC(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()