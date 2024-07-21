from Modelo_Topecio import bases
from Vista_Tropecio import vista_tropecioA

class controlador_tropecioA:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_tropecio = self.objvista.obtener_datos()
        basemayor, basemenor, altura = datos_tropecio
        self.objmodelo.set_baseMayor(basemayor)
        self.objmodelo.set_baseMenor(basemenor)
        self.objmodelo.set_altura(altura)
        self.calcular_area()
        
    def calcular_area(self):
        altura = self.objmodelo.get_altura()
        basemayor = self.objmodelo.get_baseMayor()
        basemenor = self.objmodelo.get_baseMenor()
        area = (basemayor + basemenor) * altura / 2
        self.objmodelo.set_area(area)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = bases()
objvista = vista_tropecioA()
objcontrolador = controlador_tropecioA(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()