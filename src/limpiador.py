import pandas as pd


class Limpiador:
    """
    Se encarga de limpiar y normalizar los datos.
    """

    def __init__(self):

        self.estadisticas = {
            "filas_vacias": 0,
            "duplicados": 0,
            "espacios": 0,
            "columnas": 0
        }

    def eliminar_filas_vacias(self, df):
        """
        Elimina filas completamente vacías.
        """

        filas_antes = len(df)

        df = df.dropna(how="all")

        self.estadisticas["filas_vacias"] = filas_antes - len(df)

        return df

    def eliminar_duplicados(self, df):
        """
        Elimina filas duplicadas.
        """

        filas_antes = len(df)

        df = df.drop_duplicates()

        self.estadisticas["duplicados"] = filas_antes - len(df)

        return df

    def obtener_estadisticas(self):
        """
        Devuelve las estadísticas de limpieza.
        """

        return self.estadisticas
    def limpiar(self, df):
        """
        Ejecuta todas las tareas de limpieza disponibles.
        """

        df = self.eliminar_filas_vacias(df)
        df = self.normalizar_columnas(df)
        df = self.quitar_espacios(df)
        df = self.eliminar_duplicados(df)

        return df

    def quitar_espacios(self, df):
        """
        Elimina espacios al inicio y 
        al final de todas las columnas de texto
        """
        correcciones = 0

        for columna in df.select_dtypes(include="object").columns:

            antes = df[columna].copy()

            df[columna] = df[columna].str.strip()

            correcciones += (antes != df[columna]).sum()

        self.estadisticas["espacios"] = correcciones

        return df
    
    def normalizar_columnas(self, df):
        """
        Normaliza los nombres de las columnas.
        """

        columnas_originales = list(df.columns)

        nuevas_columnas = []

        cambios = 0

        for columna in columnas_originales:

            nueva = (
                str(columna)
                .strip()
                .lower()
                .replace(" ", "_")
            )

            if nueva != columna:
                cambios += 1

            nuevas_columnas.append(nueva)

        df.columns = nuevas_columnas

        self.estadisticas["columnas"] = cambios

        return df