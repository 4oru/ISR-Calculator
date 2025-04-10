import os
from datetime import datetime
from tabulate import tabulate

def guardar_calculo(nombre, tipo_pago, salario, impuesto_isr):
    """
    Guarda el cálculo realizado en un archivo dentro de la carpeta 'Calculos_realizados'.
    """
    carpeta_destino = "Calculos_realizados"
    os.makedirs(carpeta_destino, exist_ok=True)

    fecha_actual = datetime.now().strftime("%d%m%Y")
    nombre_archivo = f"{nombre}_{fecha_actual}.txt"

    # Validación crítica: El impuesto no puede superar el salario
    if (tipo_pago == 'a' and impuesto_isr > salario) or (tipo_pago == 'm' and impuesto_isr > salario):
        raise ValueError("ERROR: El impuesto ISR no puede ser mayor que el salario.")

    # Cálculos con protección contra negativos (usando max())
    if tipo_pago == 'a':  # Anual
        sueldo_mensual = salario / 12
        total_anual_sin_impuesto = salario
        renta_mensual = impuesto_isr / 12
        total_anual_con_impuesto = max(salario - impuesto_isr, 0)  # <--- Asegurar no negativo
    else:  # Mensual
        sueldo_mensual = salario
        total_anual_sin_impuesto = salario * 12
        renta_mensual = impuesto_isr
        total_anual_con_impuesto = max((salario - impuesto_isr) * 12, 0)  # <--- Asegurar no negativo

    # Cálculos finales protegidos
    total_mensual_con_impuesto = max(sueldo_mensual - impuesto_isr, 0)  # <--- Clave
    total_mensual_sin_impuesto = sueldo_mensual

    # Crear contenido de la tabla
    table_result = f"Declaración de Impuesto Sobre la Renta ({nombre})\n\n"

    # Tabla 1: Información del Usuario
    data_user = [
        ["Nombre", nombre],
        ["Tipo de Pago", "Anual" if tipo_pago == 'a' else "Mensual"],
        ["Sueldo bruto mensual", f"${sueldo_mensual:,.2f} DOP"],
        ["Sueldo bruto anual", f"${total_anual_sin_impuesto:,.2f} DOP"],
    ]

    table_result += "\n** Información del Contribuyente **\n"
    table_result += tabulate(data_user, headers=["Descripción", "Valor"], tablefmt="fancy_grid")
    table_result += "\n\n"

    # Tabla 2: Detalles del ISR (todos protegidos contra negativos)
    data_user_irs = [
        ["Renta Mensual", f"${renta_mensual:,.2f} DOP"],
        ["Renta Anual", f"${renta_mensual * 12:,.2f} DOP"],
        ["Total Mensual con Impuesto", f"${total_mensual_con_impuesto:,.2f} DOP",
        ["Total Anual con Impuesto", f"${total_anual_con_impuesto:,.2f} DOP"]]
    ]

    table_result += "** Detalles del Impuesto (ISR) **\n"
    table_result += tabulate(data_user_irs, headers=["Descripción", "Valor"], tablefmt="fancy_grid")
    table_result += "\n"

    # Texto adicional
    table_result += """
Para información adicional, puede llamar a nuestro CENTRO DE CONTACTO DGII, 
al teléfono (809) 689-3444, desde Santo Domingo, y 1 (809) 200-6060, desde el interior sin cargos, 
o escríbanos vía correo electrónico a oficinavirtual@dgii.gov.do o informacion@dgii.gov.do.

En Santo Domingo de Guzmán, Distrito Nacional, capital de la República Dominicana, 
a los veintiséis (26) días del mes de enero del año dos mil veintidós (2022).
"""

    # Guardar archivo
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(table_result)

    print("\n\nArchivo guardado correctamente en:")
    print(ruta_archivo)