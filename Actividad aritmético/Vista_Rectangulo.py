import tkinter as tk

class vista_rectangulo:
  def crear_ventana(self):
    self.ventana = tk.Tk()
    self.ventana.title("ventana de rectángulo")
    self.ventana.geometry("300x300")
    self.ventana.config(bg="#9e2c3d",highlightbackground="#da040d",highlightthickness=9)
    self.contenedor = tk.Frame(self.ventana)
    self.contenedor.pack(pady=20,padx=20)
    self.contenedor.config(bg="#d7d1c8",highlightbackground = "#640b0f",highlightthickness = 5)
    
    self.label_longitud = tk.Label(self.contenedor, text="Ingrese la longitud del rectángulo",bg = "#e5e0da")
    self.label_longitud.pack()
    self.entry_longitud = tk.Entry(self.contenedor)
    self.entry_longitud.pack()
    
    self.label_ancho = tk.Label(self.contenedor, text="Ingrese el ancho del rectángulo ",bg = "#e5e0da")
    self.label_ancho.pack()
    self.entry_ancho = tk.Entry(self.contenedor)
    self.entry_ancho.pack()

  def crear_boton(self):
    self.boton1 = tk.Button(self.contenedor, text="Calcular área", font=("Helvetica", 8, "bold"), bg="white", highlightbackground="black", highlightthickness=2)
    self.boton1.pack()
    
    self.label_resultado = tk.Label(self.contenedor, text="")
    self.label_resultado.pack()

  def obtener_datos(self):
    longitud = float(self.entry_longitud.get())
    ancho = float(self.entry_ancho.get())
    return [longitud,ancho]

  def mostrar_resultado(self,mensaje):
    self.label_resultado.config(text=mensaje)

  def iniciar(self):
    self.ventana.mainloop()