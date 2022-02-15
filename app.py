from flask import Flask, request, render_template

from utils import get_posts_all, get_posts_by_user, get_post_by_pk, search_for_posts

app = Flask(__name__)


@app.route('/')
def get_posts():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_id>')
def posts_view(post_id):
    pass



@app.route('/search')
def search_posts_by_word():
    pass


@app.route('/users/<username>')
def search_posts_by_username(username):
    pass



if __name__ == "__main__":
    app.run()
