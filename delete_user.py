import tkinter as tk
from tkinter import messagebox
from sqldb_conn import create_connection, close_connection

def delete_user():
    user = entry_user.get().strip()
    
    if not user:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre de user a eliminar")
        return

    try:
        conn = create_connection()
        cursor = conn.cursor()

        #Se verifica si el user existe en la base de datos
        cursor.execute("SELECT user FROM user WHERE user = ?", (user,))
        fila = cursor.fetchone()

        if not fila:
            messagebox.showinfo("user no encontrado", f'El user {user} no existe en la BD')
            return

        #Se confirma si se desea eliminar el user
        confirm = messagebox.askyesno("Confirmar eliminación",
                                      f"¿Está seguro que desea elminar al user {user}?")
        
        if not confirm:
            messagebox.showinfo("Cancelado", "La operación fue cancelada")
            return
        
        #Se elimina el user de la base de datos
        cursor.execute("DELETE FROM user WHERE user = ?", (user,))
        conn.commit()

        messagebox.showinfo("Exito", f"Usario {user} eliminado con exito")
        entry_user.delete(0, tk.END)

    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", f"Error al eliminar el usario:\n {e}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado:\n {e}")

    finally:
        close_connection(conn)

ventana = tk.Tk()
ventana.title("Eliminar user")
ventana.geometry("400x250")
ventana.config(bg="#f5f7fb")
ventana.resizable(False, False)

titulo = tk.Label(ventana, text="Eliminar user", font=("Segoe UI", 16, "bold"), bg="#f5f7fb", fg="#2f4f4f")
titulo.pack(pady=20)

frame = tk.Frame(ventana, bg="#f5f7fb")
frame.pack(pady=10)

label_user = tk.Label(frame, text="Nombre de user:", bg="#f5f7fb", font=("Segoe UI", 11))
label_user.grid(row=0, column=0, padx=5, pady=5)

entry_user = tk.Entry(frame, width=30, font=("Segoe UI", 10))
entry_user.grid(row=0, column=1, padx=5, pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar user", bg="#e63946", fg="white",
                         font=("Segoe UI", 11, "bold"), relief="flat", padx=10, pady=5,
                         command=delete_user)
btn_eliminar.pack(pady=20)

ventana.mainloop()