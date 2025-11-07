import os
import sys
import re
import tkinter as tk
from tkinter import messagebox
import bcrypt
import pyodbc
from sqldb_conn import create_connection, close_connection


def validar_correo(correo):
    """Valida formato básico de correo electrónico."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))


def validar_contraseña(password):
    """Valida que la contraseña cumpla requisitos mínimos de seguridad."""
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"
    if not re.search(r'[A-Z]', password):
        return False, "La contraseña debe tener al menos una mayúscula"
    if not re.search(r'[a-z]', password):
        return False, "La contraseña debe tener al menos una minúscula"
    if not re.search(r'\d', password):
        return False, "La contraseña debe tener al menos un número"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "La contraseña debe tener al menos un carácter especial"
    return True, ""


def validar_nombre(nombre):
    """Valida que el nombre solo contenga letras y espacios."""
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]{2,50}$', nombre))


def validar_telefono(telefono):
    """Valida formato básico de número telefónico (10 dígitos)."""
    return bool(re.match(r'^\d{10}$', telefono))


def validar_usuario(usuario):
    """Valida formato de nombre de usuario (letras, números, guiones, sin espacios)."""
    if len(usuario) < 4:
        return False, "El usuario debe tener al menos 4 caracteres"
    if not re.match(r'^[a-zA-Z0-9_-]+$', usuario):
        return False, "El usuario solo puede contener letras, números, guiones y guiones bajos"
    return True, ""


def registrar_usuario():
    usuario = entry_usuario.get().strip()
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    correo = entry_correo.get().strip()
    telefono = entry_telefono.get().strip()
    password_plana = entry_contraseña.get().strip()
    password_confirm = entry_confirmar.get().strip()

    # Validaciones básicas
    if not usuario or not correo or not password_plana:
        messagebox.showwarning("Campos obligatorios", "Usuario, correo y contraseña no pueden estar vacíos.")
        return

    # Validar usuario
    usuario_valido, msg_usuario = validar_usuario(usuario)
    if not usuario_valido:
        messagebox.showerror("Error", msg_usuario)
        return

    # Validar correo
    if not validar_correo(correo):
        messagebox.showerror("Error", "El formato del correo electrónico no es válido.")
        return

    # Validar nombre y apellido si no están vacíos
    if nombre and not validar_nombre(nombre):
        messagebox.showerror("Error", "El nombre solo puede contener letras.")
        return
    if apellido and not validar_nombre(apellido):
        messagebox.showerror("Error", "El apellido solo puede contener letras.")
        return

    # Validar teléfono si no está vacío
    if telefono and not validar_telefono(telefono):
        messagebox.showerror("Error", "El teléfono debe tener 10 dígitos numéricos.")
        return

    # Validar contraseña
    if password_plana != password_confirm:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")
        return
    
    password_valida, msg_password = validar_contraseña(password_plana)
    if not password_valida:
        messagebox.showerror("Error", msg_password)
        return

    conn = None
    try:
        conn = create_connection()
        if conn is None:
            messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos. Intente de nuevo más tarde.")
            return
        cursor = conn.cursor()

        # Hasheo de contraseña
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password_plana.encode('utf-8'), salt)

        # Inserción
        query = """
        INSERT INTO Usuario (Usuario, Nombre, Apellido, Contraseña, Correo, Telefono)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (usuario, nombre, apellido, password_hashed.decode('utf-8'), correo, telefono)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Éxito", f"¡Usuario '{usuario}' registrado exitosamente!")
        limpiar_campos()

    except pyodbc.IntegrityError as e:
        if 'UNIQUE KEY' in str(e):
            messagebox.showerror("Error", "El nombre de usuario o correo electrónico ya existen.")
        else:
            messagebox.showerror("Error de integridad", f"Ocurrió un error: {e}")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")
    finally:
        close_connection(conn)


def limpiar_campos():
    entry_usuario.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)
    entry_confirmar.delete(0, tk.END)

def volver_al_menu():
    """Cierra esta ventana y regresa al menú principal"""
    ventana.destroy()
    os.system(f"{sys.executable} menu_principal.py")

# ====== Interfaz gráfica ======

ventana = tk.Tk()
ventana.title("Registro de usuario")
ventana.geometry("500x500")
ventana.config(bg="#f5f7fb")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana, text="📝 Registro de nuevo usuario",
    font=("Segoe UI", 18, "bold"), bg="#f5f7fb", fg="#2f4f4f"
)
titulo.pack(pady=20)

frame = tk.Frame(ventana, bg="#f5f7fb")
frame.pack(pady=10)

labels = ["Usuario:", "Nombre:", "Apellido:", "Correo:", "Teléfono:", "Contraseña:", "Confirmar contraseña:"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame, text=text, bg="#f5f7fb", font=("Segoe UI", 11)).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    entry = tk.Entry(frame, width=30, font=("Segoe UI", 10), show="*" if "Contraseña" in text or  "Confirmar" in text else "")
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_usuario, entry_nombre, entry_apellido, entry_correo, entry_telefono, entry_contraseña, entry_confirmar = entries

# Botón registrar
btn_registrar = tk.Button(
    ventana,
    text="Registrar usuario",
    bg="#28A745", fg="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=10, pady=6,
    command=registrar_usuario
)
btn_registrar.pack(pady=20)

btn_volver = tk.Button(
    ventana,
    text="Volver al menú",
    bg="#6C757D",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=10,
    pady=5,
    command=volver_al_menu
)
btn_volver.pack(pady=5)

ventana.mainloop()
