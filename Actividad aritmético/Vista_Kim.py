import tkinter as tk

class vista_kilometro:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de kilometros")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#f65d45", highlightbackground="#1b735e", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#fc9272", highlightbackground="#f9775c", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=280, height=190)
        
        self.label_kilometro = tk.Label(self.contenedor, text="Ingrese los kilometros", bg="#ffac88")
        self.label_kilometro.pack(pady=5, padx=5, anchor='center')
        self.entry_kilometro = tk.Entry(self.contenedor)
        self.entry_kilometro.pack(pady=5, padx=5)

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular Millas")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#ffac88")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            kilometro = float(self.entry_kilometro.get())
            return kilometro
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()