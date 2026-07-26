from pathlib import Path
import pandas as pd


class Importador:

    EXTENSIONES_COMPATIBLES = [
        ".xlsx",
        ".csv"
    ]

    def __init__(self, carpeta):

        self.carpeta = Path(carpeta)

    def buscar_archivos(self):

        archivos = []

        for archivo in self.carpeta.iterdir():

            if archivo.is_file():

                if archivo.suffix.lower() in self.EXTENSIONES_COMPATIBLES:

                    archivos.append(archivo)

        return archivos

    def leer_archivo(self, archivo):

        extension = archivo.suffix.lower()

        if extension == ".xlsx":
            return self.leer_excel(archivo)

        elif extension == ".csv":
            return self.leer_csv(archivo)

        else:
            raise ValueError("Formato no soportado.")

    def leer_excel(self, archivo):

        return pd.read_excel(archivo)

    def leer_csv(self, archivo):

        return pd.read_csv(archivo)