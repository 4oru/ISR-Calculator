import os
from datetime import datetime
from tabulate import tabulate


def guardar_calculo(nombre, tipo_pago, salario, impuesto_isr):
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

    # Calcular totales dependiendo del tipo de pago
    if tipo_pago == 'a':  # Anual
        sueldo_mensual = salario / 12
        total_anual_sin_impuesto = salario
        total_mensual_sin_impuesto = sueldo_mensual
        total_anual_con_impuesto = salario - impuesto_isr
        total_mensual_con_impuesto = total_anual_con_impuesto / 12
    else:  # Mensual
        sueldo_mensual = salario
        total_anual_sin_impuesto = salario * 12
        total_mensual_sin_impuesto = sueldo_mensual
        total_anual_con_impuesto = (salario - impuesto_isr) * 12
        total_mensual_con_impuesto = salario - impuesto_isr

    # Crear los encabezados y datos dinámicos
    data = [
        ["Nombre", nombre],
        ["Tipo de Pago", "Anual" if tipo_pago == 'a' else "Mensual"],
        ["Sueldo bruto mensual", f"${sueldo_mensual:,.2f} Pesos Dominicanos (DOP)"],
        ["Impuesto sobre la Renta", f"${impuesto_isr:,.2f} Pesos Dominicanos (DOP)"],
        ["Sueldo neto mensual", f"${sueldo_mensual - impuesto_isr:,.2f} Pesos Dominicanos (DOP)"],

        # Mostrar totales anuales solo para tipo de pago anual
        ["Total Anual sin Impuesto",
         f"${total_anual_sin_impuesto:,.2f} Pesos Dominicanos (DOP)"] if tipo_pago == 'a' else [
            "Total Anual sin Impuesto", "N/A"],

        # Mostrar total mensual para ambos casos
        ["Total Mensual sin Impuesto", f"${total_mensual_sin_impuesto:,.2f} Pesos Dominicanos (DOP)"],

        # Mostrar total anual con impuesto solo para tipo anual
        ["Total Anual con Impuesto",
         f"${total_anual_con_impuesto:,.2f} Pesos Dominicanos (DOP)"] if tipo_pago == 'a' else [
            "Total Anual con Impuesto", "N/A"],

        # Mostrar total mensual con impuesto para ambos casos
        ["Total Mensual con Impuesto", f"${total_mensual_con_impuesto:,.2f} Pesos Dominicanos (DOP)"]
    ]

    # Crear contenido de la tabla con el formato deseado
    table_result = f"Declaración de Impuesto Sobre la Renta ({nombre})\n\n"
    table_result += "Para dar cumplimiento a lo establecido en el artículo 28 de la Ley 345-21 de Presupuesto General del Estado.\n\n"
    table_result += tabulate(data, headers=["Descripción", "Valor"], tablefmt="fancy_grid")
    table_result += "\n\n"

    # Añadir el texto adicional debajo de la tabla con saltos de línea
    table_result += """
Para información adicional, puede llamar a nuestro CENTRO DE CONTACTO DGII, 
al teléfono (809) 689-3444, desde Santo Domingo, y 1 (809) 200-6060, desde el interior sin cargos, 
o escríbanos vía correo electrónico a oficinavirtual@dgii.gov.do o informacion@dgii.gov.do.

En Santo Domingo de Guzmán, Distrito Nacional, capital de la República Dominicana, 
a los veintiséis (26) días del mes de enero del año dos mil veintidós (2022).
"""

    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)

    # Guardar el archivo con codificación UTF-8
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(table_result)

    # Imprimir mensaje de éxito en consola
    print("\n\nArchivo guardado correctamente en:")
    print(ruta_archivo)
