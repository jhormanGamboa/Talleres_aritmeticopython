from Modelo_Suma import modelo_suma
from Vista_Suma import vista_suma

class controlador_suma:
    
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
        total = numero1 + numero2
        self.objmodelo.set_total(total)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_suma()
objvista = vista_suma()
objcontrolador = controlador_suma(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()