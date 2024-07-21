import tkinter as tk
class vista_circuloR:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("ventana de radio de circulo")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="blue",highlightbackground="black",highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(padx=20,pady=20)
        
        self.label_radio = tk.Label(self.contenedor,text="Ingrese el radio del circulo",bg="white")
        self.label_radio.pack()
        self.entry_radio = tk.Entry(self.contenedor)
        self.entry_radio.pack()
        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor,text="calcular area",font=("Heveltica","bold"),bg="white",highlightbackground="black",highlightthickness=2)
        self.boton.pack()
        self.label_resultado = tk.Label(self.contenedor, text= "")
        self.label_resultado.pack()
        
    def obtener_datos(self):
        radio = float(self.entry_radio.get())
        return radio
    
    def mostrar_resultado(self,mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()