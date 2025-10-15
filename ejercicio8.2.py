import math
import tkinter as tk
from tkinter import messagebox

#clase nota

class Notas:
    def __init__(self):
        self.lista_notas = []

    def set_notas(self, notas):
        self.lista_notas = notas

    def calcular_promedio(self):


        if not self.lista_notas:
            return 0.0
        

        suma= sum(self.lista_notas[1:])
        

        return suma / len(self.lista_notas)

    def calcular_desviacion_estandar(self):

        if len(self.lista_notas) < 2:
            return 0.0


        promedio = self.calcular_promedio() 
        
        suma_cuadrados = 0
        for nota in self.lista_notas:
            suma_cuadrados += math.pow(nota - promedio, 2)
        

        return math.sqrt(suma_cuadrados / len(self.lista_notas))

    def calcular_menor(self):
        if not self.lista_notas:
            return 0.0
        return min(self.lista_notas)

    def calcular_mayor(self):
        if not self.lista_notas:
            return 0.0
        return max(self.lista_notas)


#clase ventana principal

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.notas = Notas()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.eval("tk::PlaceWindow . center")
        self.crear_widgets()

    def crear_widgets(self):
        self.campos_notas = []
        for i in range(5):
            y_pos = 20 + i * 30
            etiqueta = tk.Label(self, text=f"Nota {i+1}:")
            etiqueta.place(x=20, y=y_pos, width=80, height=23)
            campo = tk.Entry(self)
            campo.place(x=105, y=y_pos, width=135, height=23)
            self.campos_notas.append(campo)

        boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        boton_calcular.place(x=20, y=170, width=100, height=25)
        boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        boton_limpiar.place(x=130, y=170, width=100, height=25)

        self.promedio_lbl = tk.Label(self, text="Promedio: ", anchor="w")
        self.promedio_lbl.place(x=20, y=210, width=240, height=23)
        self.desviacion_lbl = tk.Label(self, text="Desviación Estándar: ", anchor="w")
        self.desviacion_lbl.place(x=20, y=240, width=240, height=23)
        self.mayor_lbl = tk.Label(self, text="Nota Mayor: ", anchor="w")
        self.mayor_lbl.place(x=20, y=270, width=240, height=23)
        self.menor_lbl = tk.Label(self, text="Nota Menor: ", anchor="w")
        self.menor_lbl.place(x=20, y=300, width=240, height=23)

    def limpiar(self):
        for campo in self.campos_notas:
            campo.delete(0, tk.END)
        self.promedio_lbl.config(text="Promedio: ")
        self.desviacion_lbl.config(text="Desviación Estándar: ")
        self.mayor_lbl.config(text="Nota Mayor: ")
        self.menor_lbl.config(text="Nota Menor: ")

    def calcular(self):
        notas_ingresadas = []
        try:
            for campo in self.campos_notas:
                nota = float(campo.get())
                notas_ingresadas.append(nota)
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese solo números en todos los campos.")
            return

        self.notas.set_notas(notas_ingresadas)
        promedio = self.notas.calcular_promedio()
        desviacion = self.notas.calcular_desviacion_estandar()
        menor = self.notas.calcular_menor()
        mayor = self.notas.calcular_mayor()

        self.promedio_lbl.config(text=f"Promedio: {promedio:.2f}")
        self.desviacion_lbl.config(text=f"Desviación Estándar: {desviacion:.2f}")
        self.mayor_lbl.config(text=f"Nota Mayor: {mayor:.2f}")
        self.menor_lbl.config(text=f"Nota Menor: {menor:.2f}")


class Principal:
    @staticmethod
    def main():
      
        app = VentanaPrincipal()
        app.mainloop()

# Puerta de entrada que ejecuta el método main de la clase Principal
if __name__ == "__main__":
    Principal.main()