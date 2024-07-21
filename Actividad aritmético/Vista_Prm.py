import tkinter as tk

class vista_promedio:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de promedio")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#5dfc8a", highlightbackground="#7cfda3", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#9cfebc", highlightbackground="#64da58", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=270, height=230)
        
        self.label_num1 = tk.Label(self.contenedor, text="Ingrese el primer numero: ", bg="#bbffd5")
        self.label_num1.pack(pady=5, padx=5, anchor='center')
        self.entry_num1 = tk.Entry(self.contenedor)
        self.entry_num1.pack(pady=5, padx=5)

        self.label_num2 = tk.Label(self.contenedor,text="Ingrese el segundo numero: ", bg="#bbffd5")
        self.label_num2.pack(pady=5, padx=5, anchor='center')
        self.entry_num2 = tk.Entry(self.contenedor)
        self.entry_num2.pack(pady=5,padx=5)

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Promedio numeros")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#bbffd5")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            numero1 = float(self.entry_num1.get())
            numero2 = float(self.entry_num2.get())
            return numero1, numero2
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese numeros ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()