import mysql.connector
import getpass
import tkinter as tk
from tkinter import messagebox,Label,PhotoImage
from PIL import Image,ImageTk
import chatbot


def authenticate_user():

    username = username_entry.get()
    password = password_entry.get()
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='bd_certus',
                                             user='root',
                                             port='3709',
                                             password='')
        
        sql_select_query = f"select * from t_estudiantes where cod_estudiante='{username}' and con_estudiante='{password}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        row_count = cursor.rowcount
        
        if row_count == 1:
            messagebox.showinfo("Login Successful", "Inicio de sesión exitoso!")

        else:
            messagebox.showerror("Login Failed", "Error en las credenciales")
            
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error en la consulta: {e}")
        
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL conexión cerrada")

# Create a Tkinter window
root = tk.Tk()
root.title("Login")
root.geometry("400x650+100+50")
root.config(bg="blue")


# Creamos el titulo principal
titulo = Label(root,bg="blue", text="Login",font=("Calisto",36,"bold"))
titulo.pack(side="top" , pady=20)

# Insertamos una imagen 
img = Image.open("bot-conversacional.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)
img_label= Label(image=img,bg="blue")
img_label.pack(pady=15)

# Create username and password input fields
username_label = Label(root,bg="blue", text="Usuario:",font=("Arial",15,"bold") )
username_label.pack()
username_entry = tk.Entry(root, font="Arial",width=25,border=2,fg="black")
username_entry.pack(pady=20)


password_label = Label(root,bg="blue", text="Contraseña:",font=("Arial",15,"bold"))
password_label.pack()
password_entry = tk.Entry(root,show="*",width=25,border=2,fg="black",font="Arial")
password_entry.pack(pady=20)

# Create a login button
login_button = tk.Button(root, text="Login",cursor="hand2",width=39,bg="#57a1f8",fg="white",font=("Arial",11,"bold"),command=authenticate_user)
login_button.pack()

# Run the Tkinter main loop
root.mainloop()