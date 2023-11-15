from util.database import *
from util.error import *
from util.utils import *
import json

class ModerationFunctionsExtension:
    def save_eliminated_comment(self, post: dict, doc_comment: dict):
        comments_delete: list[dict] = post.get("comments_delete")
        comments_delete.append(doc_comment)
        update_post(post)
    
    def save_eliminated_post(self, post: dict) -> None:
        # Archivo de post eliminado
        doc = {
            "publisher": post.get("publisher"),
            "post_id": post.get("post_id"),
            "type": post.get("type"),
            "date": post.get("date"),
            "url": post.get("multimedia").get("url"),
            "interactions": {
                "comments": post.get("comments"),
                "likes": post.get("likes")
            }
        }

        # Crear la carpeta y guardar datos...        
        if os.path.exists("database/eliminated_posts.json") == False:
            doc_adapted = [doc]
            with open("database/eliminated_posts.json", "w+") as f:
                json.dump(doc_adapted, f)
            
        else:
            json_data = get_eliminated_posts_json()
            json_data.append(doc)
            save_eliminated_posts_json(json_data)
    
    def del_likes(self, current_user: dict):
        json_data = get_posts_json()
        
        # Publicación x ...
        for post in json_data:
            # Todos los likes de la publicación
            all_likes: list[str] = post.get("likes")
            
            if all_likes != []:
                # Uno x ...
                for like in all_likes:
                    if like == current_user.get("username"):
                        all_likes.remove(like)
                        
                # Actualizar y guardar
                post.update({"likes": all_likes})

        # Guardar
        save_posts_json(json_data)
    
    def del_comments(self, current_user: dict):
        json_data = get_posts_json()
        
        # Publicación x ...
        for post in json_data:
            # Todos los comentarios de la publicación
            all_comments: list[dict] = post.get("comments")
            
            if all_comments != []:
                # Uno x ...
                for comment in all_comments:
                    owner_comment = comment.get("username")
                    
                    if owner_comment == current_user.get("username"):
                        all_comments.remove(comment)
                
                # Actualizar y guardar
                post.update({"comments": all_comments})
        
        # Guardar
        save_posts_json(json_data)
        
    def del_posts(self, current_user: dict):
        json_data = get_posts_json()
        all_posts: list[dict] = []
        
        for post in json_data:
            post_user = post.get("publisher")
            
            if post_user == current_user.get("id"):
                all_posts.append(post)
        
        for post in all_posts:
            # Eliminar post
            json_data.remove(post)
            
            # Registrar post en el archivo específico
            self.save_eliminated_post(post)
            
            
        # Guardar
        save_posts_json(json_data)
    
    def del_account_aux(self, current_user: dict, reason: str = "N/A"):
        json_data = get_user_json()
        json_data.remove(current_user)
        save_user_json(json_data)
        
        # Archivo de usuarios baneados
        doc = {
            "username": current_user.get("username"),
            "id": current_user.get("id"),
            "email": current_user.get("email"),
            "reason": reason
        }

        # Agregar a lista de usuarios eliminados (baneados)
        json_data = get_ban_users_json()
        json_data.append(doc)
        save_ban_users_json(json_data)

    def del_algorithm(self, user: dict, reason) -> None:
        self.del_likes(user)
        # print(green("Se han eliminado todos los likes..."))
        
        self.del_comments(user)
        # print(green("Se han eliminado todos los comentarios..."))
        
        self.del_posts(user)
        # print(green("Se han eliminado todos los posts..."))
        
        if reason == "":
            self.del_account_aux(user)
        else:
            self.del_account_aux(user, reason)
        

class ModerationFunctions(ModerationFunctionsExtension):
    """
        Esta función permite borrar la publicación de un usuario
        
        El orden es el siguiente:
            1. Solicitar el username del usuario propietario del post
            2. Solicitar el ID de la publicación (fecha)
            3. Se comparará si la publicación es del usuario
                3.1. Se elimina la publicación
    """
    def del_post(self):
        user = messageInput("Por favor ingrese el username del usuario: ").strip().replace("@", "")
        user = search_user_with_username(user)
        
        if user != None:
            post_id = messageInput("Ingrese el ID de la publicación: ").strip()
            post = get_post(post_id)
            
            if post != None:
                if post.get("publisher") == user.get("id"):
                    del_post(post)
                    print(green("Se ha eliminado la publicación con éxito!"))
                else:
                    custom_error("ERROR! La publicación no es del usuario introducido")
            
            else:
                custom_error("ERROR! La publicación no existe")
        
        else:
            custom_error("ERROR! El usuario no existe")

    """
        Esta función permite borrar el comentario de un usuario de una publicación
        
        El orden es el siguiente:
            1. Solicitar el username del usuario propietario del post
            2. Solicitar el ID de la publicación (fecha)
            3. Se comparará si la publicación es del usuario
                3.1. Se mostrará los comentarios
                3.2. Se solicitará el ID del comentario a borrar
                3.3. Se borrará el comentario de la publicación
    """
    def del_comment(self):
        # 1. El USERNAME del dueño del post
        # 2. El ID del post
        # 3. El ID del comentario
        user = messageInput("Por favor ingrese el username del usuario: ").strip().replace("@", "")
        user = search_user_with_username(user)
        
        if user != None:
            post_id = messageInput("Ingrese el ID de la publicación: ").strip()
            post = get_post(post_id)
            
            if post != None:
                if post.get("publisher") == user.get("id"):
                    # Mostar comentarios
                    comments: list[dict] = post.get("comments")
                    index = 0
                    print(yellow("Comentarios: "))
                    if comments == []:
                        print(f"     -Sin comentarios")
                        return
                    for comment in comments:
                        print(f"     {yellow('ID:')} {index}")
                        print(f"     {yellow('Username:')} {comment.get('username')}")
                        print(f"     {yellow('Comentario:')} {comment.get('comment')}")
                        print(f"     {yellow('Fecha:')} {comment.get('date')[0:10]}")
                        print(f"     --------------------")
                        index = index + 1
                    
                    # Solicitar ID comentario
                    req_index = int(messageInput("Escriba el ID del comentario a eliminar: "))
                    
                    # Eliminar comentario
                    try:
                        self.save_eliminated_comment(post, comments[req_index])
                        comments.pop(req_index)
                        post.update({"comments": comments})
                        update_post(post)
                        print(green("Se ha eliminado el comentario con éxito!"))

                    except:
                        custom_error("ERROR! El ID del comentario no existe")
                    
                   
                    
                else:
                    custom_error("ERROR! La publicación no es del usuario introducido")
            else:
                custom_error("ERROR! La publicación no existe")
        else:
            custom_error("ERROR! El usuario no existe")

    """
    A
    """
    def del_account(self):
        user = messageInput("Por favor ingrese el username del usuario: ")
        user = search_user_with_username(user)
        
        if user != None:
            message("Se van a eliminar los likes, comentarios y publicaciones de este usuario")
            select = messageInput("Está usted seguro que desea eliminarlo? (S/N): ").strip()
            reason = messageInput("¿Cuál es la razón del ban? Si no desea responder presione ENTER: ").strip()
            
            if select == "S":
                self.del_algorithm(user, reason)
                print(green("Se ha eliminado la cuenta y todo lo relacionado con éxito!"))
        
        else:
            custom_error("ERROR! El usuario no existe")


class Moderation(ModerationFunctions):
    """
    MENU MESSAGE APP
    """
    def __menuMessage(self) -> None:
        print(cyan("1: ELIMINAR UN POST"))
        print(cyan("2: ELIMINAR UN COMENTARIO"))
        print(cyan("3: ELIMINAR UNA CUENTA"))
        # ------------------------------
        print(magenta("0: SALIR"))

    """
        El propósito de esta función es iniciar el módulo de gestión de moderación desplegando el menú con distintas opciones
        para el administrador o moderador de la aplicación
    """
    def start(self):
        menuLoop = True
        while menuLoop:
            self.__menuMessage()
            opt = messageInput("Ingrese una opción (1/2/3/0): ")

            match opt:
                case "1":
                    self.del_post()

                case "2":
                    self.del_comment()

                case "3":
                    self.del_account()

                case "0":
                    menuLoop = False

                case _:
                    default_error()
