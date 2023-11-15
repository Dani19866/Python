from simple_colors import *

def restart():
    print(green("Se efectuaron unos cambios... Se necesita volver a iniciar la aplicación!"))
    
def default_error():
    print(red("ERROR! Entrada inválida, por favor inténtelo de nuevo"))
    
def custom_error(text: str):
    print(red(text))