from Modelo_PyI import modelo_parimpar
from Vista_PyI import vista_parimpar

class controlador_parimpar:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos = self.objvista.obtener_datos()
        numero1 = datos
        self.objmodelo.set_numero1(numero1)
        self.calcular_par_impar()
        
    def calcular_par_impar(self):
        numero1 = self.objmodelo.get_numero1()
        if numero1 % 2 == 0:
            par_impar = "El numero es par"
        else:
            par_impar = "El numero es impar"
        self.objmodelo.set_par_impar(par_impar)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_parimpar()
objvista = vista_parimpar()
objcontrolador = controlador_parimpar(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()