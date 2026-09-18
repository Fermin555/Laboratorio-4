# Repositorio Github: git@github.com:Fermin555/Laboratorio-4.git
# Autores: Fermin Delgado, Kevin Ulloa

import tkinter as tk
import numpy as np

# --- PASO 1: Ventana principal ---
ventana = tk.Tk()
ventana.title("Resolución de sistemas de ecuaciones lineales mediante la Regla de Cramer")
ventana.geometry("600x400")

# --- PASO 2: Panel lateral de Dimensión ---
# Creamos una variable de Tkinter para guardar la dimensión seleccionada. 
# Por defecto, la imagen muestra seleccionado el 3x3.
dimension = tk.IntVar(value=3)

# Creamos un marco (Frame) a la izquierda para agrupar los botones
frame_izq = tk.Frame(ventana, padx=20, pady=20)
# grid() lo ubica en la fila 0, columna 0. "nw" significa alineado arriba a la izquierda (North-West)
frame_izq.grid(row=0, column=0, sticky="nw") 

# Etiqueta del marco
lbl_dim = tk.Label(frame_izq, text="Dimensión")
lbl_dim.pack(anchor="w", pady=(0, 10))

# Botones de opción (Radiobuttons) asociados a la misma variable
rb_2x2 = tk.Radiobutton(frame_izq, text="2 x 2", variable=dimension, value=2)
rb_2x2.pack(anchor="w")

rb_3x3 = tk.Radiobutton(frame_izq, text="3 x 3", variable=dimension, value=3)
rb_3x3.pack(anchor="w")

rb_4x4 = tk.Radiobutton(frame_izq, text="4 x 4", variable=dimension, value=4)
rb_4x4.pack(anchor="w")

# --- Fin PASO 2 ---

# Iniciar el bucle de eventos
ventana.mainloop()