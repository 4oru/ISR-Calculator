import os
from datetime import datetime

def guardar_calculo(nombre, tipo_pago, salario):
    """
    Guarda el cálculo realizado en un archivo dentro de la carpeta 'Calculos_realizados'.
    El nombre del archivo es el nombre del usuario seguido de la fecha actual.
    """

    # Crear la carpeta 'Calculos_realizados' si no existe
    carpeta_destino = "Calculos_realizados"
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Obtener la fecha actual en el formato deseado
    fecha_actual = datetime.now().strftime("%d%m%Y")

    # Generar el nombre del archivo con el formato: nombre_fecha.txt
    nombre_archivo = f"{nombre}_{fecha_actual}.txt"

    # Crear el contenido que se va a escribir en el archivo
    contenido = f"""Calculo del Impuesto Sobre Renta

Nombre: {nombre}
Tipo de Pago: {'Anual' if tipo_pago == 'a' else 'Mensual'}
Sueldo: ${salario:,.2f} Pesos Dominicanos (DOP)
"""

    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)

    # Guardar el archivo
    with open(ruta_archivo, 'w') as archivo:
        # Escribir el contenido en el archivo
        archivo.write(contenido)

    print(f"Archivo guardado correctamente en: {ruta_archivo}")
