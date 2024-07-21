import tkinter as tk

class vista_libra:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de libra")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#839a92", highlightbackground="#e67746", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#b2cbc2", highlightbackground="#9bb3aa", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=270, height=200)
        
        self.label_libra = tk.Label(self.contenedor, text="Ingrese la libra: ", bg="#cae3da")
        self.label_libra.pack(pady=5, padx=5, anchor='center')
        self.entry_libra = tk.Entry(self.contenedor)
        self.entry_libra.pack(pady=5, padx=5)

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Calcular Kilogramo")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#cae3da")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            libra = float(self.entry_libra.get())
            return libra
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()