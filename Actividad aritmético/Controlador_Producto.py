from Modelo_Producto import modelo_producto
from Vista_Producto import vista_producto

class controlador_producto:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_producto = self.objvista.obtener_datos()
        numero1,numero2 = datos_producto
        self.objmodelo.set_numero1(numero1)
        self.objmodelo.set_numero2(numero2)
        self.calcular_producto()
        
    def calcular_producto(self):
        numero1 = self.objmodelo.get_numero1()
        numero2 = self.objmodelo.get_numero2()
        total = numero1 * numero2
        self.objmodelo.set_total(total)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = modelo_producto()
objvista = vista_producto()
objcontrolador = controlador_producto(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()