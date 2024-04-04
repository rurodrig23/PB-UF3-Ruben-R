import os

ruta_fitxer = input("Introduïu la ruta del fitxer: ")

fd = open("ruta_fitxer","r")

os.rename(fd,ruta_fitxer)

print(fd)
