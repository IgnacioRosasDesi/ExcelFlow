from config import APP_NAME, VERSION, INPUT_FOLDER
from utils import verificar_directorios
from importador import Importador
from procesador import Procesador


def main():

    print("=" * 50)
    print(f"      {APP_NAME} v{VERSION}")
    print("=" * 50)

    verificar_directorios()

    importador = Importador(INPUT_FOLDER)

    dataframes = importador.importar()

    print(f"\nSe importaron {len(dataframes)} archivo(s).")

    procesador = Procesador()

    df_final = procesador.unir_dataframes(dataframes)

    print(f"Filas totales: {len(df_final)}")

    print("\n✔ Sistema finalizado correctamente.")


if __name__ == "__main__":
    main()