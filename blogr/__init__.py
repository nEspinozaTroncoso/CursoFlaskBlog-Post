from flask import Flask


def create_app():
    app = Flask(__name__)

    from blogr import home, auth, post

    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)

    return app
