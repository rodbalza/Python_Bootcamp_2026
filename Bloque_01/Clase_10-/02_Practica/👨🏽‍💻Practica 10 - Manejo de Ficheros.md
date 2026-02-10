# 👨🏽‍💻Practica 10 - Manejo de Ficheros

<aside>
💡

# Instrucciones

**Entregar los ejercicios en uno o varios `archivos.py` o en un notebook de Jupyter (`.ipynb`).** 

</aside>

1. Resolver los ejercicios propuestos y los casos de uso propuestos de la **clase 10**
2. Crear un script llamado **personas.py** que lea los datos de un fichero de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. Luego rocorre las personas de la lista y paracada una muestra de forma amigable todos sus campos. El fichero de texto se denominará **personas.txt** y tendrá el siguiente contenido en texto plano (créalo previamente):
    
    ```python
    1;Carlos;Pérez;05/01/1989
    2;Manuel;Heredia;26/12/1973
    3;Rosa;Campos;12/06/1961
    4;David;García;25/07/2006
    ```
    
    Los campos del diccionario serán por orden: **id**, **nombre**, **apellido** y **nacimiento**.
    
3. Crear un script llamado **contador.py** que realice varias tareas sobre un fichero llamado **contador.txt** que almacenará un contador de visitas (será un número):
- Nuestro script trabajará sobre el fichero **contador.txt**. Si el fichero no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
- Luego a partir de un argumento:
    - Si se envía el argumento **inc**, se incrementará el contador en uno y se mostrará por pantalla.
    - Si se envía el argumento **dec**, se decrementará el contador en uno y se mostrará por pantalla.
    - Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
- Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
- Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: **Error: Fichero corrupto.**