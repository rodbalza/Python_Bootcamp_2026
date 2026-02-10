from io import open

texto = 'mas lineas \nmuchas mas lineas '

# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('fichero2.txt','w')

# Escribimos el texto
fichero.write(texto)

# Cerramos el fichero
fichero.close()