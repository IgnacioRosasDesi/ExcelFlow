from pathlib import Path

"""
Configuración general de ExcelFlow.
"""

APP_NAME = "ExcelFlow"
VERSION = "1.0.0"

# Carpeta raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carpetas principales
DATA_FOLDER = BASE_DIR / "data"

# Carpeta de logs
LOG_FOLDER = DATA_FOLDER / "logs"

INPUT_FOLDER = DATA_FOLDER / "entrada"
OUTPUT_FOLDER = DATA_FOLDER / "salida"

EXPORT_FILENAME = "resultado"

# Nombre base de los archivos de log
LOG_FILENAME = "excelflow"

DEFAULT_EXPORT_FORMAT = ".xlsx"

SUPPORTED_EXTENSIONS = [
    ".xlsx",
    ".csv"
]