import tkinter as tk

class vista_paralelogramo:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de paralelogramo")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#805049", highlightbackground="#6ee39b", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#936059", highlightbackground="#6e3f39", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=240, height=250)
        
        self.label_base = tk.Label(self.contenedor, text="Ingrese la base del paralelogramo: ", bg="#b78179")
        self.label_base.pack(pady=5, padx=5, anchor='center')
        self.entry_base = tk.Entry(self.contenedor)
        self.entry_base.pack(pady=5, padx=5)

        self.label_altura = tk.Label(self.contenedor, text="Ingrese la altura del paralelogramo: ", bg="#b78179")
        self.label_altura.pack(pady=5, padx=5, anchor='center')
        self.entry_altura = tk.Entry(self.contenedor)
        self.entry_altura.pack(pady=5, padx=5)
        

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular Area")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#b78179")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            return base,altura
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()