import tkinter as tk

class vista_tropecioA:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de Trapecio")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#ffe987", highlightbackground="#1b735e", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#c79747", highlightbackground="#b47f30", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=200, height=280)
        
        self.label_basemayor = tk.Label(self.contenedor, text="Ingrese la base mayor", bg="#ffe08d")
        self.label_basemayor.pack(pady=5, padx=5, anchor='center')
        self.entry_basemayor = tk.Entry(self.contenedor)
        self.entry_basemayor.pack(pady=5, padx=5)

        self.label_basemenor = tk.Label(self.contenedor, text="Ingrese la base menor", bg="#ffe08d")
        self.label_basemenor.pack(pady=5, padx=5, anchor='center')
        self.entry_basemenor = tk.Entry(self.contenedor)
        self.entry_basemenor.pack(pady=5, padx=5)

        self.label_altura = tk.Label(self.contenedor, text="Ingrese la altura", bg="#ffe08d")
        self.label_altura.pack(pady=5, padx=5, anchor='center')
        self.entry_altura = tk.Entry(self.contenedor)
        self.entry_altura.pack(pady=5, padx=5)
        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular Área")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#ffe987")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            basemayor = float(self.entry_basemayor.get())
            basemenor = float(self.entry_basemenor.get())
            altura = float(self.entry_altura.get())
            return basemayor, basemenor, altura
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese números.")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()