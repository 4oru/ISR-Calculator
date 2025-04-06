from rich.console import Console
from rich.prompt import Prompt

import data_user
import isr_calculator
import welcome
import file_writer

def main():

    welcome.welcome()

    nombre, tipo_pago, salario = data_user.get_data_user()

    impuesto_isr = isr_calculator.calcular_isr(salario, tipo_pago)

    file_writer.guardar_calculo(nombre, tipo_pago, salario, impuesto_isr)

if __name__ == "__main__":
    main()