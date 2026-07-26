from config import APP_NAME, VERSION, INPUT_FOLDER
from utils import verificar_directorios
from importador import Importador
from procesador import Procesador


class ExcelFlow:
    """
    Clase principal de la aplicación.
    Coordina todo el flujo de trabajo.
    """

    def __init__(self):
        self.importador = Importador(INPUT_FOLDER)
        self.procesador = Procesador()

    def ejecutar(self):
        """
        Ejecuta el flujo completo de ExcelFlow.
        """

        print("=" * 50)
        print(f"      {APP_NAME} v{VERSION}")
        print("=" * 50)

        verificar_directorios()

        dataframes = self.importador.importar()

        print(f"\nSe importaron {len(dataframes)} archivo(s).")

        df_final = self.procesador.unir_dataframes(dataframes)

        print(f"Filas totales: {len(df_final)}")

        print("\n✔ Sistema finalizado correctamente.")