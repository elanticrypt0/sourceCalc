from reader import *
from htmlprinter import HtmlPrinter
import argparse

def app_banner():
    banner="""
    #########################################
        CALCULADORA DE FUENTES
                        2024  elanticrypt0
    ####################################
    """
    print(banner)

def show_html():
    print("imprimiendo html...")

""" MAIN """
app_banner()

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description='Ejemplo de uso de flags -f y -o')

# Agregar los argumentos -f y -o
parser.add_argument('-f', metavar='archivo', type=str, help='Path/nombre al archivo de entrada -f')
parser.add_argument('-o', metavar='archivo', type=str, help='path/nombre del archivo de salida -o')

# Parsear los argumentos de la línea de comandos
args = parser.parse_args()

source_file=args.f if args.f else "./source_manifest.csv"
output_file=args.o if args.o else "./resultado.html"

sources=[]
# carga las fuentes
get_source(sources,source_file)

# get the instance of htmlprinter
html_printer=HtmlPrinter(sources)
html_printer.set_outputfile_name(output_file)

# print html
html_printer.save_html()