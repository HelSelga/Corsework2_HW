from flask import Flask, request, render_template

from utils import get_posts_all, get_posts_by_user, get_post_by_pk, search_for_posts, get_comments_by_post_pk, get_posts_by_tag

app = Flask(__name__)


@app.route('/')
def get_posts():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_id>')
def page_post(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_pk(post_id)
    comments_count = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_count=comments_count)


@app.route('/search/')
def search_posts_by_word():
    query = request.args.get('s')
    if query:
        posts = search_for_posts(query)
        posts_count = len(posts)
    else:
        posts = []
        posts_count = 0
        query = "empty"

    return render_template('search.html', posts=posts, posts_count=posts_count, query=query)


@app.route('/users/<username>')
def search_posts_by_username(username):
    posts = get_posts_by_user(username)
    posts_count = len(posts)
    return render_template('user-feed.html', posts=posts, posts_count=posts_count, username=username)


@app.route('/tag/<tagname>')
def posts_by_tags(tagname):
    posts = get_posts_by_tag(tagname)
    return render_template('tag.html', posts=posts, tagname=tagname)


if __name__ == "__main__":
    app.run(debug=True)
