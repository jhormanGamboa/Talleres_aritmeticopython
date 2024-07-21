import tkinter as tk

class vista_piramide:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de piramide")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#6ee39b", highlightbackground="#6ee39b", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#b8ec62", highlightbackground="#82d82d", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=250, height=280)
        
        self.label_longitudbase = tk.Label(self.contenedor, text="Ingrese la longitud de la piramide: ", bg="#edff97")
        self.label_longitudbase.pack(pady=5, padx=5, anchor='center')
        self.entry_longitudbase = tk.Entry(self.contenedor)
        self.entry_longitudbase.pack(pady=5, padx=5)

        self.label_anchobase = tk.Label(self.contenedor, text="Ingrese el ancho base de la piramide ", bg="#edff97")
        self.label_anchobase.pack(pady=5, padx=5, anchor='center')
        self.entry_anchobase = tk.Entry(self.contenedor)
        self.entry_anchobase.pack(pady=5, padx=5)
        
        self.label_altura = tk.Label(self.contenedor, text="Ingrese la altura de la pirámide: ", bg="#edff97")
        self.label_altura.pack(pady=5, padx=5, anchor='center')
        self.entry_altura = tk.Entry(self.contenedor)
        self.entry_altura.pack(pady=5, padx=5)

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular volumen")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#edff97")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            longitud_base = float(self.entry_longitudbase.get())
            ancho_base = float(self.entry_anchobase.get())
            altura = float(self.entry_altura.get())
            return longitud_base,ancho_base,altura
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()