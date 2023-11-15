from util.utils import messageInput, generate_id, valid_username, generate_email
from util.database import (
    save_new_user,
    search_user_with_username,
    search_user_with_email,
    update_user,
    compareer_email,
    del_user,
    get_user_json,
    get_posts_json,
)

from simple_colors import *
from util.error import *
from os import system


class ProfileFunctionsExtension:
    def change_info_menu(self):
        print(cyan("1: CAMBIAR NOMBRE"))
        print(cyan("2: CAMBIAR APELLIDO"))
        print(cyan("3: CAMBIAR USERNAME"))
        print(cyan("4: CAMBIAR EMAIL"))
        # ------------------------------
        print(magenta("0: SALIR"))

    def show_user(self, doc: dict):
        print(yellow("Fullname: ") + f"{doc.get('firstName')} {doc.get('lastName')}")
        print(yellow("Email: ") + f"{doc.get('email')}")
        print(yellow("Username: ") + f"{doc.get('username')}")

    def categories_filter(self):
        # Organización
        departments = []
        careers = []
        json_data: list[dict] = get_user_json()

        for user in json_data:
            user_type = user.get("type")

            # professor -> department
            if user_type == "professor":
                deparment = user.get("department")

                if deparment not in departments:
                    departments.append(deparment)

            # student -> major
            if user_type == "student":
                major = user.get("major")
                print(major)

                if major not in careers:
                    careers.append(major)

        # Mostrar
        print(yellow("Departamentos:"))
        for d in departments:
            print(f"     {cyan(d)}")
        print(yellow("Carreras: "))
        for c in careers:
            print(f"     {cyan(c)}")

        # Separación
        users: list[dict] = []

        # Entrada
        select = input(
            yellow("Por favor, introduzca algún departamento/carrera: ")
        ).strip()

        # Búsqueda
        for user in json_data:
            department = user.get("department")
            major = user.get("major")

            if deparment == select or major == select:
                users.append(user)

        # Respuesta
        if users != []:
            print("------------------------------")
            for user in users:
                self.show_user(user)
                print("------------------------------")
        else:
            print(red("ERROR! No se ha encontrado ninguna coincidencia"))

    def show_posts_list(self, doc: dict):
        posts: list[dict] = []
        json_posts = get_posts_json()

        for post in json_posts:
            id_compareer = post.get("publisher")
            id_current = doc.get("id")

            if id_compareer == id_current:
                posts.append(post)

        for post in posts:
            type_post = post.get("type")
            id_post = post.get("post_id")

            print(f"     Tipo: {type_post}")
            print(f"     ID: {id_post}")
            print("     ------------------------------")

    def show_specific_post(self, doc: dict, post_id: str):
        json_posts = get_posts_json()

        for post in json_posts:
            if (post.get("publisher") == doc.get("id")) and (post_id == post.get("post_id")):
                print("------------------------------")
                print("     " + "Caption: " + post.get("caption"))
                print("     " + "Tags: " + post.get("tags").__str__())
                print("     " + "URL: " + post.get("multimedia").get("url"))
                print("------------------------------")
                return

        print(red("ERROR! Publicación no encontrada"))


class ProfileFunctions(ProfileFunctionsExtension):

    """
    Esta función registra al nuevo usuario en la base de datos

    El orden es el siguiente:
        1. Se solicitan los datos básicos
        2. Se solicita la información académica
        3. Se genera automáticamente su Email
        4. Guarda el usuario en la base de datos
    """
    def register_user(self):
        # Basic info
        user_id = generate_id()
        name = messageInput("Ingrese su nombre: ").strip()
        lastname = messageInput("Ingrese su apellido: ").strip()
        username = valid_username(messageInput("Ingrese su username: ")).strip()
        while username == "ERROR":
            username = valid_username(messageInput("Ingrese su username: ")).strip()

        # Type info
        fq = messageInput("¿Eres profesor (S/N)?: ").strip()
        fq_confirm = 0
        user_type = ""
        major = ""

        if fq == "S":
            user_type = "professor"
            major = messageInput("¿Cuál es el departamento?: ").strip()

        elif fq == "N":
            user_type = "student"
            major = messageInput("¿Qué carrera estás cursando?: ").strip()

        else:
            fq_confirm = 1

        # Automatic info
        email = generate_email(name, lastname, user_type).replace(" ", "_").lower()

        # Doc algorithm
        if fq_confirm == 0 and email != "ERROR" and username != "ERROR":
            doc = {
                "id": user_id,
                "firstName": name,
                "lastName": lastname,
                "email": email,
                "username": username,
                "type": user_type,
                "major": major,
                "following": [],
            }
            # ----------
            system("cls")
            # ----------
            print(
                green(
                    "Se ha registrado exitosamente! Esta es su información, no la pierda"
                )
            )
            print(yellow("Nombre y apellido: ") + f"{name} {lastname}")
            print(yellow("Username: ") + username)
            print(yellow("Email: ") + email)
            save_new_user(doc)

        else:
            custom_error(
                "ERROR! No se ha podido registrar el usuario, por favor verifique los datos introducidos e intente de nuevo"
            )

    """
        Esta función busca perfiles en la base de datos
        
        El orden es el siguiente:
            Se solicita si es por (username) o (carrera/departamento)
                a. Username
                    1. Busca el username en la bbdd
                    2. Se muestra el usuario
                
                b. Carrera/Departamento
                    1. Se muestra los departamentos y carreras
                    2. Se solicita cual carrera o departamento mostrar
                    3. Se muestra el/los usuario/s
    """
    def search_profiles(self):
        # Solicitar filtro
        select = messageInput(
            "Buscar perfiles por username (1) o Buscar perfiles por carrera (2): "
        ).strip()

        # Buscar por username
        if select == "1":
            # Solicitar
            user_to_search = (
                messageInput("Por favor, ingrese el username: ")
                .replace("@", "")
                .strip()
            )

            # Buscar
            user_data = search_user_with_username(user_to_search)

            # Condición
            if user_data != None:
                self.show_user(user_data)

            else:
                custom_error("ERROR! No se ha encontrado el usuario ")

        # Buscar por carrera o departamento
        elif select == "2":
            self.categories_filter()

        else:
            default_error()

    """
        Ya que no tenemos una contraseña con la cual validar cada usuario, se procede a pensar en la honestidad
        y el acceso solo a su cuenta mediante el Email. Esta función solicita el email para cambiar los datos
        que este tiene registrado en la base de datos
        
        El orden es el siguiente:
            1. Solicita email
            2. Busca el email
            3. Se muestran las opciones
                a. Cambiar nombre
                b. Cambiar apellido
                c. Cambiar username
                d. Cambiar email
            4. Se ejecutan y guardan los cambios
    """
    def change_info(self):
        email = messageInput("Ingrese su email: ").strip()
        user = search_user_with_email(email)

        # Encontró el usuario
        if user != None:
            self.change_info_menu()
            opt = messageInput("Ingrese una opción (1/2/3/4/0): ")

            match opt:
                case "1":
                    name = messageInput("Ingrese su nuevo nombre: ").strip()

                    # Update doc
                    user.update({"firstName": name})

                    # Save doc
                    update_user(user)
                    print(green("Se han actualizado los datos!"))

                case "2":
                    lastname = messageInput("Ingrese su nuevo apellido: ").strip()

                    # Update doc
                    user.update({"lastName": lastname})

                    # Save doc
                    update_user(user)
                    print(green("Se han actualizado los datos!"))

                case "3":
                    username = valid_username(
                        messageInput("Ingrese su username: ")
                    ).strip()
                    while username == "":
                        username = valid_username(
                            messageInput("Ingrese su username: ")
                        ).strip()

                    # Update doc
                    user.update({"username": username})

                    # Save doc
                    update_user(user)
                    print(green("Se han actualizado los datos!"))

                case "4":
                    # Organización
                    email = ""

                    # @correo.unimet.edu.ve
                    if user.get("type") == "student":
                        email = messageInput("Ingrese su nuevo email: ").strip()

                        # 1. Verificar si existe @correo.unimet.edu.ve
                        if "@correo.unimet.edu.ve" not in email:
                            print(
                                red(
                                    "ERROR! No ha ingresado correctamente @correo.unimet.edu.ve"
                                )
                            )
                            return

                        # 2. Verificar si no se está usando ese email
                        if compareer_email(email) == None:
                            print(red("ERROR! El email ya se encuentra en uso"))
                            return

                    # @unimet.edu.ve
                    else:
                        email = messageInput("Ingrese su nuevo email: ").strip()

                        # 1. Verificar si existe @unimet.edu.ve
                        if "@unimet.edu.ve" not in email:
                            print(
                                red(
                                    "ERROR! No ha ingresado correctamente @unimet.edu.ve"
                                )
                            )
                            return

                        # 2. Verificar si no se está usando ese email
                        if compareer_email(email) == None:
                            print(red("ERROR! El email ya se encuentra en uso"))
                            return

                    # Update doc
                    user.update({"email": email})

                    # Save doc
                    update_user(user)
                    print(green("Se han actualizado los datos!"))

                case "0":
                    menuLoop = False

                case _:
                    default_error()

        # Sin resultados
        else:
            custom_error("ERROR! El email introducido no existe")

    """
        Ya que no tenemos una contraseña con la cual validar cada usuario, se procede a pensar en la honestidad
        y el acceso solo a su cuenta mediante el Email. Esta función solicita el email para eliminar dicha cuenta
        de la base de datos
        
        El orden es el siguiente:
            1. Solicitud de email
            2. Busca el email
            3. Solicitud de confirmación
            4. Eliminación de cuenta en la base de datos
    """
    def del_info(self):
        email = messageInput("Ingrese su email: ").strip()
        user = search_user_with_email(email)

        # Encontró el usuario
        if user != None:
            confirm = messageInput(
                "¿Está usted seguro que quiere eliminar la cuenta? (S/N): "
            )

            if confirm == "S":
                del_user(user)

            else:
                custom_error("Operación cancelada")

        # Sin resultados
        else:
            custom_error("ERROR! El email introducido no existe")

    """
        Esta función solicita el username para poder mostrar la informació básica de la cuenta y sus publicaciones
        
        El orden es el siguiente:
            1. Solicitud de email
            2. Búsqueda de email
            3. Mostrar información
                3.1. Ofrecer acceder a una publicación
                3.2. Solicitar fecha de la publicación
    """
    def search_specific_user(self):
        user_to_search = (
            messageInput("Por favor, ingrese el username del usuario: ")
            .strip()
            .replace("@", "")
        )
        user = search_user_with_username(user_to_search)

        if user != None:
            print("------------------------------")
            print(yellow("Nombre: ") + user.get("firstName"))
            print(yellow("Username: ") + user.get("username"))
            print(yellow("Listado de publicaciones: "))
            self.show_posts_list(user)

            # Acceder a una publicación
            select = messageInput("¿Desea acceder a una publicación en específico? (S/N): ")

            if select == "S":
                post_id = messageInput("Por favor, introduzca el ID de la publicación: ").strip()
                self.show_specific_post(user, post_id)

        else:
            custom_error("ERROR! El usuario no existe")


class Profile(ProfileFunctions):
    """
    MENU MESSAGE APP
    """
    def __menuMessage(self) -> None:
        print(cyan("1: REGISTRAR NUEVO USUARIO"))
        print(cyan("2: BUSCAR PERFILES"))
        print(cyan("3: CAMBIAR LA INFORMACIÓN PERSONAL"))
        print(cyan("4: BORRAR LOS DATOS DE LA CUENTA "))
        print(cyan("5: ACCEDER AL PERFIL DE OTRO USUARIO"))
        # ------------------------------
        print(magenta("0: SALIR"))

    """
        El propósito de esta función es iniciar el módulo de gestión de perfil desplegando el menú con distintas opciones
        para la necesidad del usuario
    """
    def start(self):
        menuLoop = True
        while menuLoop:
            self.__menuMessage()
            opt = messageInput("Ingrese una opción (1/2/3/4/5/0): ")

            match opt:
                case "1":
                    self.register_user()

                case "2":
                    self.search_profiles()

                case "3":
                    self.change_info()

                case "4":
                    self.del_info()

                case "5":
                    self.search_specific_user()

                case "0":
                    menuLoop = False

                case _:
                    default_error()