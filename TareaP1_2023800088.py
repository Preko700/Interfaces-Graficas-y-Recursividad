from tkinter import *
from tkinter import messagebox, PhotoImage
import time 
import os
from PIL import Image, ImageTk
import pygame
def reproducir():
    #Incializa el mixer
    pygame.mixer.init()
    # Carga el audio directamente con pygame.mixer.Sound
    sound = pygame.mixer.Sound("./Resources/Casey Edwards & Victor Borba – Vacant Surrender [Official Audio].wav")#Ruta de la cancion
    #Reproduce la cancion
    sound.play()
def pausar():
    # Pregunta si el mixer se ha inicializado
    if pygame.mixer.get_init():
        # si, si a inicializado el mixer, lo pausa
        pygame.mixer.pause()
    else:
        #De lo contrario devuelve un mensaje
        messagebox.showinfo("Aviso","No se ha inicializado el mezclador de audio.")
#E recibe el nombre del archivo de imagen
#S la imagen
#R Solo archivos que se encuentren en la carpeta Resources
def LoadImage(nombre): # Funcion para cargar las imagenes
    ruta = os.path.join('Resources',nombre) # se define la ubicación de la imagen
    imagen = ImageTk.PhotoImage(file=ruta)
    return imagen #Devuelve la imagen
def mostrar_divisores(): #Funcion para mostrar los divisores de un numero, con interfaz grafica
  divisores=Tk()#Renombrar el metodo Tk
  divisores.title("Divisores de un Número")#Titulo de la ventana
  divisores.minsize(300,238)#Medidas
  divisores.resizable(width=NO,height=NO)#Las medidas pueden ser ajustables? NO
  num=Entry(divisores,width=25,bg="white")# crea la caja de texto para recibir el numero
  num.place(x=50,y=75)# lugar de la caja
  txt1=Label(divisores,text="Ingrese un número",bg="white")#texto
  txt1.place(x=50,y=50)#Ubicacion del texto
  aceptar=Button(divisores,text="ACEPTAR",bg="white",fg="black",command=lambda: ValidarNumbDivi(num.get()))# Boton Aceptar que al ser presionado, llama a la funcion ValidarNumbDivi para tratar el str ingresado
  aceptar.place(x=50,y=90)#Ubicacion del boton
  divisores.mainloop()
def ValidarNumbDivi(num): #Funcion que obtiene el numero ingresado
  try:
    numero = int(num) # Intenta convertirlo a un numero
    return Calcular_Divisores(abs(numero))#Si es un numero Integer, lo convierte a positivo y lo manda a la funcion para obtener sus divisores
  except ValueError: 
    messagebox.showwarning("Error", "Ingrese un número, por favor") #Si no puede, da mensaje de advertencia
#E Recibe un numero de tipo Integer de la funcion ValidarNumbDivi
#R Solo puede operar numeros enteros
#S Devuelve un mensaje con todos los divisores del numero entrante
def Calcular_Divisores(numero):
  divisores = [] #Los divisores seran almacenados en esta lista
  resultado = f"Los divisores de {numero} son: "
  if numero==0:
       return messagebox.showwarning("Error","Ingrese un numero distinto de 0") 
  else:
  # Recorre todos los números desde 1 hasta la raíz cuadrada de 'numero'
    for i in range(1, int(numero ** 0.5) + 1):
    # Si el resto de la división de 'numero' entre 'i' es 0, 'i' es un divisor
        if numero % i == 0:
      # Añade 'i' a la lista de divisores
          divisores.append(i)
      #Si 'i' no es igual a 'numero' dividido por 'i' (es decir, no es un divisor perfecto)
          if i != numero // i:
       # Añade 'numero' dividido por 'i' a la lista de divisores
            divisores.append(numero // i)
            #Si el numero es 0 no tiene divisores, por lo que pide un numero distinto de 0
            if numero==0:
              return messagebox.showwarning("Error","Ingrese un numero distinto de 0")
  # Recorrer cada divisor en la lista      
  for divisor in divisores:
    # Concatena cada divisor al 'resultado' con una coma al final
    resultado += f"{divisor}, "
  resultado = resultado[:-2]  # Eliminar las últimas dos comas
  # Muestra un mensaje con la lista de los divisores
  messagebox.showinfo("Resultado", resultado)
#E Un numero entero
#R Numero Entero
#S Mensaje con una tabla de multiplicar del 1 al 10 del numero ingresado
def Tablas():
  tablas=Tk() #Renombrar el metodo Tk
  tablas.title("tablas de un Número")#Titulo de la pantalla Tk
  tablas.minsize(300,238)#Medidas
  tablas.resizable(width=NO,height=NO)#No se puede ajustar las proporciones de la pantalla
  num=Entry(tablas,width=25,bg="white")# crea la caja de texto para recibir el numero
  num.place(x=50,y=75)# lugar de la caja
  txt1=Label(tablas,text="Ingrese un número",bg="white")#texto
  txt1.place(x=50,y=50)#Lugar del txt
  aceptar=Button(tablas,text="ACEPTAR",bg="white",fg="black",command=lambda: ValidarNumbTablas(num.get()))# boton de aceptar, que llama la funcion ValidarNumbTablas para validar si lo ingresado es un numero de tipo int
  aceptar.place(x=50,y=90)#Lugar del boton aceptar
  tablas.mainloop()
#Funcion que recibe el numero ingresado en la pantalla "Tablas de un Numero" y valida que sea int
def ValidarNumbTablas(num):
  try:
    numero = int(num) # Intenta convertirlo a un numero
    return Tablas_Num(abs(numero))#Si es un numero Integer, lo convierte a positivo y lo manda a la funcion para obtener sus divisores
  except ValueError: 
    messagebox.showwarning("Error", "Ingrese un número, por favor") #Si no puede, da mensaje de advertencia
#E Recibe un Int
#R Solo puede utilizar int
#S Mensaje con las tablas del 1 al 10 del num de entrada
def Tablas_Num(num):
  res=""#Variable para almacenar los resultados
  for i in range(1, 11):# i es una variable que servira para multiplicar el numero y pasar por las tablas del 1 al 10 sin contar la del 0, por eso el i es en un rango de 1 a 11
    res+=f"{num} x {i} = {num * i}\n" #Multiplicacion por i y formato del mensaje, siendo guardados en la variable res con un '\n' para que no se guarden seguidos
  messagebox.showinfo("Resultado", res)#Mensaje con las tablas del 1 al 10 del numero ingresado
#E No recibe nada
#R Ningun tipo de dato
#S Pantalla con informacion del estudiante
def Info():
  main=Toplevel(bg="white")# se crea la ventana, top level porque es una ventana informativa
  main.title("Informacio sobre: Adrian Monge") # titulo de la ventana
  main.minsize(1024,900)# tamaño de ventana
  main.resizable(width=NO,height=NO) # Tamaño Reajustable? No
  Title=Label(main,text="DATOS GENERALES DEL ESTUDIANTE",bg="white",fg="black")#Titulo con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
  Title.place(x=450,y=25)#ubicacion del titulo
  Name=Label(main,text="Nombre: Adrián Monge Mairena",bg="white",fg="Black")#Variable que muestra un nombre con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
  Name.place(x=50,y=50)#Ubicacion de la variable "Name"
  Age=Label(main,text="Edad: 21",bg="white",fg="Black")#Variable que muestra una edad con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
  Age.place(x=50,y=75)#ubicacion de la variable Age
  Hobbies=Label(main,text="Hobbies: Jugar a videojuegos",bg="white",fg="Black")#Variable que muestra una texto con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
  Hobbies.place(x=50,y=100)#ubicacion de la varibale Hobbies
  Movietxt=Label(main,text="Pelicula Favorita: Ready Player One",bg="white",fg="Black")#Variable que muestra un texto con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro  
  Movietxt.place(x=50,y=125)#Ubicacion de la variable Movietxt
  imagen2 = LoadImage("RPO-300x171.jpg")# carga la imagen 
  Movie=Label(main, image=imagen2) # etiqueta que va a contener la imagen
  Movie.place (x=300, y=125)# posicion de la imagen
  imagen3=LoadImage("Selfie1.jpg")# carga la imagen 
  selfitxt=Label(main,text="Las fotazas:",bg="white",fg="Black")#Variable que muestra una texto con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro
  selfitxt.place(x=10,y=280)#Ubicacion de la variable selfitxt
  selfi=Label(main,image=imagen3)# etiqueta que va a contener la imagen
  selfi.place(x=10,y=295)# posicion de la imagen
  imagen5=LoadImage("best1.jpg")# carga la imagen 
  fampic1=Label(main,image=imagen5)# etiqueta que va a contener la imagen
  fampic1.place(x=400,y=295)#ubicacion de la variable fampic1
  imagen4=LoadImage("Family1.jpg")# carga la imagen 
  selfitxt=Label(main,text="La fotaza con la family:",bg="white",fg="Black")#Variable que muestra una texto con los parametro "bg" y "fg" de "background"=Fondo en blanco y "fontground"=color de la fuente en negro
  selfitxt.place(x=50,y=700)#ubicacion de la variable fampic1
  fampic=Label(main,image=imagen4)# etiqueta que va a contener la imagen
  fampic.place(x=300,y=700)#ubicacion de la variable fampic
  boton_reproducir = Button(main,text="Reproducir", command=reproducir)#Boton que al ser presionado llamada a la funcion reproducir
  boton_reproducir.place(x=700,y=50)#Ubicacion del boton
  boton_pausar = Button(main,text="Pausar", command=pausar)#Boton que al ser presionado llamada a la funcion pausar
  boton_pausar.place(x=775,y=50)#Ubicacion del boton
  main.mainloop()

def Animación():
    ani = Toplevel()  # Crear una nueva ventana
    ani.geometry("600x419")  # Definir dimensiones de la ventana
    ani.resizable(width=NO,height=NO)  # Evitar que la ventana sea redimensionable
    ani.title("Animación")  # Establecer título de la ventana

    def MostrarImagen(imagen_path, duración):
        imagen = LoadImage(imagen_path)
        LabelImagen = Label(ani, image=imagen)
        LabelImagen.place(x=0, y=0)
        ani.update()  # Actualizar la ventana
        time.sleep(duración)  # Esperar la duración especificada en segundos
        LabelImagen.config(image=None)
        LabelImagen.pack()  # Empaquetar nuevamente el widget Label para reflejar los cambios
        ani.update()  # Actualizar la ventana para aplicar los cambios

    # Definimos una función llamada Mostrar
    def Mostrar():

      # Creamos una lista llamada image_paths que contiene las rutas de acceso a las imágenes de dinosaurios
  # Cada elemento de la lista es el nombre del archivo de imagen (por ejemplo, "dino0.jpg")
      image_paths = ["dino0.jpg", "dino1.jpg", "dino2.jpg", "dino3.jpg", "dino4.jpg", "dino6.jpg", "dino7.jpg", "dino8.jpg", "dino9.jpg", "dino10.jpg", "dino11.jpg", "dino12.jpg", "dino13.jpg", "dino14.jpg", "dino15.jpg", "dino16.jpg", "dino17.jpg", "dino18.jpg", "dino19.jpg", "dino20.jpg", "dino21.jpg", "dino22.jpg", "dino23.jpg"]

  # Creamos una lista llamada durations que define la duración de visualización de cada imagen
  # La lista durations tiene la misma longitud que la lista image_paths
  # Todos los valores de durations se establecen en 0.15 segundos usando la multiplicación por lista con [0.15]
      durations = [0.15] * len(image_paths)

  # Creamos una variable entera llamada i e la inicializamos en 0
  # Esta variable se usará como índice para recorrer la lista image_paths
      i = 0

  # Iniciamos un bucle while infinito (True)
      while True:
    # Llamamos a una función (que se supone que existe) llamada MostrarImagen
    # Esta función presumiblemente se encarga de mostrar la imagen especificada en la ruta image_paths[i]
    # durante el tiempo indicado en durations[i]
        MostrarImagen(image_paths[i], durations[i])

    # Incrementamos el índice i en 1
        i = (i + 1) % len(image_paths)

    # Usamos el módulo (%) para asegurarnos de que i siempre esté dentro del rango de la lista image_paths
    # Esto evita que el índice se salga de los límites de la lista

  # Llamamos a la función Mostrar() para iniciar la presentación
    Mostrar()

# Llamamos a la función ani.mainloop() para iniciar el bucle principal de la animación
#  (se asume que ani es una biblioteca o módulo para animaciones)
    ani.mainloop()

main = Tk()# se crea la ventana
main.title("Tarea Programada 1 - Adrian Monge") # titulo de la ventana
main.minsize(1024,693)# tamaño de ventana
main.resizable(width=NO,height=NO) # si se puede hacer pequña o grande
imagen = LoadImage("main_paper.jpg")# pone la imagen de fondo 
LabelFondo=Label(main, image=imagen) # etiqueta que va a contener la imagen
LabelFondo.place (x=0, y=0)# posicion de la imagen
menubar=Menu(main)# crea la barra del menu
menubar.add_command(label="Mostrar Divisores",command=mostrar_divisores)#abre la funcion mostrar_divisores
menubar.add_command(label="Tablas de un número",command=Tablas)#abre la funcion Tablas
menubar.add_command(label="About",command=Info)#abre la funcion Info
menubar.add_command(label="Animación",command=Animación)
main.config(menu=menubar)# agrega el menu
main.mainloop()



    
    
