import json


def get_posts_all():
    with open('/data/data.json', "r", encoding="utf-8") as f:
        posts = json.load(f)

    if posts:
        return posts
    else:
        return []


def get_posts_by_user(user_id):
    pass


def search_for_posts(query):
    pass


def get_post_by_pk(pk):
    pass