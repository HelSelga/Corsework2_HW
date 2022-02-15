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
        if post['poster_name'] == user_name:
            posts_by_user.append(post)

    return posts_by_user


def search_for_posts(query):
    """
    Возвращает список словарей по вхождению query
    :param query: поисковое слово
    :return: список постов, куда входит это слово
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


def get_comments_all():
    """
    Возвращает все комментарии всех пользователей
    :return: список комментариев
    """
    with open('data/comments.json', "r", encoding="utf-8") as f:
        comments = json.load(f)

    if comments:
        return comments
    else:
        return []


def get_comments_by_post_pk(pk):
    """
    Возвращает список комментариев определенного пользователя
    :param pk: идентификатор пользователя
    :return: список комментариев этого пользователя
    """
    comments = get_comments_all()
    comments_by_pk = []
    for comment in comments:
        if comment['post_id'] == pk:
            comments_by_pk.append(comment)

    return comments_by_pk


def get_posts_by_tag(tagname):
    posts = get_posts_all()
    post_match = []
    search_object = f'#{tagname}'
    for post in posts:
        if search_object in post['content']:
            post_match.append(post)

    return post_match
