from Modelo_Prisma import datos
from Vista_Prisma import vista_prisma

class controlador_prisma:
    
    def __init__(self, objmodelo, objvista):
        self.objmodelo = objmodelo
        self.objvista = objvista
        
    def tomardatos(self):
        datos_prisma = self.objvista.obtener_datos()
        base,altura,ancho = datos_prisma
        self.objmodelo.set_base(base)
        self.objmodelo.set_altura(altura)
        self.objmodelo.set_ancho(ancho)
        self.calcular_volumen()
        
    def calcular_volumen(self):
        base = self.objmodelo.get_base()
        altura = self.objmodelo.get_altura()
        ancho = self.objmodelo.get_ancho()
        volumen = (base * altura * ancho)/2
        self.objmodelo.set_volumen(volumen)
        mensaje = self.objmodelo.imprimir_datos()
        self.objvista.mostrar_resultado(mensaje)
        return True

objmodelo = datos()
objvista = vista_prisma()
objcontrolador = controlador_prisma(objmodelo, objvista)
objvista.crear_ventana()
objvista.crear_boton()
objvista.boton.config(command=objcontrolador.tomardatos)
objvista.iniciar()