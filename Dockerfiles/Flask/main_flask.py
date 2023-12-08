import os

from flask import Flask
from flask_cors import CORS

from Dockerfiles.Flask.re_edge_gpt_blueprint import re_edge_gpt_blueprint_instance
from Dockerfiles.Flask.swagger_config import bind_swagger


def create_app() -> Flask:
    flask_app = Flask(__name__)
    blueprints = [re_edge_gpt_blueprint_instance]
    for blueprint in blueprints:
        flask_app.register_blueprint(blueprint)

    @flask_app.route("/", methods=["GET"])
    async def index():
        return "INDEX"

    CORS(flask_app)
    bind_swagger(flask_app)

    return flask_app


if __name__ == "__main__":
    # Init Flask with blueprint
    app = create_app()
    # Create new secret key using urandom 24
    app.secret_key = os.urandom(24)
    app.run(port=8888, debug=True)
else:
    app = create_app()
    # Create new secret key using urandom 24
    app.secret_key = os.urandom(24)
