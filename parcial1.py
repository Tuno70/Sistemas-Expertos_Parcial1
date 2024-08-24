import tkinter as tk
from tkinter import ttk, messagebox

# Base de conocimientos: datos sobre las películas
peliculas = [
    {"titulo": "Inception", "genero": "acción", "duracion": "larga", "estilo": "suspenso"},
    {"titulo": "The Shawshank Redemption", "genero": "drama", "duracion": "larga", "estilo": "emocional"},
    {"titulo": "The Godfather", "genero": "drama", "duracion": "larga", "estilo": "crimen"},
    {"titulo": "The Dark Knight", "genero": "acción", "duracion": "larga", "estilo": "superhéroes"},
    {"titulo": "Toy Story", "genero": "animación", "duracion": "corta", "estilo": "familiar"},
    {"titulo": "Finding Nemo", "genero": "animación", "duracion": "corta", "estilo": "aventura"},
    {"titulo": "Parasite", "genero": "thriller", "duracion": "larga", "estilo": "suspenso"},
    {"titulo": "La La Land", "genero": "musical", "duracion": "larga", "estilo": "romántico"},
]

# Función para recomendar películas
def recomendar_pelicula():
    genero = genero_var.get()
    duracion = duracion_var.get()
    estilos = [estilo for estilo, var in estilo_vars.items() if var.get()]
    
    recomendaciones = []
    for pelicula in peliculas:
        if pelicula["genero"] == genero and pelicula["duracion"] == duracion and pelicula["estilo"] in estilos:
            recomendaciones.append(pelicula["titulo"])
    
    if recomendaciones:
        messagebox.showinfo("Recomendación", "Te recomendamos ver: " + ", ".join(recomendaciones))
    else:
        messagebox.showinfo("Recomendación", "Lo siento, no encontramos películas que coincidan con tus preferencias.")

# Función para reiniciar las selecciones
def reiniciar():
    genero_var.set('')
    duracion_var.set('')
    for estilo, var in estilo_vars.items():
        var.set(False)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto para Recomendación de Películas")

# Variables para almacenar las selecciones del usuario
genero_var = tk.StringVar()
duracion_var = tk.StringVar()
estilo_vars = {
    "suspenso": tk.BooleanVar(),
    "emocional": tk.BooleanVar(),
    "crimen": tk.BooleanVar(),
    "superhéroes": tk.BooleanVar(),
    "familiar": tk.BooleanVar(),
    "aventura": tk.BooleanVar(),
    "romántico": tk.BooleanVar()
}

# Crear los componentes de la interfaz
ttk.Label(ventana, text="Seleccione sus preferencias").grid(column=0, row=0, padx=10, pady=10, columnspan=2)

ttk.Label(ventana, text="Género:").grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
genero_combobox = ttk.Combobox(ventana, textvariable=genero_var)
genero_combobox['values'] = ("acción", "drama", "animación", "thriller", "musical")
genero_combobox.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(ventana, text="Duración:").grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
duracion_combobox = ttk.Combobox(ventana, textvariable=duracion_var)
duracion_combobox['values'] = ("corta", "larga")
duracion_combobox.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(ventana, text="Estilo:").grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
for i, (estilo, var) in enumerate(estilo_vars.items()):
    ttk.Checkbutton(ventana, text=estilo, variable=var).grid(column=0, row=4+i, padx=10, pady=5, sticky=tk.W)

# Botones para recomendar películas y reiniciar
ttk.Button(ventana, text="Recomendar Película", command=recomendar_pelicula).grid(column=0, row=11, columnspan=2, pady=10)
ttk.Button(ventana, text="Reiniciar", command=reiniciar).grid(column=0, row=12, columnspan=2, pady=10)

# Configuración de la ventana
ventana.geometry("400x400")
ventana.mainloop()
