import tkinter as tk

class vista_prisma:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de prisma")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#d95e30", highlightbackground="#e67746", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#f28f5d", highlightbackground="#e67746", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=240, height=280)
        
        self.label_base = tk.Label(self.contenedor, text="Ingrese la base del prisma: ", bg="#ffa873")
        self.label_base.pack(pady=5, padx=5, anchor='center')
        self.entry_base = tk.Entry(self.contenedor)
        self.entry_base.pack(pady=5, padx=5)

        self.label_altura = tk.Label(self.contenedor, text="Ingrese la altura del prisma: ", bg="#ffa873")
        self.label_altura.pack(pady=5, padx=5, anchor='center')
        self.entry_altura = tk.Entry(self.contenedor)
        self.entry_altura.pack(pady=5, padx=5)

        self.label_ancho = tk.Label(self.contenedor, text="Ingrese el ancho del prisma: ", bg="#ffa873")
        self.label_ancho.pack(pady=5, padx=5, anchor='center')
        self.entry_ancho = tk.Entry(self.contenedor)
        self.entry_ancho.pack(pady=5, padx=5)
        

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular Area")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#ffa873")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            ancho = float(self.entry_ancho.get())
            return base,altura,ancho
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()