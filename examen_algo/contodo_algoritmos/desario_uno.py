import tkinter as tk
import csv
import tkinter.messagebox
import os

def save_data():
    name = entry_name.get()
    grade = entry_grade.get()

    # Verificar que los campos no estén vacíos
    if name == "" or grade == "":
        tkinter.messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
        return

    # Verificar que la nota sea un número
    try:
        grade = int(grade)
    except ValueError:
        tkinter.messagebox.showerror("Error", "La nota debe ser un número.")
        return

    # Escribir los datos en el archivo CSV
    with open('notas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])

    # Limpiar los campos de entrada
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

    tkinter.messagebox.showinfo("Éxito", "Datos guardados correctamente.")

# Inicializar el archivo CSV con encabezados si no existe
if not os.path.exists('notas.csv'):
    with open('notas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Nota"])  # Especificar los encabezados aquí

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Gestor de Notas")

label_name = tk.Label(root, text="Nombre:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_grade = tk.Label(root, text="Nota:")
label_grade.pack()

entry_grade = tk.Entry(root)
entry_grade.pack()

save_button = tk.Button(root, text="Guardar", command=save_data)
save_button.pack(pady=10)

root.geometry("300x200")
root.mainloop()

