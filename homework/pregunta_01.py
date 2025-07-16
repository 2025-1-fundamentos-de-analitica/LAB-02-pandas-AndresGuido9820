"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    # Cargar datos desde archivo TSV
    tabla = pd.read_csv("files/input/tbl0.tsv", delimiter="\t")
    
    # Obtener número total de registros
    num_filas = len(tabla)
    
    return num_filas
