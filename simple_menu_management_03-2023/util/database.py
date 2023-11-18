from simple_colors import *
import json


# READY TO USE
def get_user_json() -> list[dict]:
    # Extracción
    with open("database/users.json") as f:
        return json.loads(f.read())


# READY TO USE
def save_user_json(doc: list[dict]) -> None:
    with open("database/users.json", "w+") as f:
        json.dump(doc, f)


# READY TO USE
def get_posts_json() -> list[dict]:
    # Extracción
    with open("database/posts.json") as f:
        return json.loads(f.read())


# READY TO USE
def save_posts_json(doc: list[dict]) -> None:
    with open("database/posts.json", "w+") as f:
        json.dump(doc, f)


# READY TO USE
def get_ban_users_json() -> list[dict]:
    # Extracción
    with open("database/ban_users.json") as f:
        return json.loads(f.read())


# READY TO USE
def save_ban_users_json(doc: list[dict]) -> None:
    with open("database/ban_users.json", "w+") as f:
        json.dump(doc, f)


# READY TO USE
def get_eliminated_posts_json() -> list[dict]:
    # Extracción
    with open("database/eliminated_posts.json") as f:
        return json.loads(f.read())


# READY TO USE
def save_eliminated_posts_json(doc: list[dict]) -> None:
    with open("database/eliminated_posts.json", "w+") as f:
        json.dump(doc, f)


# READY TO USE
def compareer_email(email: str) -> str | None:
    json_data: list[dict] = get_user_json()

    # Uno x Uno cada usuario
    for user in json_data:
        # Extraer username
        email_compareer = user.get("email")

        # Comparación -> Si son iguales, retornar None
        if email == email_compareer:
            # return "coincidence"
            return None

    # Si no hay ningun problema, retorna username
    return email


# READY TO USE
def compareer_username(username: str) -> str | None:
    json_data = get_user_json()

    # Uno x Uno cada usuario
    for user in json_data:
        # Extraer username
        username_compareer = user.get("username")

        # Comparación -> Si son iguales, retornar 'coincidence'
        if username == username_compareer:
            return None

    # Si no hay ningun problema, retorna username
    return username


# READY TO USE
def save_new_user(doc: dict) -> None:
    json_data: list[dict] = get_user_json()

    # Agregar
    json_data.append(doc)

    # Escribir
    save_user_json(json_data)


# READY TO USE
def update_user(doc: dict) -> None:
    json_data: list[dict] = get_user_json()

    # Buscar
    for user in json_data:
        id_compareer = user.get("id")
        id_current = doc.get("id")

        if id_compareer == id_current:
            user.update(doc)

            # Guardar
            save_user_json(json_data)


# READY TO USE
def del_user(doc: dict) -> None:
    json_data: list[dict] = get_user_json()
    json_data.remove(doc)
    save_user_json(json_data)
    print(green(f"Se han borrado los datos de {doc.get('username')}!"))


# READY TO USE
def search_user_with_username(username: str) -> dict | None:
    json_data: list[dict] = get_user_json()

    # Buscar
    for user in json_data:
        username_compareer = user.get("username")

        if username == username_compareer:
            return user

    # Sin coincidencias
    return None


# READY TO USE
def search_user_with_email(email: str) -> dict | None:
    json_data: list[dict] = get_user_json()

    # Buscar
    for user in json_data:
        email_compareer: str = user.get("email")

        if email.lower() == email_compareer.lower():
            return user

    # Error
    return None


# READY TO USE
def get_post(current_post_id: str) -> dict | None:
    json_data = get_posts_json()

    for post in json_data:
        if post.get("post_id") == current_post_id:
            return post

    return None


# READY TO USE
def update_post(doc: dict) -> None:
    json_data = get_posts_json()

    for post in json_data:
        if post.get("post_id") == doc.get("post_id"):
            # Actualizar
            post.update(doc)

            # Guardar
            save_posts_json(json_data)


# READY TO USE
def search_user_with_id(id: str) -> dict | None:
    json_data: list[dict] = get_user_json()

    # Buscar
    for user in json_data:
        id_compareer: str = user.get("id")

        if id.lower() == id_compareer.lower():
            return user

    # Error
    return None


# READY TO USE
def del_post(doc: dict) -> None:
    json_data = get_posts_json()
    json_data.remove(doc)
    save_posts_json(json_data)


# READY TO USE
def get_career_with_username(username: str) -> str:
    users = get_user_json()
    for user in users:
        if user.get("username") == username and user.get("major") != None:
            return user.get("major")
