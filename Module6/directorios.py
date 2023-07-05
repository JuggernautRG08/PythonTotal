import os
from pathlib import Path

# ruta = os.getcwd()
# ruta2 = os.chdir('C:\TFS_GNV\otro_texto.txt')

# print(ruta)
# print(open(ruta2, 'r').read())

# carpeta = Path('C:/TFS_GNV/')
# archivo= carpeta/' otro_texto.txt'
# mi_archivo = open(archivo, 'r').read()
# print(mi_archivo)
# mi_archivo.close()

folder= Path("C:\TFS_GNV\otro_texto.txt")
if not os.path.exists(folder):
    print("The file does not exist")
else:
    print("The file exists")
