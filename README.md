GENERADOR DE CONTRASEÑAS SEGURAS

Este proyecto en Python es un Generador de Contraseñas Seguras que permite a los usuarios crear contraseñas fuertes basadas en su preferencia de longitud y tipo de caracteres (mayúsculas, minúsculas, números y símbolos). La aplicación tiene una interfaz gráfica simple y amigable para el usuario, creada con la librería tkinter, y proporciona la capacidad de generar contraseñas aleatorias con una sola acción.

Descripción
Este generador de contraseñas te permite:

Especifique la longitud de la contraseña.
- Elija qué tipo de caracteres incluir en la contraseña (mayúsculas, minúsculas, números, símbolos).
- Ver la contraseña generada en tiempo real.
- Reiniciar los campos para empezar desde cero.
- Librerías utilizadas

Este proyecto utiliza las siguientes librerías:

1.tkinter

- Es la librería estándar en Python para crear interfaces gráficas de usuario (GUI). Se utiliza para crear ventanas, botones, cuadros de texto y mostrar mensajes.
- Para crear la ventana y los componentes gráficos como botones y etiquetas.
- messagebox: Para mostrar mensajes emergentes.

2.random

- Es una librería que permite realizar operaciones aleatorias, como seleccionar elementos aleatoriamente de una lista (como letras, números y símbolos) para generar una contraseña única cada vez.
- random.choice(): Elige un elemento aleatorio de una lista o secuencia.

3.string
- Contiene secuencias predefinidas de caracteres que pueden ser utilizados para la generación de contraseñas, como las letras mayúsculas, minúsculas, dígitos y símbolos.
- string.ascii_uppercase:Letras mayúsculas (AZ).
- string.ascii_lowercase:Letras minúsculas (az).
- string.digits:Numeros (0-9).
- string.punctuation: Símbolos (p. ej. !, , @, #).

VARIABLES PRINCIPALES

1.length_entry
Un cuadro de texto donde el usuario puede ingresar la longitud deseada para la contraseña. Su valor es extraído y utilizado para definir la longitud de la contraseña generada.

2. uppercase_var, lowercase_var, numbers_var,special_var
Son variables que almacenan el estado de las casillas de verificación (checkboxes) que permiten al usuario seleccionar si desea incluir mayúsculas, minúsculas, números y símbolos, respectivamente. Estas variables determinan qué tipo de caracteres se usarán en la contraseña generada.

3.characters
Es una cadena vacía que se llena con los caracteres que el usuario selecciona en las casillas. Es el "almacén" de todos los caracteres que se usarán para formar la contraseña.

4.password
Es la contraseña generada. Contiene la cadena final que el robot crea a partir de los caracteres seleccionados y la longitud especificada.

FUNCIONES

1.generate_password()
- Esta es la función principal que genera la contraseña:

  * Obtiene la longitud de la contraseña del cuadro de texto length_entry.
  * Llene la variable characterscon los caracteres apropiados según las casillas de verificación activadas.
  * Utilice un bucle para seleccionar aleatoriamente caracteres de la bolsa charactersy generar la contraseña.
  * Muestra la contraseña generada en la ventana mediante result_label.

2.reset_fields()
- Esta función reinicia todos los campos de entrada, desmarcando las casillas de verificación, borrando el cuadro de longitud y limpiando el resultado de la contraseña generada. Permite al usuario empezar de nuevo fácilmente.

* Interfaz Gráfica
- La interfaz gráfica está diseñada para ser sencilla y amigable. Tiene los siguientes elementos:

Campo de entrada para la longitud de la contraseña : El usuario puede escribir el número de caracteres que debe tener la contraseña.

Casillas de verificación para seleccionar si se quieren incluir mayúsculas, minúsculas, números y símbolos.

Botón "Generar Contraseña" : Al hacer clic, el botón genera la contraseña obtenida en las selecciones.

Etiqueta para mostrar la contraseña generada : Aquí es donde aparece la contraseña una vez generada.

Botón "Reiniciar" : Limpia los campos y permite empezar de nuevo.
