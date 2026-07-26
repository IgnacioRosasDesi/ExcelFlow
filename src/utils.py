from pathlib import Path

from config import INPUT_FOLDER, OUTPUT_FOLDER


def verificar_directorios():

    carpetas = [
        INPUT_FOLDER,
        OUTPUT_FOLDER
    ]

    for carpeta in carpetas:
        Path(carpeta).mkdir(parents=True, exist_ok=True)

    print("✔ Directorios verificados.")