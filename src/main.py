from excelflow import ExcelFlow


def main():

    try:

        app = ExcelFlow()

        app.ejecutar()

    except Exception as error:

        print("\n❌ Error inesperado")
        print(error)


if __name__ == "__main__":
    main()