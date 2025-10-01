from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hola():
        return "Hola Blog-post"

    return app
