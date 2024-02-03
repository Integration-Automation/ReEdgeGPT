from flask import Flask, render_template
from flask_cors import CORS

from re_edge_gpt.api.re_edge_gpt_blueprint import re_edge_gpt_blueprint_instance
from re_edge_gpt.api.swagger_config import bind_swagger


def create_app() -> Flask:
    flask_app = Flask(__name__)
    blueprints = [re_edge_gpt_blueprint_instance]
    for blueprint in blueprints:
        flask_app.register_blueprint(blueprint)

    @flask_app.route("/", methods=["GET"])
    async def index():
        return render_template("index.html")

    CORS(flask_app)
    bind_swagger(flask_app)

    return flask_app
