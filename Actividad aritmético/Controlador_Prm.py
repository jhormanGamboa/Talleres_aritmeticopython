from Modelo_Prm import modelo_promedio
from Vista_Prm import vista_promedio

class controlador_promedio:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_promedio = self.objvista.obtener_datos()
        numero1,numero2 = datos_promedio
        self.objmodelo.set_numero1(numero1)
        self.objmodelo.set_numero2(numero2)
        self.calcular()
        
    def calcular(self):
        numero1 = self.objmodelo.get_numero1()
        numero2 = self.objmodelo.get_numero2()
        promedio = (numero1 + numero2)/2
        self.objmodelo.set_promedio(promedio)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_promedio()
objvista = vista_promedio()
objcontrolador = controlador_promedio(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()