import math
import tkinter as tk
from tkinter import messagebox



class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

#clase de cilindro, esfera y piramide

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # math.pi es el equivalente a Math.PI
        # math.pow(base, exp) es el equivalente a Math.pow(base, exp)
        self.volumen = math.pi * self.altura * math.pow(self.radio, 2)

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_bases = 2 * math.pi * math.pow(self.radio, 2)
        self.superficie = area_lateral + area_bases

#clase de esfera

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        # Se usa (4/3) en lugar de 1.333 para mayor precisión
        self.volumen = (4/3) * math.pi * math.pow(self.radio, 3)

    def calcular_superficie(self):
        self.superficie = 4 * math.pi * math.pow(self.radio, 2)

#clase de piramide

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.calcular_volumen()
        self.calcular_superficie()

    def calcular_volumen(self):
        self.volumen = (math.pow(self.base, 2) * self.altura) / 3

    def calcular_superficie(self):
        area_base = math.pow(self.base, 2)
        area_lateral = 2 * self.base * self.apotema
        self.superficie = area_base + area_lateral

#clases de las ventanas

   #Ventana para ingresar los datos de un Cilindro.
class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        # crea una ventana hija de la principal
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        
        # Etiquetas y campos de entrada
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=135)

        # Botón
        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=80, width=135)

        # Etiquetas para resultados
        self.volumen_lbl = tk.Label(self, text="Volumen (cm³):")
        self.volumen_lbl.place(x=20, y=110)
        self.superficie_lbl = tk.Label(self, text="Superficie (cm²):")
        self.superficie_lbl.place(x=20, y=140)



    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            
            cilindro = Cilindro(radio, altura)
            

            self.volumen_lbl.config(text=f"Volumen (cm³): {cilindro.volumen:.2f}")
            self.superficie_lbl.config(text=f"Superficie (cm²): {cilindro.superficie:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")

    #Ventana para ingresar los datos de una Esfera

class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=50, width=135)

        self.volumen_lbl = tk.Label(self, text="Volumen (cm³):")
        self.volumen_lbl.place(x=20, y=90)
        self.superficie_lbl = tk.Label(self, text="Superficie (cm²):")
        self.superficie_lbl.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.volumen_lbl.config(text=f"Volumen (cm³): {esfera.volumen:.2f}")
            self.superficie_lbl.config(text=f"Superficie (cm²): {esfera.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")



    #Ventana para ingresar los datos de una Pirámide.

class VentanaPiramide(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)

        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50, width=135)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80, width=135)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=120, y=110, width=135)

        self.volumen_lbl = tk.Label(self, text="Volumen (cm³):")
        self.volumen_lbl.place(x=20, y=140)
        self.superficie_lbl = tk.Label(self, text="Superficie (cm²):")
        self.superficie_lbl.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.volumen_lbl.config(text=f"Volumen (cm³): {piramide.volumen:.2f}")
            self.superficie_lbl.config(text=f"Superficie (cm²): {piramide.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")


    #Ventana principal:Menu

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        
        # Botones para abrir cada ventana de figura 
        tk.Button(self, text="Cilindro", command=self.abrir_cilindro).place(x=20, y=50, width=80)
        tk.Button(self, text="Esfera", command=self.abrir_esfera).place(x=125, y=50, width=80)
        tk.Button(self, text="Pirámide", command=self.abrir_piramide).place(x=225, y=50, width=100)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)


#punto de entrada



class Principal:

    @staticmethod
    def main():

        app = VentanaPrincipal()
        app.mainloop()


if __name__ == "__main__":
    Principal.main()