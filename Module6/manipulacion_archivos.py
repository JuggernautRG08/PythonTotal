# Abrir el archivo en modo escritura
archivo = open("C:\PythonTotal\Module6\Archivos\prueba.txt", "a")

# Lista de valores a escribir en el archivo
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Crear una cadena con los elementos de la lista separados por un tabulador
linea = "\t".join(registro_ultima_sesion) + "\n"

# Escribir la línea en el archivo
archivo.writelines(linea)

# Cerrar el archivo en modo escritura
archivo.close()

# Abrir el archivo en modo lectura
archivo = open("registro.txt", "r")

# Leer y mostrar el contenido completo del archivo
contenido = archivo.read()
print(contenido)

# Cerrar el archivo en modo lectura
archivo.close()
