import os
from typing import List, Union

from flask import Flask, Blueprint

from Dockerfiles.Flask.re_edge_gpt_blueprint import re_edge_gpt_blueprint_instance


def create_app(blueprint_list: Union[List[Blueprint], None] = None) -> Flask:
    flask_app = Flask(__name__)
    if blueprint_list is not None:
        for blueprint in blueprint_list:
            flask_app.register_blueprint(blueprint)

    return flask_app


if __name__ == "__main__":
    # Init Flask with blueprint
    blueprints = [re_edge_gpt_blueprint_instance]
    app = create_app(blueprints)
    # Create new secret key using urandom 24
    app.secret_key = os.urandom(24)


    @app.route("/", methods=["GET"])
    async def index():
        return "INDEX"


    app.run(port=8888, debug=True)
else:
    # Init Flask with blueprint
    blueprints = [re_edge_gpt_blueprint_instance]
    app = create_app(blueprints)
    # Create new secret key using urandom 24
    app.secret_key = os.urandom(24)


    @app.route("/", methods=["GET"])
    async def index():
        return "INDEX"
