import tkinter as tk
from tkinter import messagebox
import sqlite3
import http.client
import json

def create_database():
    the_db = sqlite3.connect("usuarios.db")
    c = the_db.cursor()
    c.execute(
        '''
            CREATE TABLE IF NOT EXISTS usuarios (
                username TEXT,
                password TEXT
            )
        '''
    )

    c.execute(
        "INSERT OR IGNORE INTO usuarios VALUES (?, ?)", 
        ("admin", "Vienna22*")
    )
    the_db.commit()
    the_db.close()

def verify_password(username, pwd):
    the_db = sqlite3.connect("usuarios.db")
    c = the_db.cursor()
    c.execute(
        "SELECT * FROM usuarios WHERE username=? AND password=?", 
        (username, pwd)
    )
    resultado = c.fetchone()
    the_db.close()
    return resultado is not None

def get_rm_characters():
    req = http.client.HTTPSConnection("rickandmortyapi.com")
    req.request("GET", "/api/character")
    response = req.getresponse()
    if response.status == 200:
        data = json.loads(response.read().decode())
        return [personaje['name'] for personaje in data['results']]
    else:
        return ["No se pudieron obtener los personajes"]

def show_characters():
    characters = get_rm_characters()
    characters_window = tk.Toplevel()
    characters_window.title("I'M PICKLE RICK!!!!!!!")
    characters_window.geometry("300x400")
    lista = tk.Listbox(characters_window, width=40)
    lista.pack(pady=10)
    for name in characters:
        lista.insert(tk.END, name)
    tk.Button(characters_window, text="Close window", command=characters_window.destroy).pack(pady=10)

def login():
    user = entrada_usuario.get()
    pwd = entrada_clave.get()
    if verify_password(user, pwd):
        show_characters()
    else:
        messagebox.showerror("Error", "Usuario o contraseña están mal")
    entrada_usuario.delete(0, tk.END)
    entrada_clave.delete(0, tk.END)

create_database()
ventana = tk.Tk()
ventana.title("Login into the system")
ventana.geometry("300x200")

tk.Label(ventana, text="Usuario:").pack(pady=5)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entrada_clave = tk.Entry(ventana, show="*")
entrada_clave.pack(pady=5)

tk.Button(ventana, text="Login", command=login).pack(pady=20)

ventana.mainloop()
