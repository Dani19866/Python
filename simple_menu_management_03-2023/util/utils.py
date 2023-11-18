from util.database import compareer_email, compareer_username
from util.error import *
from simple_colors import *
from uuid import uuid4

import os
import time
import string
import random


# ------------------------------
# Funciones específicas
# READY TO USE
def message(text: str):
    print(yellow(text))


# READY TO USE
def messageInput(text: str):
    return input(yellow(text))


# ------------------------------
# Funciones de: app.py
# READY TO USE
def app_presentation():
    print(cyan("Este es el proyecto de Jesus Rodriguez"))
    print(cyan("Sin más nada que añadir, se presenta el proyecto..."))
    print(
        yellow(
            "Se desea quitar esta pausa de 5s vaya a util/utils.py -> app_presentation()"
        )
    )
    time.sleep(5)
    os.system("cls")


# READY TO USE
def app_prevent_error_folder_no_exist():
    message("Se ha CREADO la CARPETA que almacena los archivos!")
    message(
        "Por favor conéctese a internet para que al momento de solicitar la API no haya inconvenientes"
    )
    restart()
    exit(0)


# READY TO USE
def app_prevent_error_files_no_exist():
    with open("database/users.json", "x") as f:
        pass

    with open("database/posts.json", "x") as f:
        pass

    message("Se han CREADO los ARCHIVOS que almacena los datos!")
    message(
        "Por favor conéctese a internet para que al momento de solicitar la API no haya inconvenientes"
    )
    restart()
    exit(0)


# ------------------------------
# Funciones de: modules/profile.py
# READY TO USE
def generate_id() -> str:
    return str(uuid4())

def generate_post_id() -> str:
    keywords = string.ascii_letters + string.digits
    key = "".join(random.choice(keywords) for i in range(20))
    return key

# READY TO USE
def generate_email_extemsion() -> str:
    keywords = string.ascii_letters + string.digits
    key = "".join(random.choice(keywords) for i in range(10))
    return key


# READY TO USE
def generate_email(name: str, lastname: str, type: str) -> str:
    email = ""
    # ------------------------------
    # 1. Creation of email
    if type == "professor":
        email = f"{name}.{lastname}.{generate_email_extemsion()}@unimet.edu.ve".lower()

    elif type == "student":
        email = f"{name}.{lastname}.{generate_email_extemsion()}@correo.unimet.edu.ve".lower()

    else:
        return ""

    # ------------------------------
    # 2. Verify email and RECURSIVIDAD
    if compareer_email(email) != None:
        return email

    return generate_email(name, lastname, type)


# READY TO USE
def valid_username(username: str) -> str | None:
    # 1. Search in db -> Error if has coincidence
    if compareer_username(username) != None:
        return username
    
    custom_error("ERROR! Usuario ya en uso")
    return ""