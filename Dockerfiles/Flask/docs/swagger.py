from pathlib import Path

from flask import Blueprint, render_template

from config.flask_config import FLASK_PATH

swagger_blueprint = Blueprint(
    "swagger_blueprint", __name__, url_prefix="/docs",
    template_folder=str(
        Path(str(Path.cwd()) + FLASK_PATH.get("swagger_template_folder"))),
    static_folder=str(
        Path(str(Path.cwd()) + FLASK_PATH.get("swagger_static_folder")))
)


@swagger_blueprint.route("/swagger", methods=["GET"])
async def swagger_doc():
    return render_template('swagger_ui.html')
