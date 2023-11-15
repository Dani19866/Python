from util.database import *
from util.utils import *
from util.error import *
from simple_colors import *
import datetime


class InteractionsFunctionsExtension:
    def create_comment_doc(self, current_user: str, comment: str) -> dict:
        return {
            "username": current_user.get("username"),
            "comment": comment,
            "date": str(datetime.datetime.now()).replace(" ", "T") + "Z",
        }

    def aux_follow(self, current_user: dict, compareer_user: dict):
        following_list: list = current_user.get("following")

        if compareer_user.get("id") not in following_list:
            following_list.append(compareer_user.get("id"))
            current_user.update({"following": following_list})
            update_user(current_user)

    def aux_unfollow(self, current_user: dict, compareer_user: dict):
        following_list: list = current_user.get("following")

        if compareer_user.get("id") in following_list:
            following_list.remove(compareer_user.get("id"))
            current_user.update({"following": following_list})
            update_user(current_user)

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
            print(f"     Fecha: {id_post}")
            print("     ------------------------------")

    def select_post(self, user_view: dict) -> str:
        id_post = messageInput("Escriba el ID de la publicación: ").strip()
        json_posts = get_posts_json()

        for post in json_posts:
            if (post.get("publisher") == user_view.get("id")) and (post.get("post_id") == id_post):
                return id_post

        print(red("ERROR! Publicación no encontrada"))
        return None

    def save_comment(self, current_post_id: str, current_user: dict, comment: str):
        json_posts = get_posts_json()

        for post in json_posts:
            compareer_post_id = post.get("post_id")

            if current_post_id == compareer_post_id:
                all_comments: list = post.get("comments")
                doc = self.create_comment_doc(current_user, comment)
                all_comments.append(doc)
                post.update({"comments": all_comments})
                update_post(post)

    def show_user(self, doc: dict):
        print(yellow("Usuario: "))
        print(
            "     "
            + yellow("Fullname: ")
            + f"{doc.get('firstName')} {doc.get('lastName')}"
        )
        print("     " + yellow("Email: ") + f"{doc.get('email')}")
        print("     " + yellow("Username: ") + f"{doc.get('username')}")

    def search_with_index(self, username: str):
        user = search_user_with_username(username)

        if user != None:
            self.show_user(user)

        else:
            custom_error("ERROR! El usuario no existe")

    def list_of_likes(self, current_user: dict):
        message("Primero, se solicita el username del usuario. Segundo, se solicita la fecha del post a visualizar y por último elegir que perfil visitar")
        founded_user = messageInput("Por favor, ingrese el username del usuario: ")
        founded_user = search_user_with_username(founded_user)

        if founded_user != None:
            self.show_posts(founded_user)
            id_post = self.select_post(founded_user)

            if id_post != None:
                post = get_post(id_post)
                all_likes: list[str] = post.get("likes")
                
                message("Usuarios:")
                if all_likes == []:
                    print("     -La publicación no tiene likes")
                    return
                index = 0
                for like in all_likes:
                    print(yellow("     Username: ") + like + ". ID: " + str(index))
                    index = index + 1

                # Verificar índice
                try:
                    # Índice
                    index = int(
                        messageInput("Por favor, ingrese el ID del comentario: ")
                    )

                    # Username
                    username_like = all_likes[index]

                    # Buscar perfil
                    self.search_with_index(username_like)

                except:
                    custom_error("ERROR! Entrada no válida")

            else:
                custom_error("ERROR! El ID es inválido")

        else:
            custom_error("ERROR! El usuario no existe")

    def list_of_comments(self, current_user: dict):
        message("Primero, se solicita el username del usuario. Segundo, se solicita la fecha del post a visualizar y por último elegir que perfil visitar")
        founded_user = messageInput("Por favor, ingrese el username del usuario: ")
        founded_user = search_user_with_username(founded_user)

        if founded_user != None:
            self.show_posts(founded_user)
            id_post = self.select_post(founded_user)

            if id_post != None:
                post = get_post(id_post)
                all_coments: list[dict] = post.get("comments")
                
                message("Usuarios:")
                if all_coments == []:
                    print("     -La publicación no tiene comentarios")
                    return
                index = 0
                for comment in all_coments:
                    print(
                        yellow("     Username: ")
                        + comment.get("username")
                        + ". ID: "
                        + str(index)
                    )
                    index = index + 1

                # Verificar índice
                try:
                    # Índice
                    index = int(messageInput("Por favor, ingrese el ID del comentario: ").strip())

                    # Username
                    username_like = all_coments[index].get("username")

                    # Buscar perfil
                    self.search_with_index(username_like)

                except:
                    custom_error("ERROR! Entrada no válida")

            else:
                custom_error("ERROR! El ID es inválido")

        else:
            custom_error("ERROR! El usuario no existe")


class InteractionsFunctions(InteractionsFunctionsExtension):
    """
    1. (A) puede seguir a (B)
    """
    def follow(self, current_user: dict):
        compareer_user = (messageInput("Por favor, ingrese el username: ").strip().replace("@", ""))
        compareer_user = search_user_with_username(compareer_user)

        if compareer_user != None:
            self.aux_follow(current_user, compareer_user)
            print(green(f"Usted en este momento está siguiendo a {compareer_user.get('username')}"))

        else:
            custom_error("ERROR! El usuario no existe")

    """
        2. (A) dejar de seguir a (B)
    """
    def unfollow(self, current_user: dict):
        compareer_user = (messageInput("Por favor, ingrese el username: ").strip().replace("@", ""))
        compareer_user = search_user_with_username(compareer_user)

        if compareer_user != None:
            self.aux_unfollow(current_user, compareer_user)
            print(green(f"Usted en este momento ya no está siguiendo a {compareer_user.get('username')}"))

        else:
            custom_error("ERROR! El usuario no existe")

    """
        3. (A) comentar post de (B)
    """
    def comment(self, current_user: dict):
        founded_user = (messageInput("Por favor, ingrese el username: ").strip().replace("@", ""))
        founded_user = search_user_with_username(founded_user)

        if founded_user != None:
            self.show_posts(founded_user)
            post_id: dict = self.select_post(founded_user)

            if post_id != None:
                c = messageInput("Por favor, ingrese el comentario: ")
                self.save_comment(post_id, current_user, c)
                print(green(f"El comentario ha sido enviado a la publicación de {founded_user.get('username')}, ID de la publicación {post_id}"))

        else:
            custom_error("ERROR! El usuario no existe")

    """
        4. (A) likear post de (B)
    """
    def like(self, current_user: dict):
        founded_user = (messageInput("Por favor, ingrese el username: ").strip().replace("@", ""))
        founded_user = search_user_with_username(founded_user)

        if founded_user != None:
            self.show_posts(founded_user)
            post_id = self.select_post(founded_user)
            if post_id == None:
                return

            post = get_post(post_id)
            all_likes: list = post.get("likes")

            # Si no tiene el like...
            if current_user.get("username") not in all_likes:
                all_likes.append(current_user.get("username"))
                post.update({"likes": all_likes})
                update_post(post)
                print(green(f"Le ha dado like a la publicación de {founded_user.get('username')}, ID de la publicación {post_id}"))

            # Si ya tiene el like...
            else:
                all_likes.remove(current_user.get("username"))
                post.update({"likes": all_likes})
                update_post(post)
                print(green(f"Le ha dado quitado el like a la publicación de {founded_user.get('username')}, ID de la publicación {post_id}"))

        else:
            custom_error("ERROR! El usuario no existe")

    """
        5. (A) elimina un comentario de su post
    """
    def detele_comment(self, current_user: dict):
        self.show_posts(current_user)
        post_id = self.select_post(current_user)
        if post_id == None:
            return

        # Presentación
        print(yellow("Comentarios: "))
        post = get_post(post_id)
        comments: list[dict] = post.get("comments")
        if comments == []:
            print(f"     -Sin comentarios")
            return

        # Comentarios
        index = 0
        for comment in comments:
            print(f"     {yellow('ID:')} {index}")
            print(f"     {yellow('Username:')} {comment.get('username')}")
            print(f"     {yellow('Comentario:')} {comment.get('comment')}")
            print(f"     {yellow('Fecha:')} {comment.get('date')[0:10]}")
            print(f"     --------------------")
            index = index + 1

        # Solicitar index
        del_index = int(messageInput("Por favor, escriba el ID del comentario a eliminar: ").strip())
        try:
            comments.pop(del_index)
            post.update({"comments": comments})
            update_post(post)

        except:
            custom_error("ERROR! El ID del comentario no existe")

    """
        (A) acceder al perfil de otro usuario desde: [a. Lista de likes] [b. Lista de comments]
    """
    def access_to(self, current_user: dict):
        select = messageInput(
            "Por lista de likes de una publicación (1), Por lista de comentarios de una publicación (2): "
        ).strip()

        if select == "1":
            self.list_of_likes(current_user)

        elif select == "2":
            self.list_of_comments(current_user)

        else:
            default_error()


class Interactions(InteractionsFunctions):
    """
    MENU MESSAGE APP
    """
    def __menuMessage(self) -> None:
        print(cyan("1: SEGUIR A UN USUARIO"))
        print(cyan("2: DEJAR DE SEGUIR A UN USUARIO"))
        print(cyan("3: COMENTAR POST DE UN USUARIO"))
        print(cyan("4: LIKE A UN POST DE UN USUARIO"))
        print(cyan("5: ELIMINAR COMENTARIO DE MI POST"))
        print(cyan("6: ACCEDER AL PERFIL DE OTRO USUARIO DESDE OTROS MÉTODOS"))
        # ------------------------------
        print(magenta("0: SALIR"))

    """
        El propósito de esta función es iniciar el módulo de gestión de interacciones desplegando el menú
        con funciones que permiten que la aplicación sea interactiva entre los usuarios
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
            opt = messageInput("Ingrese una opción (1/2/3/4/5/6/0): ").strip()

            match opt:
                case "1":
                    self.follow(user)

                case "2":
                    self.unfollow(user)

                case "3":
                    self.comment(user)

                case "4":
                    self.like(user)

                case "5":
                    self.detele_comment(user)

                case "6":
                    self.access_to(user)

                case "0":
                    menuLoop = False

                case _:
                    default_error()
