from util.database import *
from util.utils import *
from util.error import *
from modules.extra.graphic import *
from simple_colors import *

class StadisticsFunctionsExtension:
    def get_top_10_users(self) -> list[dict]:
        top_list_aux = {}
        top_list: list[dict] = []
        posts_json_data = get_posts_json()

        # Organizando índice
        for post in posts_json_data:
            post_owner = search_user_with_id(post.get("publisher")).get("username")

            if top_list_aux.get(post_owner) == None:
                top_list_aux[post_owner] = 1

            else:
                top_list_aux[post_owner] = top_list_aux.get(post_owner) + 1

        for user, num in top_list_aux.items():
            doc = {"username": user, "num_posts": num}
            top_list.append(doc)

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num_posts"], reverse=True)
        top_list = top_list[0:10]

        return top_list
    
    def get_top_10_careers(self) -> list[dict]:
        top_list_aux = {}
        top_list: list[dict] = []
        users_json_data = get_user_json()
        posts_json_data = get_posts_json()

        for post in posts_json_data:
            user = search_user_with_id(post.get("publisher"))
            username = user.get("username")
            career = get_career_with_username(username)

            if career != None:
                if top_list_aux.get(career) == None:
                    top_list_aux[career] = 1

                else:
                    top_list_aux[career] = top_list_aux.get(career) + 1

        for career, num in top_list_aux.items():
            doc = {"career": career, "num_posts": num}
            top_list.append(doc)

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num_posts"], reverse=True)
        top_list = top_list[0:10]

        return top_list

    def get_top_10_posts_with_more_interactions(self) -> list[dict]:
        top_list_aux = {}
        top_list: list[dict] = []
        posts_json_data = get_posts_json()

        for post in posts_json_data:
            post_id = post.get("post_id")
            post_owner: str = search_user_with_id(post.get("publisher")).get("username")
            post_total_reactions = len(post.get("likes")) + len(post.get("comments"))
            doc = {
                "post_id": post_id,
                "username": post_owner,
                "num_interactions": post_total_reactions,
            }
            top_list.append(doc)

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num_interactions"], reverse=True)
        top_list = top_list[0:10]

        return top_list

    def get_top_10_users_with_more_interactions(self) -> list[dict]:
        aux_list = []
        top_list: list[dict] = []
        posts_json_data = get_posts_json()

        # Post x Post... All reactions (like and comment) of user
        for post in posts_json_data:
            comments: list[dict] = post.get("comments")
            likes: list[str] = post.get("likes")

            # Comments
            for comment in comments:
                username = comment.get("username")

                # Si el usuario no está el la aux list (Lista de ayuda para simplificar el algoritmo)
                if username not in aux_list:
                    aux_list.append(username)
                    doc = {"username": username, "num_interactions": 0}
                    top_list.append(doc)

                # Quiere decir que ya está en el top_list
                else:
                    doc = {}
                    aux_interactions = 0

                    # Busca el doc
                    for aux_doc in top_list:
                        if aux_doc.get("username") == username:
                            doc = aux_doc
                            aux_interactions = aux_doc.get("num_interactions")
                            break

                    # Actualiza el doc
                    doc.update({"num_interactions": aux_interactions + 1})

            # Likes
            for like in likes:
                username = like

                # Si el usuario no está el la aux list (Lista de ayuda para simplificar el algoritmo)
                if username not in aux_list:
                    aux_list.append(username)
                    doc = {"username": username, "num_interactions": 0}
                    top_list.append(doc)

                # Quiere decir que ya está en el top_list
                else:
                    doc = {}
                    aux_interactions = 0

                    # Busca el doc
                    for aux_doc in top_list:
                        if aux_doc.get("username") == username:
                            doc = aux_doc
                            aux_interactions = aux_doc.get("num_interactions")
                            break

                    # Actualiza el doc
                    doc.update({"num_interactions": aux_interactions + 1})

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num_interactions"], reverse=True)
        top_list = top_list[0:10]

        return top_list

    def get_top_10_users_with_eliminated_posts(self) -> list[dict]:
        top_list_aux = {}
        top_list: list[dict] = []
        users = get_user_json()
        posts = get_eliminated_posts_json()

        # Extraer usuarios y cantidad de posts eliminados
        for post in posts:
            post_id = post.get("publisher")

            for user in users:
                user_id = user.get("id")
                user_username = user.get("username")

                # Conseguir el dueño del post
                if post_id == user_id:
                    # Si no está (Nueva entrada)
                    if top_list_aux.get(user_username) == None:
                        top_list_aux[user_username] = 1

                    # Si ya está
                    else:
                        top_list_aux[user_username] = (
                            top_list_aux.get(user_username) + 1
                        )

        # Agregar de la lista aux a la lista a retornar
        for user, num in top_list_aux.items():
            doc = {"username": user, "num_posts": num}
            top_list.append(doc)

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num_posts"], reverse=True)
        top_list = top_list[0:10]

        return top_list

    def get_top_10_careers_with_inapropiate_comments(self) -> list[dict]:
        top_list_aux = {}
        top_list: list[dict] = []
        posts = get_posts_json()

        # Extraer usuarios y cantidad de comentarios eliminados
        for post in posts:
            all_deleted_comments: list[dict] = post.get("comments_delete")

            for deleted_comment in all_deleted_comments:
                username = deleted_comment.get("username")
                career = get_career_with_username(username)

                # Si no está (Nueva entrada)
                if top_list_aux.get(career) == None:
                    top_list_aux[career] = 1

                # Si ya está
                else:
                    top_list_aux[career] = top_list_aux.get(career) + 1

        # Agregar de la lista aux a la lista a retornar
        for career, num in top_list_aux.items():
            if career != None:
                doc = {"career": career, "num_posts": num}
                top_list.append(doc)

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num_posts"], reverse=True)
        top_list = top_list[0:10]

        return top_list

    def get_top_10_reasons_ban(self) -> list[dict]:
        top_list_aux = {}
        top_list: list[dict] = []
        ban_users = get_ban_users_json()

        # Extraer usuarios y cantidad de comentarios eliminados
        for user in ban_users:
            reason = user.get("reason")

            # Nueva entrada
            if top_list_aux.get(reason) == None:
                top_list_aux[reason] = 1

            # Actualizar dato
            else:
                top_list_aux[reason] = top_list_aux.get(reason) + 1

        # Agregar de la lista aux a la lista a retornar
        for reason, num in top_list_aux.items():
            doc = {"reason": reason, "num": num}
            top_list.append(doc)

        # Organizar top 10
        top_list = sorted(top_list, key=lambda i: i["num"], reverse=True)
        top_list = top_list[0:10]

        return top_list

    def get_quantity_bans(self) -> int:
        return len(get_ban_users_json())

class StadisticsFunctions(StadisticsFunctionsExtension):
    """
    A
    """
    def report_posts(self):
        # Seleccionar qué ver
        select = messageInput("Usuarios con más publicaciones (1), Carreras con más publicaciones (2): ").strip()

        if select == "1":
            # Top 10 usuarios... cantidad de publicaciones
            top_users = self.get_top_10_users()
            message("Los usuarios con más publicaciones son: ")
            for user in top_users:
                print("     " + yellow("Username: ") + user.get("username"))
                print("     " + yellow("Posts: ") + str(user.get("num_posts")))
                print("     " + "--------------------")
        elif select == "2":
            # Top 10 carreras... cantidad de publicaciones
            top_careers = self.get_top_10_careers()
            message("Las carreras con más publicaciones son: ")
            for post in top_careers:
                print("     " + yellow("Carrera: ") + post.get("career"))
                print("     " + yellow("Posts: ") + str(post.get("num_posts")))
                print("     " + "--------------------")
        else:
            default_error()

    """
    A
    """
    def report_interactions(self):
        # Seleccionar qué ver
        select = messageInput("Posts con más interacciones (1), Usuarios con más interacciones (2): ").strip()

        if select == "1":
            # Top 10 posts... cantidad de interacciones
            top_posts = self.get_top_10_posts_with_more_interactions()
            message("Los posts con más interacciones son: ")
            for post in top_posts:
                print("     " + yellow("Post ID: ") + post.get("post_id"))
                print("     " + yellow("Owner: ") + post.get("username"))
                print(
                    "     "
                    + yellow("Interacciones: ")
                    + str(post.get("num_interactions"))
                )
                print("     " + "--------------------")
        elif select == "2":
            # Top 10 usuarios... cantidad de interacciones
            top_users = self.get_top_10_users_with_more_interactions()
            message("Las usuarios con más interacciones son: ")
            for user in top_users:
                print("     " + yellow("Username: ") + user.get("username"))
                print(
                    "     "
                    + yellow("Interacciones: ")
                    + str(user.get("num_interactions"))
                )
                print("     " + "--------------------")
        else:
            default_error()

    """
    A
    """
    def report_moderation(self):
        # Seleccionar que ver
        select = messageInput("Ver top 10 usuarios con más posts eliminados (1). Ver top 10 carreras con mayor cantidad de comentarios inadecuados (2). Ver top 10 razones más comunes por suspensión de cuenta (3): ")

        # Selección
        if select == "1":
            # Usuarios con la mayor cantidad de post eliminados
            top_users_elimnated_posts = self.get_top_10_users_with_eliminated_posts()
            message("Los usuarios con más posts eliminados son: ")
            for user in top_users_elimnated_posts:
                print("     " + yellow("Username: ") + user.get("username"))
                print("     " + yellow("Cantidad: ") + str(user.get("num_posts")))
                print("     " + "--------------------")
        elif select == "2":
            # Carreras con mayor comentarios inadecuados
            top_careers_inapropiated_comments = (
                self.get_top_10_careers_with_inapropiate_comments()
            )
            message("Las carreras con mayor cantidad de comentarios eliminados son: ")
            for careers in top_careers_inapropiated_comments:
                print("     " + yellow("Carrera: ") + careers.get("career"))
                print("     " + yellow("Cantidad: ") + str(careers.get("num_posts")))
                print("     " + "--------------------")
        elif select == "3":
            # Usuarios eliminados por infracciones
            top_reasons_bans = self.get_top_10_reasons_ban()
            message("Las razones más comunes de suspensión de cuenta son: ")
            for reason in top_reasons_bans:
                print("     " + yellow("Razón: ") + reason.get("reason"))
                print("     " + yellow("Cantidad: ") + str(reason.get("num")))
                print("     " + "--------------------")
        else:
            default_error()

    """
    """
    def reports_graphic(self):
        message_ = cyan("""1: Usuarios con más publicaciones
2: Carreras con más publicaciones
3: Posts con más interracciones
4: Usuarios con más interacciones
5: Usuarios con más posts tumbados
6: Carreras con mayor cantidad de comentarios inadecuados
7: Cantidad de usuarios baneados por infracción""".upper())
        print(message_)
        select = messageInput("Seleccione la opción que quiera colocando el número correspondiente: ").strip()
        
        match select:
            case "1":
                graphic_top_users_more_posts(self.get_top_10_users())
            
            case "2":
                graphic_top_careers_more_posts(self.get_top_10_careers())
            
            case "3":
                graphic_top_posts_more_interactions(self.get_top_10_posts_with_more_interactions())
            
            case "4":
                graphic_top_users_more_interactions(self.get_top_10_users_with_more_interactions())
            
            case "5":
                graphic_top_users_eliminated_posts(self.get_top_10_users_with_eliminated_posts())
            
            case "6":
                graphic_top_careers_more_inapropiated_comments(self.get_top_10_careers_with_inapropiate_comments())
                
            case "7":
                graphic_top_reasons_more_common_of_ban(self.get_top_10_reasons_ban())
            
            case _:
                default_error()
        

class Stadistics(StadisticsFunctions):
    """
    MENU MESSAGE APP
    """
    def __menuMessage(self) -> None:
        print(cyan("1: INFORME DE PUBLICACIONES"))
        print(cyan("2: INFORME DE INTERACCIÓN"))
        print(cyan("3: INFORME DE MODERACIÓN"))
        print(cyan("4: GRÁFICO DE ESTADÍSTICAS"))
        # ------------------------------
        print(magenta("0: SALIR"))

    """
        El propósito de esta función es iniciar el módulo de estadísticas que permite ver los movimientos
        y datos que se almacenan en la aplicación
    """
    def start(self):
        menuLoop = True
        while menuLoop:
            self.__menuMessage()
            opt = messageInput("Ingrese una opción (1/2/3/4/0): ").strip()

            match opt:
                case "1":
                    self.report_posts()

                case "2":
                    self.report_interactions()

                case "3":
                    self.report_moderation()

                case "4":
                    self.reports_graphic()

                case "0":
                    menuLoop = False

                case _:
                    default_error()
