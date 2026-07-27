from datetime import datetime

from config import (
    OUTPUT_FOLDER,
    EXPORT_FILENAME,
    DEFAULT_EXPORT_FORMAT
)


class Exportador:
    """
    Se encarga de exportar los datos procesados.
    """

    def __init__(self):

        self.output_folder = OUTPUT_FOLDER

    def generar_nombre_archivo(self):
        """
        Genera un nombre único basado en fecha y hora.
        """

        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        return self.output_folder / f"{EXPORT_FILENAME}_{fecha}"

    def exportar_excel(self, dataframe):

        archivo = self.generar_nombre_archivo().with_suffix(".xlsx")

        dataframe.to_excel(
            archivo,
            index=False
        )

        print(f"\n📁 Archivo exportado: {archivo.name}")

    def exportar_csv(self, dataframe):

        archivo = self.generar_nombre_archivo().with_suffix(".csv")

        dataframe.to_csv(
            archivo,
            index=False,
            encoding="utf-8-sig"
        )

        print(f"\n📁 Archivo exportado: {archivo.name}")

    def exportar(self, dataframe):
        """
        Decide automáticamente el formato de exportación.
        """

        if DEFAULT_EXPORT_FORMAT == ".xlsx":

            self.exportar_excel(dataframe)

        elif DEFAULT_EXPORT_FORMAT == ".csv":

            self.exportar_csv(dataframe)

        else:

            raise ValueError(
                f"Formato no soportado: {DEFAULT_EXPORT_FORMAT}"
            )