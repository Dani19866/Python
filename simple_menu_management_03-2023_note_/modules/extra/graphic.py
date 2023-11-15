import matplotlib.pyplot as plt

# ------------------------------
def graphic_top_users_more_posts(worker: list):
    # Extraer nombres de usuario y número de publicaciones
    usernames = [entry['username'] for entry in worker]
    num_posts = [entry['num_posts'] for entry in worker]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(usernames, num_posts, color='skyblue')
    plt.xlabel('Usuarios')
    plt.ylabel('Número de Publicaciones')
    plt.title('Número de Publicaciones por Usuario')
    plt.xticks(rotation=45, ha='right')  # Rotar nombres de usuario para mejor legibilidad
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

def graphic_top_careers_more_posts(worker: list):
    # Extraer nombres de carrera y número de publicaciones
    careers = [entry['career'] for entry in worker]
    num_posts_careers = [entry['num_posts'] for entry in worker]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(careers, num_posts_careers, color='lightcoral')
    plt.xlabel('Carreras')
    plt.ylabel('Número de Publicaciones')
    plt.title('Número de Publicaciones por Carrera')
    plt.xticks(rotation=45, ha='right')  # Rotar nombres de carrera para mejor legibilidad
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()
# ------------------------------
def graphic_top_posts_more_interactions(worker: list):
    # Extraer identificadores de publicación y número de interacciones
    post_ids = [entry['post_id'] for entry in worker]
    num_interactions_posts = [entry['num_interactions'] for entry in worker]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(post_ids, num_interactions_posts, color='lightgreen')
    plt.xlabel('ID de Publicación')
    plt.ylabel('Número de Interacciones')
    plt.title('Número de Interacciones por Publicación')
    plt.xticks(rotation=45, ha='right')  # Rotar IDs de publicación para mejor legibilidad
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

def graphic_top_users_more_interactions(worker: list):
    # Extraer nombres de usuario y número de interacciones
    usernames_interactions = [entry['username'] for entry in worker]
    num_interactions_users = [entry['num_interactions'] for entry in worker]

    # Crear gráfico de barras horizontal
    plt.figure(figsize=(10, 6))
    plt.barh(usernames_interactions, num_interactions_users, color='salmon')
    plt.xlabel('Número de Interacciones')
    plt.ylabel('Usuarios')
    plt.title('Número de Interacciones por Usuario')
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()
# ------------------------------
def graphic_top_users_eliminated_posts(worker: list):
    # Extraer nombres de usuario y número de publicaciones
    usernames_posts = [entry['username'] for entry in worker]
    num_posts_users = [entry['num_posts'] for entry in worker]

    # Crear gráfico de barras horizontal
    plt.figure(figsize=(10, 6))
    plt.barh(usernames_posts, num_posts_users, color='lightblue')
    plt.xlabel('Número de Publicaciones')
    plt.ylabel('Usuarios')
    plt.title('Número de Publicaciones por Usuario')
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

def graphic_top_careers_more_inapropiated_comments(worker: list):
    # Extraer nombres de carrera y número de publicaciones
    careers_posts = [entry['career'] for entry in worker]
    num_posts_careers = [entry['num_posts'] for entry in worker]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(careers_posts, num_posts_careers, color='lightcoral')
    plt.xlabel('Carreras')
    plt.ylabel('Número de Comentarios')
    plt.title('Número de Comentarios por Carrera')
    plt.xticks(rotation=45, ha='right')  # Rotar nombres de carrera para mejor legibilidad
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

def graphic_top_reasons_more_common_of_ban(worker: list):
    # Extraer razones y número de usuarios baneados
    ban_reasons = [entry['reason'] for entry in worker]
    num_banned_users = [entry['num'] for entry in worker]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(ban_reasons, num_banned_users, color='tomato')
    plt.xlabel('Razón del Baneo')
    plt.ylabel('Número de Usuarios Baneados')
    plt.title('Cantidad de Usuarios Baneados por Razón de Infracción')
    plt.xticks(rotation=45, ha='right')  # Rotar razones para mejor legibilidad
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()
# ------------------------------