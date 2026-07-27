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
        df = self.eliminar_duplicados(df)

        return df