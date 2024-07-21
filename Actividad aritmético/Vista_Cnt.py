import tkinter as tk

class vista_cantidad:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de intereses")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#f65d45", highlightbackground="#1b735e", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#fc9272", highlightbackground="#f9775c", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=280, height=190)
        
        self.label_cantidad = tk.Label(self.contenedor, text="Ingrese la cantidad de dinero:", bg="#ffac88")
        self.label_cantidad.pack(pady=5, padx=5, anchor='center')
        self.entry_cantidad = tk.Entry(self.contenedor)
        self.entry_cantidad.pack(pady=5, padx=5)

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular interez")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#ffac88")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            cantidad = float(self.entry_cantidad.get())
            return cantidad
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese la cantidad de dinero ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()