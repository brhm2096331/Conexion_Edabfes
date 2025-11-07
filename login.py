import os
import sys
import bcrypt
import tkinter as tk
from tkinter import messagebox
from sqldb_conn import create_connection, close_connection

def iniciar_sesion():
    user = entry_user.get().strip()
    password = entry_contraseña.get().strip()

    if not user or not password:
        messagebox.showwarning("Campos vacíos", "Por favor, ingrese su user/correo y contraseña.")
        return

    conn = None
    try:
        conn = create_connection()
        if conn is None:
            messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos.")
            return
        cursor = conn.cursor()

        # Usar los mismos nombres de tabla/columnas que en el registro (Usuario)
        query = "SELECT Usuario, Correo, Contraseña FROM Usuario WHERE Usuario = ? OR Correo = ?"
        cursor.execute(query, (user, user))
        fila = cursor.fetchone()

        if fila is None:
            messagebox.showerror("Error", "user o correo no encontrado.")
            return

        user_db, correo_db, password_db = fila

        # Verifica contraseña con bcrypt
        if bcrypt.checkpw(password.encode('utf-8'), password_db.encode('utf-8')):
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido {user_db}")
            entry_user.delete(0, tk.END)
            entry_contraseña.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error durante el inicio de sesión:\n{e}")

    finally:
        close_connection(conn)


def volver_al_menu():
    """Cierra esta ventana y regresa al menú principal"""
    ventana.destroy()
    os.system(f"{sys.executable} menu_principal.py")


# ======== Interfaz gráfica ========

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("400x400")
ventana.config(bg="#FFEBF7")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana, text="Inicio de sesión",
    font=("Century Gothic", 20, "bold"),
    bg="#FFEBF7", fg="#880E4F"
)
titulo.pack(pady=20)

frame = tk.Frame(ventana, bg="#FFEBF7")
frame.pack(pady=10)

# user/correo
tk.Label(frame, text="Usuario o correo:", bg="#FFEBF7", 
         font=("Century Gothic", 11)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_user = tk.Entry(frame, width=30, font=("Century Gothic", 10))
entry_user.grid(row=0, column=1, padx=5, pady=5)

# Contraseña
tk.Label(frame, text="Contraseña:", bg="#FFEBF7", font=("Century Gothic", 11)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_contraseña = tk.Entry(frame, show="*", width=30, font=("Century Gothic", 10))
entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

# Botón de inicio de sesión
btn_login = tk.Button(
    ventana,
    text="Iniciar sesión",
    bg="#FF5AA4",
    fg="white",
    activebackground="#C2185B",
    font=("Century Gothic", 11, "bold"),
    relief="flat",
    padx=12,
    pady=6,
    command=iniciar_sesion
)
btn_login.pack(pady=25)

btn_volver = tk.Button(
    ventana,
    text="Volver al menú",
    bg="#F70071",
    fg="white",
    activebackground="#C2185B",
    font=("Century Gothic", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5,
    command=volver_al_menu
)
btn_volver.pack(pady=5)

ventana.mainloop()
