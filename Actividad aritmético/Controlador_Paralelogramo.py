from Modelo_Paralelogramo import modelo_paralelogramo
from Vista_Paralelogramo import vista_paralelogramo

class controlador_paralelogramo:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_paralelogramo = self.objvista.obtener_datos()
        base,altura = datos_paralelogramo
        self.objmodelo.set_base(base)
        self.objmodelo.set_altura(altura)
        self.calcular_area()
        
    def calcular_area(self):
        base = self.objmodelo.get_base()
        altura = self.objmodelo.get_altura()
        area = (base * altura)
        self.objmodelo.set_area(area)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_paralelogramo()
objvista = vista_paralelogramo()
objcontrolador = controlador_paralelogramo(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()