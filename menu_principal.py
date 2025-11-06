"""This module creates the main menu window for user navigation."""

import tkinter as tk
import os
import sys


def login_user():
    """Navigate to the login window."""
    ventana_menu.destroy()
    os.system(f"{sys.executable} login.py")


def user_registration():
    """Navigate to the user registration window."""
    ventana_menu.destroy()
    os.system(f"{sys.executable} registro_usuario.py")


def delete_user():
    """Navigate to the user deletion window."""
    ventana_menu.destroy()
    os.system(f"{sys.executable} delete_user.py")


def exit_from_menu():
    """Exit the main menu and the main script."""
    ventana_menu.destroy()


# ======== GUI from the menu ========

ventana_menu = tk.Tk()
ventana_menu.title("Menú Principal")
ventana_menu.geometry("400x350")
ventana_menu.config(bg="#f0f0f0")

# Tittle for the menu window
titulo = tk.Label(
    ventana_menu,
    text="Menú Principal",
    font=("Segoe UI", 18, "bold"),
    bg="#f0f0f0",
    fg="#333",
)
titulo.pack(pady=15)

# Button to the user login window
btn_ir_a_login = tk.Button(
    ventana_menu,
    text="Iniciar Sesión",
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=20,
    pady=8,
    command=login_user
)
btn_ir_a_login.pack(pady=8)

# Button to the user registration window
btn_ir_a_login = tk.Button(
    ventana_menu,
    text="Registrar usuario",
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=20,
    pady=8,
    command=user_registration
)
btn_ir_a_login.pack(pady=8)

# Button to the user elimination window
btn_ir_a_login = tk.Button(
    ventana_menu,
    text="Borrar Usuario",
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=20,
    pady=8,
    command=delete_user
)
btn_ir_a_login.pack(pady=8)

# Button to exit the menu
btn_salir = tk.Button(
    ventana_menu,
    text="Salir",
    bg="#dc3545",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=12,
    pady=5,
    command=exit_from_menu
)
btn_salir.pack(pady=10)

ventana_menu.mainloop()

