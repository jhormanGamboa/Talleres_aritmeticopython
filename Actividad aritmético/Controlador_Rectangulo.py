from Modelo_Rectangulo import modelo_rectangulo
from Vista_Rectangulo import vista_rectangulo

class controlador_rectangulo:
  def __init__(self,objmodelo,objvista):
    self.objmodelo = objmodelo
    self.objvista = objvista
    
  def Tomardatos(self):
    datos_rectangulo = self.objvista.obtener_datos()
    self.objmodelo.set_longitud(datos_rectangulo[0])
    self.objmodelo.set_ancho(datos_rectangulo[1])
    self.calcular_area()

  def calcular_area(self):
    longitud= self.objmodelo.get_longitud()
    ancho = self.objmodelo.get_ancho()
    area = self.objmodelo.get_area()
    area = longitud * ancho
    self.objmodelo.set_area(area)
    mensaje = self.objmodelo.imprimir_datos()
    self.objvista.mostrar_resultado(mensaje)
    return True

#codigo principal
objmodelo = modelo_rectangulo()
objvista = vista_rectangulo()
objcontrolador = controlador_rectangulo(objmodelo,objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton1.config(command = objcontrolador.Tomardatos)
objvista.iniciar()