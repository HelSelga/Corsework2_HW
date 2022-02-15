import json


def get_posts_all():
    """
    Возвращает посты
    :return: список постов
    """
    with open('data/data.json', "r", encoding="utf-8") as f:
        posts = json.load(f)

    if posts:
        return posts
    else:
        return []


def get_posts_by_user(user_name):
    """
    Выполняет поиск и возвращает посты определенного пользователя
    :param user_name: имя пользователя, посты которого хотим найти
    :return: список постов определенного пользователя
    """
    posts = get_posts_all()
    posts_by_user = []
    for post in posts:
        if post['poster_mame'] == user_name:
            posts_by_user.append(post)

    return posts_by_user


def search_for_posts(query):
    """
    Возвращает список словарей по вхождению query
    :param query:
    :return:
    """
    posts = get_posts_all()
    posts_match = []
    query_lower = query.lower()
    for post in posts:
        if query_lower in post['content'].lower():
            posts_match.append(post)

    return posts_match


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору
    :param pk:
    :return:
    """
    posts = get_posts_all()

    for post in posts:
        if post['pk'] == pk:
            return post
