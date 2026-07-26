from pathlib import Path


def verificar_directorios():
    """
    Crea las carpetas necesarias si no existen.
    """

    carpetas = [
        "data/entrada",
        "data/salida"
    ]

    for carpeta in carpetas:
        Path(carpeta).mkdir(parents=True, exist_ok=True)

    print("✔ Directorios verificados.")