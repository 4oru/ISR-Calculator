def calcular_isr(total, payment_type):
    """
    Calcula el Impuesto Sobre la Renta (ISR) en la República Dominicana.

    Args:
        total (float): Ingreso mensual o anual en pesos dominicanos (RDS).
        payment_type (str): Tipo de ingreso ("m" para mensual, otro valor para anual).

    Returns:
        float: Impuesto calculado, redondeado a dos decimales.

    Raises:
        ValueError: Si el total es negativo.
    """
    if total < 0:
        raise ValueError("El ingreso no puede ser negativo.")

    # Convertir a anual si es mensual
    if payment_type == "m":
        total *= 12

    # Límites y tasas de los tramos (en RDS)
    tramos = [
        (416220.00, 0.0, 0.0),  # Tramo 1: Exento
        (624329.00, 416220.01, 0.15),  # Tramo 2: 15% sobre excedente
        (867123.00, 624329.01, 0.20),  # Tramo 3: RDS31,216 + 20%
        (float('inf'), 867123.01, 0.25)  # Tramo 4: RDS79,776 + 25%
    ]

    if total <= tramos[0][0]:
        return 0.0

    # Calcular el tramo correspondiente
    impuesto = 0.0
    if total <= tramos[1][0]:  # Tramo 2
        excedente = total - tramos[1][1]
        impuesto = excedente * tramos[1][2]

    elif total <= tramos[2][0]:  # Tramo 3
        excedente = total - tramos[2][1]
        impuesto = 31216.00 + (excedente * tramos[2][2])

    else:  # Tramo 4
        excedente = total - tramos[3][1]
        impuesto = 79776.00 + (excedente * tramos[3][2])

    # Asegurar que no haya impuesto negativo por errores de precisión
    impuesto = max(impuesto, 0.0)
    return round(impuesto, 2)