# Source calc

Calculadora de fuentes para realizar presentaciones con fuentes de información.

Basada en la calculador realizada por el equipo <completar>

# Uso
Crear una copia del archivo **source_manifest-example.csv**
y renombrarlo como: **source_manifest.csv**

y luego ejecutar el script así:

```bash
python3 main.py
```

Esto parseará y el archivo source_manifest.csv y generará un archivo html para ver las fuentes. Este archivo se puede imprimir y modificar de ser necesario.

Se le puede pasar otro nombre de archivo de entrada o path y un nombre diferente para el archivo de salida.

```bash
python3 main.py -f <nombre_del_archivo_entrada> -o <nombre_del_archivo_salida>
```

# Ejemplo del formato del archivo de entrada (csv)

Son 4 campos separadas por ,
- título
- link
- puntaje 1
- puntaje 2

```csv
mi ejemplo, http://google.com/resultado1, 2, 1
mi ejemplo2, http://google.com/resultado2, 3, 1
mi ejemplo3, http://google.com/resultado3, 7, 1
```