from config import APP_NAME, VERSION, INPUT_FOLDER
from utils import verificar_directorios
from importador import Importador
from procesador import Procesador
from limpiador import Limpiador
from exportador import Exportador


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

    def ejecutar(self):

        print("=" * 50)
        print(f"      {APP_NAME} v{VERSION}")
        print("=" * 50)

        verificar_directorios()

        dataframes = self.importador.importar()

        print(f"\nSe importaron {len(dataframes)} archivo(s).")

        df_final = self.procesador.unir_dataframes(dataframes)

        filas_originales = len(df_final)

        df_final = self.limpiador.limpiar(df_final)

        estadisticas = self.limpiador.obtener_estadisticas()

        print("\n===== RESUMEN =====")

        print(f"Filas originales : {filas_originales}")
        print(f"Filas finales    : {len(df_final)}")
        print(f"Filas vacías     : {estadisticas['filas_vacias']}")
        print(f"Duplicados       : {estadisticas['duplicados']}")

        self.exportador.exportar(df_final)

        print("\n✔ Sistema finalizado correctamente.")