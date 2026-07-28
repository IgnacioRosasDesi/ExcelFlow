from datetime import datetime

from config import LOG_FOLDER, LOG_FILENAME


class Logger:

    def __init__(self):

        # Asegura que exista la carpeta de logs
        LOG_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        fecha = datetime.now().strftime("%Y-%m-%d")

        self.archivo = LOG_FOLDER / f"{LOG_FILENAME}_{fecha}.log"
        
    def escribir(self, mensaje):
        """
        Escribe un mensaje en el archivo de log.
        """

        hora = datetime.now().strftime("%H:%M:%S")

        linea = f"[{hora}] {mensaje}\n"

        with open(
            self.archivo,
            "a",
            encoding="utf-8"
        ) as log:

            log.write(linea)