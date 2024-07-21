import tkinter as tk

class vista_parimpar:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de par_impar")
        self.ventana.geometry("300x300")
        self.ventana.config(bg="#b30801", highlightbackground="#7cfda3", highlightthickness=5)
        
        self.contenedor = tk.Frame(self.ventana, bg="#e01703", highlightbackground="#f61f04", highlightthickness=5)
        self.contenedor.place(relx=0.5, rely=0.5, anchor="center", width=260, height=200)
        
        self.label_num1 = tk.Label(self.contenedor, text="Ingrese el primer numero: ", bg="#ff95bc")
        self.label_num1.pack(pady=5, padx=5, anchor='center')
        self.entry_num1 = tk.Entry(self.contenedor)
        self.entry_num1.pack(pady=5, padx=5)


        
    def crear_boton(self):
        self.boton = tk.Button(self.contenedor, text="Par o Impar")
        self.boton.pack(pady=10)
        self.label_resultado = tk.Label(self.contenedor, text="", bg="#ff95bc")
        self.label_resultado.pack(pady=10)
        
    def obtener_datos(self):
        try:
            numero1 = int(self.entry_num1.get())
            return numero1
        except ValueError:
            self.mostrar_resultado("Por favor, ingrese un numero ")
            return None
    
    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)
        
    def iniciar(self):
        self.ventana.mainloop()