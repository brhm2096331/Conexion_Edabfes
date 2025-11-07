"""This module creates the main menu window for user navigation."""

import tkinter as tk
import os
import sys
from tkinter import messagebox


def _safe_launch(script_name):
    # ejecuta script_name de forma segura
    try:
        # sys.executable para mantener el mismo intérprete
        cmd = f"{sys.executable} {script_name}"
        rc = os.system(cmd)
        if rc != 0:
            messagebox.showerror("Error al abrir ventana", "No se pudo abrir la ventana solicitada.")
    except Exception as e:
        messagebox.showerror("Error inesperado", "No se pudo abrir la ventana. Revise la consola para más detalles.")


def login_user():
    """Navigate to the login window."""
    try:
        ventana_menu.destroy()
        _safe_launch("login.py")
    except Exception as e:
        messagebox.showerror("Error", "No se pudo ir a Iniciar Sesión.")


def user_registration():
    """Navigate to the user registration window."""
    try:
        ventana_menu.destroy()
        _safe_launch("registro_usuario.py")
    except Exception as e:
        messagebox.showerror("Error", "No se pudo ir a Registrar usuario.")


def delete_user():
    """Navigate to the user deletion window."""
    try:
        ventana_menu.destroy()
        _safe_launch("delete_user.py")
    except Exception as e:
        messagebox.showerror("Error", "No se pudo ir a Borrar usuario.")


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

