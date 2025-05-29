# Tarea Programada 1: Interfaces Gráficas y Recursividad

## 📋 Descripción del Proyecto

Este proyecto es una aplicación gráfica desarrollada con Python y Tkinter que implementa conceptos de recursividad en un entorno visual. La aplicación incluye varias funcionalidades interactivas que permiten al usuario realizar operaciones matemáticas, visualizar información personal y disfrutar de contenido multimedia.

## ✨ Características principales

- ✅ Cálculo de divisores de un número
- ✅ Generación de tablas de multiplicar
- ✅ Sección "About" con información personal
- ✅ Animación interactiva
- ✅ Reproducción y pausa de audio

## 🚀 Instalación

### Prerrequisitos

```bash
Python 3.x
Pillow (PIL)
pygame
```

### Pasos de instalación

```bash
# Clonar el repositorio (o descargar los archivos)
git clone https://github.com/tu_usuario/tarea-programada-1.git

# Acceder al directorio
cd tarea-programada-1

# Instalar dependencias
pip install pillow pygame
```

## 💻 Uso

Para ejecutar la aplicación, simplemente ejecute el archivo principal:

```bash
python main.py
```

La aplicación mostrará una ventana principal con un menú en la parte superior que le permitirá acceder a las diferentes funcionalidades:

- **Mostrar Divisores**: Calcula todos los divisores exactos de un número entero
- **Tablas de un número**: Muestra las tablas de multiplicar de un número del 1 al 10
- **About**: Muestra información personal del estudiante
- **Animación**: Despliega una animación creativa

## 🔧 Estructura del proyecto

```
tarea-programada-1/
│
├── main.py                # Archivo principal con el código de la aplicación
│
└── Resources/             # Carpeta con recursos multimedia
    ├── main_paper.jpg     # Imagen de fondo principal
    ├── RPO-300x171.jpg    # Imagen de película
    ├── Selfie1.jpg        # Foto del estudiante
    ├── Family1.jpg        # Foto familiar
    ├── best1.jpg          # Imagen adicional
    ├── dino0.jpg          # Imágenes para la animación
    ├── dino1.jpg
    ├── ...
    └── Casey Edwards & Victor Borba – Vacant Surrender [Official Audio].wav  # Archivo de audio
```

## 📝 Detalles de implementación

### Funcionalidad de divisores

La función `Calcular_Divisores()` calcula todos los divisores exactos de un número y los muestra en una ventana de mensaje.

```python
def Calcular_Divisores(numero):
  divisores = [] 
  
  if numero == 0:
    return messagebox.showwarning("Error", "Ingrese un número distinto de 0") 
  
  for i in range(1, int(numero ** 0.5) + 1):
    if numero % i == 0:
      divisores.append(i)
      if i != numero // i:
        divisores.append(numero // i)
        
  # Mostrar resultados...
```

### Tablas de multiplicar

La función `Tablas_Num()` genera las tablas de multiplicar del 1 al 10 para un número dado:

```python
def Tablas_Num(num):
  res = ""
  for i in range(1, 11):
    res += f"{num} x {i} = {num * i}\n"
  messagebox.showinfo("Resultado", res)
```

### Sistema de animación

La animación se implementa mostrando una secuencia de imágenes con un retardo entre ellas:

```python
def Mostrar():
  image_paths = ["dino0.jpg", "dino1.jpg", ..., "dino23.jpg"]
  durations = [0.15] * len(image_paths)
  
  i = 0
  while True:
    MostrarImagen(image_paths[i], durations[i])
    i = (i + 1) % len(image_paths)
```

## 🔍 Implementación de recursividad

Aunque la tarea solicitaba implementar recursividad, la solución actual utiliza enfoques iterativos. A continuación se presentan propuestas para implementar versiones recursivas de las funcionalidades:

### Versión recursiva para calcular divisores

```python
def calcular_divisores_recursivo(numero, divisor=1, divisores=None):
    if divisores is None:
        divisores = []
    
    if divisor > numero:
        return divisores
    
    if numero % divisor == 0:
        divisores.append(divisor)
    
    return calcular_divisores_recursivo(numero, divisor + 1, divisores)
```

### Versión recursiva para tablas de multiplicar

```python
def tabla_multiplicar_recursiva(num, multiplicador=1, resultado=""):
    if multiplicador > 10:
        return resultado
    
    resultado += f"{num} x {multiplicador} = {num * multiplicador}\n"
    return tabla_multiplicar_recursiva(num, multiplicador + 1, resultado)
```

## 📝 Aspectos a mejorar

1. **Implementación de recursividad**: La tarea solicitaba usar recursividad para la lógica, pero la implementación actual usa enfoques iterativos.

2. **Manejo de errores**: Añadir más validaciones para entradas de usuario.

3. **Organización del código**: Separar la lógica en módulos diferentes para mejor mantenimiento.

4. **Optimización del rendimiento**: La animación podría mejorar su eficiencia utilizando técnicas más avanzadas.

## 📄 Licencia

Licencia Educativa - Este proyecto fue desarrollado con fines educativos como parte de la asignatura de Introducción a la Programación.

Desarrollado por: Adrián Monge Mairena
