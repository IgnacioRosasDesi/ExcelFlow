import pandas as pd


class Procesador:
    """
    Se encarga de procesar y combinar los datos importados.
    """

    def unir_dataframes(self, dataframes):
        """
        Une una lista de DataFrames en uno solo.

        Args:
            dataframes (list): Lista de DataFrames.

        Returns:
            pandas.DataFrame: DataFrame unificado.
        """

        if len(dataframes) == 0:
            return pd.DataFrame()

        return pd.concat(
            dataframes,
            ignore_index=True
        )