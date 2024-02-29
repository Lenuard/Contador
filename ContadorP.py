import os
import re
class contador:
    def __init__(self, carpeta, palabra):
        self.carpeta = carpeta
        self.palabra = palabra
        self.totalPalabras = 0

    """def contar_en_archivo(self, archivo):
        try:
            with open(archivo, 'r') as file:
                contenido = file.read().lower()
                cantidad = contenido.count(self.palabra.lower())
                return cantidad
        except Exception:
            print('No se pudo leer el archivo o no es un archivo con las extensiones permitidas')
            return 0"""

    def contar_en_archivo(self, archivo):
        cantidad = 0
        try:
            with open(archivo, 'r') as file:
                contenido = file.read()
                contenido_sin_caracteres = re.sub(r'[,();]', ' ', contenido)
                lista_palabras = contenido_sin_caracteres.split()

                print(lista_palabras)

                for palabra in lista_palabras:
                    if self.palabra.lower() == palabra.lower():
                        cantidad +=1

                return cantidad
        except Exception:
            print('No se pudo leer el archivo o no es un archivo con las extensiones permitidas')
            return 0

    def contar_en_carpeta(self):
        extensiones = ['.txt', '.xml', '.json', '.csv']

        if not os.path.exists(self.carpeta):
            print("La carpeta no existe.")
            return

        for archivo in os.listdir(self.carpeta):
            ruta_archivo = self.carpeta +'\\'+ archivo

            for i in extensiones:
                if os.path.isfile(ruta_archivo) and ruta_archivo.lower().endswith(i):
                    cantidad_en_archivo = self.contar_en_archivo(ruta_archivo)
                    self.totalPalabras += cantidad_en_archivo
                else:
                    print("No hay archivos de texto")

        print('Total en la carpeta: ', self.totalPalabras, ' veces')


contador = contador('C:\\Users\\57311\\Desktop\\IngSoftware\\Tarea1\\pruebas2', 'foto')
contador.contar_en_carpeta()

"""contador = contador('./C:/Users/57311/Desktop/IngSoftware/Tarea1/pruebas1', 'arar')
archivo = 'C:\\Users\\57311\\Desktop\\IngSoftware\\Tarea1\\pruebas1\\Texto3.txt'
print(contador.contar_en_archivo(archivo))"""





