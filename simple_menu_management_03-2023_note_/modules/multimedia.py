from util.database import (
    search_user_with_username,
    get_posts_json,
    save_posts_json,
    update_user,
    get_post,
    update_post,
    search_user_with_id,
)
from util.utils import messageInput, message, generate_post_id
from util.error import *

import time
import datetime


class MultimediaFunctionsExtension:
    def req_type(self) -> dict:
        doc = {"type": "", "url": ""}

        # Type post
        type_post = (messageInput('Escriba "video" o "photo" según su publicación: ').strip().lower())
        doc.update({"type": type_post})

        # Condition & URL post
        if type_post == "video" or type_post == "photo":
            # URL post
            url_post = (messageInput("Escriba la URL de la publicación: ").strip().lower())
            doc.update({"url": url_post})
            return doc

        return None

    def req_hashtag(self) -> list:
        tags = (messageInput("Escriba sus tags separandolos por comas (,). Si no desea colocar tags presione ENTER: ").strip().replace(" ", ""))
        if tags == "":
            return []
        else:
            return tags.split(",")

    def req_date(self) -> str:
        return str(datetime.datetime.now()).replace(" ", "T") + "Z"

    def save_follow(self, user_current: dict, user_view: dict):
        # Extraer id del follower
        user_id = user_current.get("id")

        # Incluir el id del follower en el account
        user_view_followers: list = user_view.get("following")
        user_view_followers.append(user_id)

        # Actualizar doc
        user_view.update({"following": user_view_followers})

        # Actualizar base de datos
        update_user(user_view)

    def show_posts(self, user_view: dict):
        print("------------------------------")
        print(yellow("Nombre: ") + user_view.get("firstName"))
        print(yellow("Username: ") + user_view.get("username"))
        print(yellow("Listado de publicaciones: "))

        posts: list[dict] = []
        json_posts = get_posts_json()

        for post in json_posts:
            id_compareer = post.get("publisher")
            id_current = user_view.get("id")

            if id_compareer == id_current:
                posts.append(post)

        for post in posts:
            type_post = post.get("type")
            id_post = post.get("post_id")

            print(f"     Tipo: {type_post}")
            print(f"     ID: {id_post}")
            print("     ------------------------------")

    def select_post(self, user_view: dict) -> str:
        post_id = messageInput("Escriba el ID de la publicación: ").strip()
        json_posts = get_posts_json()

        for post in json_posts:
            if (post.get("publisher") == user_view.get("id")) and (post.get("post_id") == post_id):
                return post_id

        print(red("ERROR! Publicación no encontrada"))
        return None

    def show_comments(self, post: dict):
        comments: list[dict] = post.get("comments")

        # Presentar
        if comments != []:
            for user in comments:
                username = user.get("username")
                comment = user.get("comment")
                print("     " + f"({username}): {comment}")

        # No contiene data
        else:
            print("     " + "Este post se encuentra sin comentarios")

    def show_likes(self, post: dict):
        likes = post.get("likes")

        # Presentar
        if likes != []:
            for username in likes:
                print("     " + username)

        # No contiene data
        else:
            print("     " + "Este post se encuentra sin likes")

    def fullshow_post(self, post_id: str, user_view: dict):
        post = get_post(post_id)
        print("------------------------------")
        print(yellow("ID: ") + post.get("post_id"))
        print(yellow("Username: ") + user_view.get("username"))
        print(yellow("Tipo: ") + post.get("type"))
        print(yellow("Descripción: ") + post.get("caption"))
        print(yellow("Fecha: ") + post.get("date")[0:10])
        print(yellow("Tags: ") + post.get("tags").__str__())
        print(yellow("URL: ") + post.get("multimedia").get("url"))
        print(yellow("Comentarios: "))
        self.show_comments(post)
        print(yellow("Likes: "))
        self.show_likes(post)
        print("------------------------------")

    def comment_post(self, user: dict, post_id: str):
        comment = messageInput("Introduzca su comentario: ").strip()
        post = get_post(post_id)
        
        doc = {"username": user.get("username"), "comment": comment, "date": self.req_date()}
        
        post.get("comments").append(doc)
        update_post(post)

    def view_post_extension(self, user: dict, user_view: dict):
        self.show_posts(user_view)
        post = self.select_post(user_view)

        if post != None:
            select = messageInput(
                "Si desea ver el post presione (1), si desea comentar presione (2): "
            ).strip()

            if select == "1":
                self.fullshow_post(post, user_view)

            elif select == "2":
                self.comment_post(user, post)

            else:
                default_error()


class MultimediaFunctions(MultimediaFunctionsExtension):
    """
    Esta función permite registrar la publicación de un usuario en la base de datos

    El orden es el siguiente:
        1. Solicitar tipo de publicación
        2. Solicitar descripción
        3. Solicitar tags
        4. Creación de publicación
        5. Actualizar y guardar
    """
    def register_post(self, user: dict):
        id_post = user.get("id")
        type_post = self.req_type()
        # Handle error
        if type_post == None:
            print(red("ERROR! El tipo de publicación es inválido"))
            return
        caption_post = messageInput("Ingrese una descripción. Presione ENTER si no desea agregar descripción: ").strip()
        hashtags_post = self.req_hashtag()
        date_post = self.req_date()

        # Doc
        doc = {
            "publisher": id_post,
            "type": type_post.get("type"),
            "caption": caption_post,
            "date": date_post,
            "tags": hashtags_post,
            "multimedia": {"type": type_post.get("type"), "url": type_post.get("url")},
            "comments": [],
            "likes": [],
            "post_id": generate_post_id()
        }

        # Update and save
        json_data = get_posts_json()
        json_data.append(doc)
        print(green("Se ha registrado el post con éxito!"))
        save_posts_json(json_data)

    """
        Esta función permite ver los posts de forma más detallada y adicionalmente comentarla de un usuario
        
        El orden es el siguiente:
            1. Ingresar el username del usuario a buscar
                a. Si no sigues el usuario
                    1.1. Solicitar seguimiento
                        a. Aceptar
                            1. Guardar follow
                            2. view_post_extension

                        b. Rechazar
                            1. Salir del menu de gestión de multimedia
                
                b. Si sigues el usuario
                    1. view_post_extension
                
        Extensión:
            view_post_extension:
                1. Mostrar publicaciones
                2. Solicitar publicación
                    a. Mostrar publicación completa
                    b. Comentar la publicación

    """
    def view_post(self, user: dict):
        user_to_view = messageInput("Por favor, ingrese el username: ").strip()
        user_view = search_user_with_username(user_to_view)

        if user_view != None:
            userid_current = user.get("id")
            compareer_following: list = user_view.get("following")

            # Si no lo sigue...
            if userid_current not in compareer_following:
                select = messageInput("Usted no sigue a este usuario... ¿Desea seguirlo? (S/N): ").strip()

                # Aceptar
                if select == "S":
                    # Seguir y aplicar cambios
                    self.save_follow(user, user_view)
                    self.view_post_extension(user, user_view)

                # Rechazar
                else:
                    message(f"Entonces usted no puede ver las publicaciones de {user_view.get('username')}")

            # Si ya lo sigue...
            else:
                self.view_post_extension(user, user_view)

        else:
            custom_error("ERROR! No se encuentra el usuario")

    """
        NOTE: Como está estructurado el proyecto y su funcionalidad, el punto 3 (este) debería ir en el punto 2
        ya que primero buscas la publicación y con los datos obtenidos tener el username para buscar el usuario.
        Por eso mismo se cambia el hecho de buscar en función a 'User' ya que mostrar publicaciones de un usuario
        en específico ya se encuentra en el punto 2 y a parte, en el módulo de perfil

        Esta función permite buscar posts que contengan un tag en específico
        
        El orden es el siguiente:
            1. Solicitar tag
            2. Buscar publicaciones
            3. Mostrar publicaciones        
        """
    def search_tags(self, user: dict):
        # Organización
        req_tag = (
            messageInput("Introduzca el tag para buscar referencias: ")
            .strip()
            .replace('""', "")
            .replace("''", "")
        )
        posts = get_posts_json()

        # Presentar
        count = 0
        print(yellow("Publicaciones: "))
        for post in posts:
            tags: list = post.get("tags")

            for tag in tags:
                if tag == req_tag:
                    count = count + 1

                    type_post = post.get("type")
                    id_post = post.get("post_id")

                    print(f"     Username: {search_user_with_id(post.get('publisher')).get('username')}")
                    print(f"     Tipo: {type_post}")
                    print(f"     ID: {id_post}")
                    print("     ------------------------------")

        if count == 0:
            print("     " + "Sin resultados")


class Multimedia(MultimediaFunctions):
    """
    MENU MESSAGE APP
    """
    def __menuMessage(self) -> None:
        print(cyan("1: REGISTRAR POST"))
        print(cyan("2: VER POSTS DE OTRO USUARIO"))
        print(cyan("3: BUSCAR POSTS EN BASE A TAGS"))
        # ------------------------------
        print(magenta("0: SALIR"))

    """
        El propósito de esta función es iniciar el módulo de multimedia que permite manejar las publicaciones de los usuarios
    """
    def start(self):
        username = (
            messageInput("Por favor, ingrese su username: ").strip().replace("@", "")
        )
        user = search_user_with_username(username)

        if user == None:
            custom_error("ERROR! No se encuentra el usuario")
            time.sleep(2)
            return

        menuLoop = True
        while menuLoop:
            self.__menuMessage()
            opt = messageInput("Ingrese una opción (1/2/3/0): ")

            match opt:
                case "1":
                    self.register_post(user)

                case "2":
                    self.view_post(user)

                case "3":
                    self.search_tags(user)

                case "0":
                    menuLoop = False

                case _:
                    default_error()
