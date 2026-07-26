from pathlib import Path
import pandas as pd

from config import SUPPORTED_EXTENSIONS


class Importador:
    """
    Se encarga de buscar e importar archivos compatibles.
    """

    def __init__(self, carpeta):
        self.carpeta = Path(carpeta)

    def buscar_archivos(self):
        """
        Devuelve una lista con todos los archivos compatibles.
        """

        if not self.carpeta.exists():
            raise FileNotFoundError(
                f"La carpeta '{self.carpeta}' no existe."
            )

        archivos = []

        for archivo in self.carpeta.iterdir():

            if archivo.is_file():

                if archivo.suffix.lower() in SUPPORTED_EXTENSIONS:

                    archivos.append(archivo)

        return archivos

    def leer_excel(self, archivo):
        """
        Lee un archivo Excel y devuelve un DataFrame.
        """
        return pd.read_excel(archivo)

    def leer_csv(self, archivo):
        """
        Lee un archivo CSV y devuelve un DataFrame.
        """
        return pd.read_csv(archivo)

    def leer_archivo(self, archivo):
        """
        Detecta automáticamente el tipo de archivo.
        """

        extension = archivo.suffix.lower()

        if extension == ".xlsx":
            return self.leer_excel(archivo)

        elif extension == ".csv":
            return self.leer_csv(archivo)

        raise ValueError(f"Formato no soportado: {extension}")

    def importar(self):
        """
        Lee todos los archivos encontrados y devuelve
        una lista de DataFrames.
        """

        dataframes = []

        archivos = self.buscar_archivos()

        for archivo in archivos:

            print(f"📄 Importando: {archivo.name}")

            df = self.leer_archivo(archivo)

            dataframes.append(df)

        return dataframes