import tkinter as tk

class vistatriangulo:
    def crear_Ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana de Triángulo")
        self.ventana.geometry("300x300")
        self.contenedor = tk.Frame(self.ventana)
        self.contenedor.pack(pady=20, padx=20)

        self.label_altura = tk.Label(self.contenedor, text="Ingrese la altura del triángulo")
        self.label_altura.pack()
        self.entry_altura = tk.Entry(self.contenedor)
        self.entry_altura.pack()

        self.label_base = tk.Label(self.contenedor, text="Ingrese la base del triángulo")
        self.label_base.pack()
        self.entry_base = tk.Entry(self.contenedor)
        self.entry_base.pack()

        self.boton_calcular = tk.Button(self.contenedor, text="Calcular Área")
        self.boton_calcular.pack()

        self.label_resultado = tk.Label(self.contenedor, text="")
        self.label_resultado.pack()

    def obtener_datos(self):
        altura = float(self.entry_altura.get())
        base = float(self.entry_base.get())
        return [base, altura]

    def mostrar_resultado(self, mensaje):
        self.label_resultado.config(text=mensaje)

    def iniciar(self):
        self.ventana.mainloop()