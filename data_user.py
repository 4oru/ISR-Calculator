# data_user.py
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import os

# Creamos un objeto de consola para manejar la salida con rich
console = Console()

def clear_screen():
    """
    Limpiar la terminal.
    """
    # Limpiar la terminal dependiendo del sistema operativo
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Para sistemas tipo Unix (Linux/macOS)
        os.system('clear')

def create_table(nombre="", tipo_pago="", salario=""):
    """
    Crea la tabla con los datos proporcionados y la muestra en la terminal.
    """
    table = Table(title="Información del Usuario")
    
    # Definimos las columnas de la tabla
    table.add_column("Nombre", style="bold green")
    table.add_column("Tipo de Pago", style="bold green")
    table.add_column("Salario", style="bold green")
    
    # Añadimos las filas con la información proporcionada
    table.add_row(nombre, tipo_pago, f"{salario:,.2f} Pesos Dominicanos (DOP)")
    
    # Mostramos la tabla en la terminal
    console.clear()  # Limpiar la terminal antes de mostrar la tabla
    console.print(table)

def get_data_user():
    """
    Solicita la información del usuario:
    - Nombre
    - Tipo de pago (anual o mensual)
    - Monto del salario
    """
    
    # Inicializamos las variables de los datos del usuario
    nombre = ""
    tipo_pago = ""
    salario = 0.0

    while True:
        # Pedir el nombre del usuario
        nombre = Prompt.ask("¿Cuál es tu nombre?")
        
        # Pedir el tipo de pago (anual o mensual)
        tipo_pago = Prompt.ask("¿Es tu sueldo anual o mensual? (a/m)", choices=["a", "m"], default="m")
        
        # Pedir el monto del salario
        salario = float(Prompt.ask("¿Cuál es tu monto bruto de salario?", default="0"))
        
        # Mostrar la tabla actualizada con los datos proporcionados
        tipo_pago_str = 'anuales' if tipo_pago == 'a' else 'mensuales'
        create_table(nombre, tipo_pago_str, salario)
        
        # Mostrar la información obtenida para confirmación
        console.print(f"\n[green]{nombre}[/green], tu salario es [green]${salario:,.2f}[/green] Pesos Dominicanos (DOP) [green]{tipo_pago_str}[/green], ¿es correcto?")
        
        # Preguntar al usuario si la información es correcta
        confirmacion = Prompt.ask("¿Es correcto? (y/n)", choices=["y", "n"], default="y")
        
        # Si la respuesta es 'y', salimos del bucle, si es 'n', limpiamos la terminal y repetimos el proceso
        if confirmacion.lower() == 'y':
            return nombre, tipo_pago, salario
        else:
            # Limpiar la pantalla y repetir el proceso
            clear_screen()
