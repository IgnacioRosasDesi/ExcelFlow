from utils import verificar_directorios
from importador import Importador


def main():

    print("=" * 50)
    print("          ExcelFlow v1.0")
    print("=" * 50)

    verificar_directorios()

    importador = Importador("data/entrada")

    archivos = importador.buscar_archivos()

    print(f"\nArchivos encontrados: {len(archivos)}")

    for archivo in archivos:

        print(f"📄 {archivo.name}")

    print("\nSistema iniciado correctamente.")


if __name__ == "__main__":
    main()