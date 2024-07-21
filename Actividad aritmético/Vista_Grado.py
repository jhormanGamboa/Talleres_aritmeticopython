import tkinter as tk

class vista_gradoC:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de grados Fahrenheit")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#845cb5", highlightbackground="#1b735e", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#b68e9a",highlightbackground="#5a005a",highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=200, height=150)
        
        self.label_celsius = tk.Label(self.contenedor, text="Ingrese los grados Celsius", bg="#dfdbef")
        self.label_celsius.pack(pady=5, padx=5, anchor='center')
        self.label_celsius.pack()
        self.entry_celsius = tk.Entry(self.contenedor)
        self.entry_celsius.pack()
        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular Grados")
        self.boton.place(x=40,y=60)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#dfdbef")
        self.label_resultado.place(x=15,y=90)
        
    def obtener_datos(self):
        try:
            celsius = float(self.entry_celsius.get())
            return celsius
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros.")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()