from Modelo_Dv import modelo_division
from Vista_Dv import vista_division

class controlador_division:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_suma = self.objvista.obtener_datos()
        numero1,numero2 = datos_suma
        self.objmodelo.set_numero1(numero1)
        self.objmodelo.set_numero2(numero2)
        self.calcular()
        
    def calcular(self):
        numero1 = self.objmodelo.get_numero1()
        numero2 = self.objmodelo.get_numero2()
        total = numero1 / numero2
        self.objmodelo.set_total(total)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_division()
objvista = vista_division()
objcontrolador = controlador_division(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()