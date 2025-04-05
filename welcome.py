from rich.console import Console
from rich.panel import Panel

console = Console()

def welcome():
    "Calculo Impuesto Sobre la Renta"
    
    # Crear un panel con el mensaje de bienvenida
    welcome_message = "[bold green]Bienvenido a la Calculadora de Impuestos sobre la Renta![/bold green]\n"
    welcome_message += "\nEste programa te ayudará a calcular el impuesto sobre tu sueldo neto.\n"
    
    # Usar Panel para dar un borde alrededor del mensaje
    panel = Panel(welcome_message, title="Impuesto sobre la Renta", title_align="center", border_style="bold blue")
    
    # Mostrar el panel en la consola
    console.print(panel)
