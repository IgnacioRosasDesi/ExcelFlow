# 🚀 ExcelFlow

> Automatiza la importación, limpieza y exportación de archivos Excel y CSV.

ExcelFlow es una herramienta desarrollada en Python que permite procesar grandes cantidades de datos provenientes de múltiples archivos de Excel y CSV, unificarlos, limpiarlos automáticamente y generar un archivo consolidado listo para utilizar.

El objetivo del proyecto es reducir tareas manuales repetitivas realizadas en Excel y facilitar el trabajo de analistas de datos, empresas y equipos administrativos.

---

# ✨ Características

Actualmente ExcelFlow permite:

- ✅ Importar archivos Excel (.xlsx)
- ✅ Importar archivos CSV (.csv)
- ✅ Detectar automáticamente el tipo de archivo
- ✅ Combinar múltiples archivos en un único DataFrame
- ✅ Eliminar filas completamente vacías
- ✅ Eliminar registros duplicados
- ✅ Exportar automáticamente el resultado
- ✅ Generar nombres únicos con fecha y hora
- ✅ Arquitectura modular preparada para crecer

---

# 🛠 Tecnologías utilizadas

- Python 3
- Pandas
- Pathlib
- Git
- GitHub
- Visual Studio Code

---

# 📁 Estructura del proyecto

```
ExcelFlow/

├── data/
│   ├── entrada/
│   └── salida/
│
├── src/
│   ├── config.py
│   ├── excelflow.py
│   ├── exportador.py
│   ├── importador.py
│   ├── limpiador.py
│   ├── main.py
│   ├── procesador.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 Instalación

Clonar el repositorio

```bash
git clone https://github.com/IgnacioRosasDesi/ExcelFlow.git
```

Ingresar al proyecto

```bash
cd ExcelFlow
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución

Ubicarse en la carpeta `src`

```bash
cd src
```

Ejecutar

```bash
py main.py
```

---

# 📂 Archivos de entrada

Colocar los archivos dentro de:

```
data/entrada/
```

ExcelFlow detectará automáticamente si son archivos Excel o CSV.

---

# 📤 Resultado

Los archivos procesados se exportan automáticamente en:

```
data/salida/
```

Cada ejecución genera un nombre único basado en la fecha y hora para evitar sobrescribir resultados anteriores.

---

# 🧱 Arquitectura

ExcelFlow está diseñado siguiendo una arquitectura modular basada en responsabilidades.

```
ExcelFlow
│
├── Importador
├── Procesador
├── Limpiador
├── Exportador
└── Configuración
```

Cada módulo realiza una única función, facilitando el mantenimiento y la incorporación de nuevas características.

---

# 📅 Roadmap

## ✅ Versión 1.0

- Importación de Excel
- Importación de CSV
- Unión de DataFrames
- Eliminación de duplicados
- Eliminación de filas vacías
- Exportación automática

## 🚧 Próximamente

- Limpieza inteligente de texto
- Eliminación de espacios
- Normalización de columnas
- Conversión automática de fechas
- Reportes de limpieza
- Exportación a Google Sheets
- Interfaz gráfica
- Integración con bases de datos

---

# 👨‍💻 Autor

**Ignacio**

Ingeniero en Informática | Python | Automatización | Procesamiento de Datos

LinkedIn:
https://www.linkedin.com/in/ignacio-rosas-sanhueza-99162023a/

GitHub:
https://github.com/IgnacioRosasDesi

---

# 📄 Licencia

Este proyecto se encuentra bajo la licencia MIT.