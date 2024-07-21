import tkinter as tk

class vista_hora:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de hora")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#6da9b5", highlightbackground="#7cfda3", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#9edae6", highlightbackground="#85c2ce", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=200, height=200)
        
        self.label_hora = tk.Label(self.contenedor, text="Ingrese las hora: ", bg="#b6f3ff")
        self.label_hora.pack(pady=5, padx=5, anchor='center')
        self.entry_hora = tk.Entry(self.contenedor)
        self.entry_hora.pack(pady=5, padx=5)


        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Hora a minuto")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#b6f3ff")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            hora = int(self.entry_hora.get())
            return hora
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese el numero ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()