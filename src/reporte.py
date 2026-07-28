from datetime import datetime


class Reporte:
    """
    Se encarga de generar el reporte del proceso.
    """

    def __init__(self):

        self.fecha = datetime.now()

    def mostrar(
        self,
        archivos,
        filas_originales,
        filas_finales,
        estadisticas,
        archivo_generado=None
    ):

        print("\n" + "=" * 50)
        print("           REPORTE EXCELFLOW")
        print("=" * 50)

        print(f"Fecha                 : {self.fecha.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Archivos procesados   : {archivos}")
        print(f"Filas originales      : {filas_originales}")
        print(f"Filas finales         : {filas_finales}")

        print(f"Filas vacías          : {estadisticas['filas_vacias']}")
        print(f"Duplicados            : {estadisticas['duplicados']}")
        print(f"Espacios corregidos   : {estadisticas['espacios']}")
        print(f"Columnas normalizadas : {estadisticas['columnas']}")

        if archivo_generado:

            print(f"Archivo generado      : {archivo_generado}")

        print("=" * 50)