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

# --- PASO 3: Cuadrículas para las matrices A, b y x ---
# Creamos un marco (Frame) a la derecha para organizar las entradas de texto
frame_matrices = tk.Frame(ventana, padx=20, pady=20)
frame_matrices.grid(row=0, column=1, sticky="n")

# Títulos superiores ("A", "b", "x")
tk.Label(frame_matrices, text="A", font=("Arial", 10, "bold")).grid(row=0, column=1, columnspan=4)
tk.Label(frame_matrices, text="b", font=("Arial", 10, "bold")).grid(row=0, column=5, padx=(15, 0))
tk.Label(frame_matrices, text="x", font=("Arial", 10, "bold")).grid(row=0, column=6, padx=(15, 0))

# Índices de columnas para A (0, 1, 2, 3)
for j in range(4):
    tk.Label(frame_matrices, text=str(j)).grid(row=1, column=j+1)

# Listas de Python para guardar las referencias a los campos de texto
# Esto nos va a servir en el futuro para extraer los números que escriba el usuario
entradas_A = []
entradas_b = []
entradas_x = []

# Creación de la cuadrícula 4x4 y los vectores 4x1
for i in range(4):
    # Índice de fila a la izquierda (0, 1, 2, 3)
    tk.Label(frame_matrices, text=str(i)).grid(row=i+2, column=0, padx=(0, 5))
    
    # Filas y columnas para la matriz A
    fila_A = []
    for j in range(4):
        entry = tk.Entry(frame_matrices, width=5)
        entry.grid(row=i+2, column=j+1, padx=2, pady=2)
        fila_A.append(entry)
    entradas_A.append(fila_A)
    
    # Columna de entradas para el vector b
    entry_b = tk.Entry(frame_matrices, width=5)
    entry_b.grid(row=i+2, column=5, padx=(15, 0), pady=2)
    entradas_b.append(entry_b)
    
    # Columna de entradas para el vector x (solo lectura para mostrar el resultado)
    entry_x = tk.Entry(frame_matrices, width=5, state="readonly")
    entry_x.grid(row=i+2, column=6, padx=(15, 0), pady=2)
    entradas_x.append(entry_x)
# --- Fin PASO 3 ---

# --- PASO 4: Botones de Acción y Determinante ---
# Creamos un marco inferior que ocupe las dos columnas de arriba
frame_inferior = tk.Frame(ventana, pady=10)
frame_inferior.grid(row=1, column=0, columnspan=2)

# Etiqueta de ayuda tal cual pide el laboratorio
lbl_ayuda = tk.Label(frame_inferior, text="Ayuda: el sistema de ecuaciones permite calcular A.x = b\nSe deben cargar los valores de A y b y luego,\nal calcular, se obtienen los valores de x")
lbl_ayuda.grid(row=0, column=0, columnspan=4, pady=(0, 15))

# 1. Definimos las funciones vacías (las programaremos después)
def limpiar_campos():
    pass

def calcular_sistema():
    pass

def calcular_determinante():
    pass

# 2. Botones centrales
btn_borrar = tk.Button(frame_inferior, text="Borrar valores", command=limpiar_campos)
btn_borrar.grid(row=1, column=1, padx=5, sticky="e")

btn_calcular = tk.Button(frame_inferior, text="Calcular", command=calcular_sistema)
btn_calcular.grid(row=1, column=2, padx=5, sticky="w")

# 3. Fila del Determinante
lbl_det = tk.Label(frame_inferior, text="Determinante:")
lbl_det.grid(row=2, column=0, sticky="e", pady=(15, 0))

# Campo de texto de solo lectura para mostrar el resultado del determinante
entry_det = tk.Entry(frame_inferior, width=10, state="readonly")
entry_det.grid(row=2, column=1, pady=(15, 0))

btn_det = tk.Button(frame_inferior, text="Calcular det.", command=calcular_determinante)
btn_det.grid(row=2, column=2, padx=5, sticky="w", pady=(15, 0))
# --- Fin PASO 4 ---

# Iniciar el bucle de eventos
ventana.mainloop()