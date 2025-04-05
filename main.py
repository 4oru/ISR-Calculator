from rich.console import Console
from rich.prompt import Prompt

import data_user
import welcome
import file_writer

def main():

    welcome.welcome()

    nombre, tipo_pago, salario = data_user.get_data_user()
    
    
    file_writer.guardar_calculo(nombre, tipo_pago, salario)

if __name__ == "__main__":
    main()