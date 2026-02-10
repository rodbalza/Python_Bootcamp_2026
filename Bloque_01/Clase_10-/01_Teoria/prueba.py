from io import open

texto = ''

# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('registro.txt','w')

# Escribimos el texto
fichero.write(texto)

# Cerramos el fichero
fichero.close()