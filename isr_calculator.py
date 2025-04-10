def calcular_isr(total, payment_type):
    """
    Calcula el Impuesto Sobre la Renta (ISR) en la República Dominicana.
    Retorna el impuesto **mensual** si payment_type es "m", y anual si es otro valor.
    """
    if total < 0:
        raise ValueError("El ingreso no puede ser negativo.")

    ingreso_anual = total * 12 if payment_type == "m" else total

    tramos = [
        (416220.00, 0.0, 0.0),
        (624329.00, 416220.01, 0.15),
        (867123.00, 624329.01, 0.20),
        (float('inf'), 867123.01, 0.25)
    ]

    if ingreso_anual <= tramos[0][0]:
        impuesto_anual = 0.0
    elif ingreso_anual <= tramos[1][0]:
        excedente = ingreso_anual - tramos[1][1]
        impuesto_anual = excedente * tramos[1][2]
    elif ingreso_anual <= tramos[2][0]:
        excedente = ingreso_anual - tramos[2][1]
        impuesto_anual = 31216.00 + (excedente * tramos[2][2])
    else:
        excedente = ingreso_anual - tramos[3][1]
        impuesto_anual = 79776.00 + (excedente * tramos[3][2])

    impuesto_anual = max(impuesto_anual, 0.0)

    # Convertir a mensual si el tipo de pago es "m"
    if payment_type == "m":
        impuesto = impuesto_anual / 12
    else:
        impuesto = impuesto_anual

    return round(impuesto, 2)