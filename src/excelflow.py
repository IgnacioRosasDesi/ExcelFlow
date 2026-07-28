import time
from config import APP_NAME, VERSION, INPUT_FOLDER
from utils import verificar_directorios
from importador import Importador
from procesador import Procesador
from limpiador import Limpiador
from exportador import Exportador
from reporte import Reporte
from logger import Logger


class ExcelFlow:
    """
    Clase principal de la aplicación.
    Coordina todo el flujo de trabajo.
    """

    def __init__(self):
        self.importador = Importador(INPUT_FOLDER)
        self.procesador = Procesador()
        self.limpiador = Limpiador()
        self.exportador = Exportador()
        self.reporte = Reporte()
        self.logger = Logger()

    def ejecutar(self):

        print("=" * 50)
        print(f"      {APP_NAME} v{VERSION}")
        print("=" * 50)

        try:
            inicio = time.perf_counter()

            verificar_directorios()
            
            self.logger.escribir("ExcelFlow iniciado.")

            self.logger.escribir("Directorios verificados.")

            dataframes = self.importador.importar()

            self.logger.escribir(
                f"Archivos importados: {len(dataframes)}"
            )

            df_final = self.procesador.unir_dataframes(dataframes)

            filas_originales = len(df_final)

            df_final = self.limpiador.limpiar(df_final)

            estadisticas = self.limpiador.obtener_estadisticas()

            archivo_generado = self.exportador.exportar(df_final)

            self.logger.escribir(
                f"Archivo generado: {archivo_generado}"
            )

            fin = time.perf_counter()

            tiempo_total = fin - inicio

            self.reporte.mostrar(
                archivos=len(dataframes),
                filas_originales=filas_originales,
                filas_finales=len(df_final),
                estadisticas=estadisticas,
                archivo_generado=archivo_generado,
                tiempo=tiempo_total
            )
            self.logger.escribir("Proceso finalizado correctamente.")

            print("\n✔ Sistema finalizado correctamente.")

        except Exception as e:

            self.logger.escribir(
                f"ERROR: {e}"
            )

            print("\n❌ Error inesperado.")
            print(e)