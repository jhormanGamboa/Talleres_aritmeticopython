import tkinter as tk

class vista_division:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de Dividir")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#876b8d", highlightbackground="#7cfda3", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#ab8eb1", highlightbackground="#997d9f", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=270, height=230)
        
        self.label_num1 = tk.Label(self.contenedor, text="Ingrese el primer numero: ", bg="#bd9fc3")
        self.label_num1.pack(pady=5, padx=5, anchor='center')
        self.entry_num1 = tk.Entry(self.contenedor)
        self.entry_num1.pack(pady=5, padx=5)

        self.label_num2 = tk.Label(self.contenedor,text="Ingrese el segundo numero: ", bg="#bd9fc3")
        self.label_num2.pack(pady=5, padx=5, anchor='center')
        self.entry_num2 = tk.Entry(self.contenedor)
        self.entry_num2.pack(pady=5,padx=5)

        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Dividir numeros")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#bd9fc3")
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