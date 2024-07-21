from Modelo_Raiz import modelo_raiz
from Vista_Raiz import vista_raiz

class controlador_raiz:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_suma = self.objvista.obtener_datos()
        numero1 = datos_suma
        self.objmodelo.set_numero1(numero1)
        self.calcular_raiz()
        
    def calcular_raiz(self):
        numero1 = self.objmodelo.get_numero1()
        total = numero1 ** 0.5
        self.objmodelo.set_total(total)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_raiz()
objvista = vista_raiz()
objcontrolador = controlador_raiz(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()