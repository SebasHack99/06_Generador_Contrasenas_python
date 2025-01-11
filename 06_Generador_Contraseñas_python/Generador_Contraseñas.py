# Importamos las bibliotecas necesarias
import random  # La biblioteca random nos proporciona herramientas para generar números o elementos aleatorios.
import string  # La biblioteca string contiene constantes de cadenas útiles, como letras y números.
import tkinter as tk  # Tkinter es la biblioteca para crear interfaces gráficas en Python.


# Función para generar una contraseña
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """
    Esta función genera una contraseña segura basada en los criterios proporcionados.
    Los criterios incluyen longitud, inclusión de letras mayúsculas, números y caracteres especiales.

    Argumentos:
    length (int): La longitud de la contraseña a generar. El valor por defecto es 12.
    use_uppercase (bool): Si es True, incluye letras mayúsculas en la contraseña. El valor por defecto es True.
    use_numbers (bool): Si es True, incluye números en la contraseña. El valor por defecto es True.
    use_special_chars (bool): Si es True, incluye caracteres especiales en la contraseña. El valor por defecto es True.

    Retorna:
    str: La contraseña generada, que es una cadena de texto (string).
    """
    # Inicializamos la variable 'characters' con las letras minúsculas del abecedario.
    characters = string.ascii_lowercase  # 'ascii_lowercase' contiene 'abcdefghijklmnopqrstuvwxyz'

    # Si 'use_uppercase' es True, añadimos las letras mayúsculas al conjunto de caracteres.
    if use_uppercase:
        characters += string.ascii_uppercase  # 'ascii_uppercase' contiene 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Si 'use_numbers' es True, añadimos los números al conjunto de caracteres.
    if use_numbers:
        characters += string.digits  # 'digits' contiene '0123456789'

    # Si 'use_special_chars' es True, añadimos los caracteres especiales (símbolos) al conjunto de caracteres.
    if use_special_chars:
        characters += string.punctuation  # 'punctuation' contiene caracteres como "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Generamos una contraseña seleccionando caracteres aleatorios del conjunto 'characters'
    # Se hace esto 'length' veces (indicado por la longitud deseada de la contraseña).
    password = ''.join(
        random.choice(characters) for _ in range(length))  # 'random.choice(characters)' elige un carácter al azar

    return password  # Devolvemos la contraseña generada.


# Función para manejar la acción de generar una contraseña cuando se presiona el botón
def on_generate():
    """
    Esta función se ejecuta cuando el usuario presiona el botón 'Generar Contraseña'.
    Toma los valores proporcionados en la interfaz gráfica, genera una contraseña usando esos valores,
    y muestra la contraseña generada en la interfaz.

    Argumentos:
    Ninguno. Los valores se toman de los campos y casillas de la interfaz.
    """
    # Obtenemos el valor de la longitud de la contraseña desde el campo de texto 'entry_length'.
    length = int(entry_length.get())  # Convierte el texto a un número entero.

    # Obtenemos el valor de las casillas de verificación (checkboxes), que indican si el usuario quiere incluir ciertos tipos de caracteres.
    use_uppercase = var_uppercase.get()  # Esto devuelve True si el checkbox está marcado, False si no lo está.
    use_numbers = var_numbers.get()  # Lo mismo para la opción de incluir números.
    use_special_chars = var_special_chars.get()  # Lo mismo para la opción de incluir caracteres especiales.

    # Llamamos a la función 'generate_password' pasando los valores obtenidos de la interfaz gráfica.
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

    # Limpiamos el campo de texto donde se muestra la contraseña para eliminar cualquier valor previo.
    entry_password.delete(0, tk.END)  # '0' es el índice de inicio, 'tk.END' significa el final del texto.

    # Insertamos la nueva contraseña generada en el campo de texto para que el usuario la vea.
    entry_password.insert(0,
                          password)  # El primer argumento '0' indica la posición donde insertar el texto (al principio).


# Crear la ventana principal de la aplicación
root = tk.Tk()  # Creamos una ventana raíz con Tkinter. Esta será la ventana principal de nuestra aplicación.
root.title("Generador de Contraseñas Seguras")  # Establecemos el título de la ventana.

# Crear y configurar los controles de la interfaz gráfica

# Etiqueta para la longitud de la contraseña
label_length = tk.Label(root,
                        text="Longitud de la contraseña:")  # Creamos una etiqueta con un texto que guía al usuario.
label_length.pack()  # Añadimos la etiqueta a la ventana.

# Campo de texto para que el usuario ingrese la longitud de la contraseña
entry_length = tk.Entry(root)  # Creamos un campo de entrada de texto donde el usuario puede escribir.
entry_length.insert(0, "12")  # Establecemos un valor predeterminado para la longitud (12 caracteres).
entry_length.pack()  # Añadimos el campo de texto a la ventana.

# Casilla de verificación para incluir letras mayúsculas
var_uppercase = tk.BooleanVar(
    value=True)  # Creamos una variable que indica si se deben usar letras mayúsculas. Inicialmente es True.
checkbox_uppercase = tk.Checkbutton(root, text="Incluir letras mayúsculas",
                                    variable=var_uppercase)  # Creamos un checkbox.
checkbox_uppercase.pack()  # Añadimos el checkbox a la ventana.

# Casilla de verificación para incluir números
var_numbers = tk.BooleanVar(
    value=True)  # Creamos una variable que indica si se deben usar números. Inicialmente es True.
checkbox_numbers = tk.Checkbutton(root, text="Incluir números", variable=var_numbers)  # Creamos un checkbox.
checkbox_numbers.pack()  # Añadimos el checkbox a la ventana.

# Casilla de verificación para incluir caracteres especiales
var_special_chars = tk.BooleanVar(
    value=True)  # Creamos una variable que indica si se deben usar caracteres especiales. Inicialmente es True.
checkbox_special_chars = tk.Checkbutton(root, text="Incluir símbolos especiales",
                                        variable=var_special_chars)  # Creamos un checkbox.
checkbox_special_chars.pack()  # Añadimos el checkbox a la ventana.

# Botón para generar la contraseña
button_generate = tk.Button(root, text="Generar Contraseña",
                            command=on_generate)  # Creamos un botón. Cuando se presiona, ejecuta la función 'on_generate'.
button_generate.pack()  # Añadimos el botón a la ventana.

# Etiqueta para mostrar la contraseña generada
label_password = tk.Label(root,
                          text="Contraseña Generada:")  # Creamos una etiqueta que indica dónde se mostrará la contraseña.
label_password.pack()  # Añadimos la etiqueta a la ventana.

# Campo de texto para mostrar la contraseña generada
entry_password = tk.Entry(root)  # Creamos un campo de texto para mostrar la contraseña generada.
entry_password.pack()  # Añadimos el campo de texto a la ventana.

# Iniciar la aplicación
root.mainloop()  # Esta línea ejecuta la ventana y mantiene la aplicación abierta hasta que el usuario decida cerrarla.
