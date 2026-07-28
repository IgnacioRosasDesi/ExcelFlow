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
        Genera un nombre base único utilizando
        la fecha y hora actual.
        """

        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        return self.output_folder / f"{EXPORT_FILENAME}_{fecha}"

    def _generar_archivo(self, extension):
        """
        Genera la ruta completa del archivo
        con la extensión indicada.

        Args:
            extension (str): Extensión del archivo.

        Returns:
            pathlib.Path
        """

        return self.generar_nombre_archivo().with_suffix(extension)

    def exportar_excel(self, dataframe):
        """
        Exporta un DataFrame a Excel.

        Returns:
            str: Nombre del archivo generado.
        """

        archivo = self._generar_archivo(".xlsx")

        dataframe.to_excel(
            archivo,
            index=False
        )

        print(f"\n📁 Archivo exportado: {archivo.name}")

        return archivo.name

    def exportar_csv(self, dataframe):
        """
        Exporta un DataFrame a CSV.

        Returns:
            str: Nombre del archivo generado.
        """

        archivo = self._generar_archivo(".csv")

        dataframe.to_csv(
            archivo,
            index=False,
            encoding="utf-8-sig"
        )

        print(f"\n📁 Archivo exportado: {archivo.name}")

        return archivo.name

    def exportar(self, dataframe):
        """
        Exporta el DataFrame utilizando el formato
        definido en DEFAULT_EXPORT_FORMAT.

        Returns:
            str: Nombre del archivo generado.
        """

        if DEFAULT_EXPORT_FORMAT == ".xlsx":

            return self.exportar_excel(dataframe)

        elif DEFAULT_EXPORT_FORMAT == ".csv":

            return self.exportar_csv(dataframe)

        else:

            raise ValueError(
                f"Formato no soportado: {DEFAULT_EXPORT_FORMAT}"
            )