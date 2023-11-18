from util.utils import (
    app_presentation,
    app_prevent_error_folder_no_exist,
    app_prevent_error_files_no_exist,
    message,
    messageInput,
)
from modules import interactions, moderation, multimedia, profile, stadistics
from simple_colors import *
from util.error import *
import os
import requests
import json


class ModulesApp:
    profile_module = profile.Profile()
    multimedia_module = multimedia.Multimedia()
    interactions_module = interactions.Interactions()
    moderation_module = moderation.Moderation()
    stadistics_module = stadistics.Stadistics()


class App(ModulesApp):
    url_api_users: str = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json"
    url_api_posts: str = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json"

    """
        INIT APP
    """
    def __init__(self) -> None:
        # app_presentation()
        pass

    """
        El propósito de esta función es iniciar la aplicación
        
        El orden estipulado es el siguiente:
            1. Llamar a la API (Si es necesario)
            2. Expandir menú de opciones
            3. Despedirse al usuario
    """
    def start(self) -> None:
        self.__api()
        self.__menu()
        print(green("Gracias por usar la aplicación!"))

    """
    Esta función hace lo siguiente en el orden estipulado:
        1. ¿La carpeta existe?
            a. True
                1. ¿Algunos de los archvos no existe?
                    a. True
                        1. ¿Los archivos están vacíos?
                            a. True
                                - Llamar a la API
                                - Descargar información
                                - Almacenarla
                            
                            b. False
                                - Seguir curso
                                - Se sobreentiende que los archivos no han sido manipulados
                    
                    b. False
                        - Crea los archivos
                        - Cierra la aplicación para evitar errores
            
            b. False
                - Crea al carpeta
                - Cierra la aplicación para evitar errores
                
    """
    def __api(self) -> None:
        if os.path.exists("database"):
            # Si no existe los archivos json...
            if (
                os.path.exists("database/users.json") == False
                or os.path.exists("database/posts.json") == False
            ):
                app_prevent_error_files_no_exist()

            # Si no existen datos (Vacío) en los archivos
            try:
                with open("database/users.json", "r+") as f:
                    # Verificando información... Si entra, este descargará y guardará la info
                    if f.read() == "":
                        message("Se están descargando los datos de la API...")

                        json_users: dict = json.loads(
                            requests.get(self.url_api_users).content
                        )
                        json_posts: dict = json.loads(
                            requests.get(self.url_api_posts).content
                        )

                        # Guardando la info...
                        with open("database/users.json", "w+") as file_users:
                            json.dump(json_users, file_users)

                        # Guardando la info...
                        with open("database/posts.json", "w+") as file_posts:
                            json.dump(json_posts, file_posts)

                        message("Se terminó de descargar los datos!")

                with open("database/posts.json", "r+") as f:
                    # Verificando información... Si entra, este descargará y guardará la info
                    if f.read() == "":
                        message("Se están descargando los datos de la API...")
                        json_users: dict = json.loads(
                            requests.get(self.url_api_users).content
                        )
                        json_posts: dict = json.loads(
                            requests.get(self.url_api_posts).content
                        )

                        # Guardando la info...
                        with open("database/users.json", "w+") as file_users:
                            json.dump(json_users, file_users)

                        # Guardando la info...
                        with open("database/posts.json", "w+") as file_posts:
                            json.dump(json_posts, file_posts)

                        message("Se terminó de descargar los datos!")

            except requests.ConnectionError or requests.Timeout or requests.HTTPError:
                custom_error("ERROR! Ha ocurrido un problema con la conexión")
                exit()

        else:
            message(
                "Se detectó que la carpeta 'database' ha sido eliminada! Por favor conectese a internet para que al momento de solicitar la API no haya inconvenientes"
            )
            os.mkdir("database")
            app_prevent_error_folder_no_exist()

    """
        MENU MESSAGE APP
    """
    def __menuMessage(self) -> None:
        os.system("cls")
        # ------------------------------
        print(cyan("1: GESTIÓN DE PERFIL"))
        print(cyan("2: GESTIÓN DE MULTIMEDIA"))
        print(cyan("3: GESTIÓN DE INTERACCIONES"))
        print(cyan("4: GESTIÓN DE MODERACIÓN"))
        print(cyan("5: ESTADÍSTICAS"))
        # ------------------------------
        print(magenta("0: SALIR"))

    """
        MENU APP
    """
    def __menu(self) -> None:
        menuLoop = True
        while menuLoop:
            self.__menuMessage()
            opt = messageInput("Ingrese una opción (1/2/3/4/5/0): ")

            match opt:
                case "1":
                    self.profile_module.start()

                case "2":
                    self.multimedia_module.start()

                case "3":
                    self.interactions_module.start()

                case "4":
                    self.moderation_module.start()

                case "5":
                    self.stadistics_module.start()

                case "0":
                    menuLoop = False

                case _:
                    default_error()