from modelo_Triangulo import modelo_triangulo
from vista_Triangulo import vistatriangulo

class controlador_triangulo:
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista

    def tomarDatos(self):
        datos_triangulo = self.objvista.obtener_datos()
        self.objmodelo.set_base(datos_triangulo[0])
        self.objmodelo.set_altura(datos_triangulo[1])
        self.calcular_Area()

    def verDatos(self):
        altura = self.objmodelo.get_altura()
        base = self.objmodelo.get_base()
        area = self.objmodelo.get_area()
        return altura, base, area

    def calcular_Area(self):
        base = self.objmodelo.get_base()
        altura = self.objmodelo.get_altura()
        area = base * altura / 2
        self.objmodelo.set_area(area)
        mensaje = self.objmodelo.imprimirDatos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_triangulo()
objvista = vistatriangulo()
objcontrolador = controlador_triangulo(objmodelo, objvista)
objvista.crear_Ventana()
objvista.boton_calcular.config(command=objcontrolador.tomarDatos)
objvista.iniciar()