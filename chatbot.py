import tkinter as tk
from tkinter import Entry, Button, Label, StringVar, Text, Scrollbar
import mysql.connector
import re
import random
import login




conm = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_certus',
    port='3709'
    )
cursor = conm.cursor()



sql_select_Query = f" SELECT * FROM materiales_curso "
cursor = conm.cursor()
cursor.execute(sql_select_Query)

records = cursor.fetchall()
rp = cursor.rowcount


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    print("DEBUG: Bot response:", response)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        prob = message_probability(message, list_of_words, single_response, required_words)
        if prob > highest_prob.get(bot_response, 0):
            highest_prob[bot_response] = prob

    # Recuperar respuestas de la base de datos
    cursor.execute("SELECT respuestas, palabras_clave FROM materiales_curso")
    materiales_curso = cursor.fetchall()
    for respuestas, palabras_clave in materiales_curso:
        response(respuestas, palabras_clave, single_response=True )

    # # Respuestas predefinidas{
    # response(respuestas, [palabras_clave], single_response= True, required_words=['saludo'])
    response('Hola,que tal saludos humano soy EduBot Pro', [ 'hi', 'saludos', 'buenas', 'hola'], single_response=True)
    response('Estoy bien y tú?', ['como', 'estas', 'va', 'vas', 'sientes'], single_response=True)
    response('Siempre a la orden', ['gracias', 'te lo agradezco', 'agradecido'], single_response=True)

    #Preguntas sobre la carrera
    response('¿Que Carrera Cursas?', ['curso','categoria','tema'], single_response=True)
    response('¿En que  te puedo brindar mi apoyo?', ['dds', 'diseño','desarrollo','software', 'reparador de impresoras'], single_response=True)
    response('Arquitectura y Diseño con IA, Diseño Grafico,Administracion de Sistemas,Diseño Desarrollo de Software,Administracion Financiera,Contabilidad y Tributacion,Administracion y Recursos Humanos', ['sexto ciclo', 'sexto', 'cursos','ciclo'], single_response=True)
    response('Explícame más sobre tu trabajo', ['trabajo', 'tareas', 'funciones'], single_response=True)
    response('¿Qué quieres que haga?', ['capacidades', 'habilidades', 'puedes'], single_response=True)

    #Preguntas para obtener Informacion
    response('¿Qué cursos ofrecen?', ['ofrecen', 'disponibles'], single_response=True)
    response('¿Cuál es el curso más popular?', [ 'popular', 'más demandado'], single_response=True)
    response('¿Deseas Inscribirte a este curso?', ['inscribirme', 'inscripción', 'matricularme'], single_response=True)
    
    #Preguntas sobre los recurso digitales
    response('La politica de la devolucion de los libros varia depende de los materiales didacticos prestados',['materiales','devolucion'], single_response=True)
    response('EL material prestado es un libro Su devolucion es de una semana academica',['libros','prestamos'],single_response=True)
    response('A través de la plataforma en línea del curso con tu nombre de usuario y contraseña.', ['ingresar','login'], single_response=True)
    response('Para este curso incluyen un libro de texto específico, asignaciones en línea y notas de conferencias proporcionadas por el instructor.', ['cuales','este','especificaciones'], single_response=True) 

    #Preguntas del Segundo Tema
    response('Claro te gustaria tener informacion de los cursos de Certus ¿De que carrera te gustaria obtener informacion',['tener'],single_response=True)

    response('En Certus tenemos varias carreras de diferentes rubros como negocios , finanzas , tecnologia ,creatividad',['rubros'],single_response=True)

    response('En el rubro de negocios encontramos Administracion de Empresas , Administracion de negocios internacionales , Marketing y Gestion de Medios Digitales',['negocios'],single_response=True)

    response('En el rubro de finanzas tenemos Contabilidad y tributacion',['finanzas'],single_response=True)

    response('En el rubro de tecnologia tenemos Diseño y Desarrollo de Software y Administracion de sistemas',['tecnologia'],single_response=True)

    response('En el rubro de creatividad tenemos las carreras de Diseño Grafico y Publicidad',['creatividad'],single_response=True)

    response('En la carrera de administracion de empresas aprenderas a gestionar recursos , procesos y personas de las distintas areas de una empresa .',['empresas'],single_response=True)

    response('En la carrera de administracion de negocios internacionales,coordina y gestiona procesos de importación, exportación, introducción y expedición de bienes',['internacionales'],single_response=True)

    response('En la carrera de Marketing y Gestion de medios digitales gestiona estrategias de marketing online y offline de manera innovadora, basados en el análisis de mercado',['marketing'],single_response=True)

    response('En la carrera de Administracion y Gestion Comercial, podrás liderar equipos comerciales, diseñar e implementar la estrategia y las políticas comerciales de una organización',['gestion'],single_response=True)

    response('En la carrera de Administracion y recursos humanos Aprenderás a optimizar procesos internos simplificando la administración de datos, documentación y proyectos',['recursos'],single_response=True)

    response('En la carrera de Contabilidad y Tributacion organiza e interpreta todas las operaciones contables; Además, podrás analizar y aplicar las normas tributarias',['contabilidad'],single_response=True)

    response('En la carrera de Administracion financiera y banca digital podrás identificar, analizar y gestionar los procesos administrativos y operaciones del sector financiero tradicional y digital',['financiera'],single_response=True)

    response('En la carrera de Diseño Desarrollo de Software podrás diseñar, desarrollar, probar, implementar y mejorar softwares empresariales',['desarrollo'],single_response=True)

    response('En la carrera de Administracion de Sistemas gestiona infraestructuras, plataformas, servicios y sistemas que permitan la transformación digital de una empresa',['sistemas'],single_response=True)

    response('En la carrera de Diseño grafico podrás diseñar mensajes de comunicación visual, desarrollar propuestas de diseño, formular sus prototipos y validarlos',['grafico'],single_response=True)

    response('En la carrera de Publicidad  podrás crear campañas publicitarias para promover marcas, productos y servicios a través de la aplicación de técnicas',['publicidad'],single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['No entendí tu consulta', 'No estoy seguro de lo que quieres', 'Disculpa, ¿puedes intentarlo de nuevo?'][random.randrange(3)]
    return response


conm.commit()

#Historial
root = tk.Tk()
root.title("EduBot Pro") #Titulo de nuestro chat bot
root.geometry("400x650+100+50") #Medida del angulo
root.resizable(width=False, height=False)
root.config(bg="aqua") #Color de fondo
titulo_text = Label(height=2,width=14, bg='aqua',text='EduChatBot',font=('Impact',20),fg='black') #Titulo
titulo_text.pack()
history_text = Text(root, wrap="word", width=40, height=25) #Historial de texto
history_text.pack()

scrollbar = Scrollbar(root, command=history_text.yview)
scrollbar.pack(side="right",fill="y")

history_text.config(yscrollcommand=scrollbar.set)

def chat_response(input_entry, response_label, history_text):
    user_input = input_entry.get()
    bot_response = get_response(user_input)
    response_label.config(text="EduBot Pro: "+ bot_response)
    history_text.insert(tk.END, f'Usuario:{user_input}\nEduBot Pro: {bot_response}\n\n')
    try:
        # Inserción en la base de datos
        cursor.execute("INSERT INTO materiales_curso (palabras_clave, respuestas) VALUES (%s, %s)", (user_input, bot_response))
        conm.commit()
    except mysql.connector.Error as err:
        print(f"Error al insertar en la base de datos: {err}")

    response_label.config(text="EduBot Pro: " + bot_response)



input_var = StringVar()

input_label = Label(root,bg='aqua',text="Ingresa tu mensaje:",font=("Arial",10,"bold"))
input_label.pack(pady=10)

input_entry = Entry(root, textvariable=input_var)
input_entry.pack(pady=10)

response_label = Label(root,bg='aqua', text="")
response_label.pack(pady=5)

chat_button = Button(root, text="Enviar",width=16 , command=lambda: chat_response(input_entry, response_label, history_text))
chat_button.pack(pady=10)



def logout():
    conm.close()
    root.destroy()

logout_button = Button(root, text="Cerrar Sesión",width=12 ,command=logout,bg="red",fg="white", font=("arial",8,"bold"))
logout_button.pack()
logout_button.place(x=295,y=20)


root.mainloop()
