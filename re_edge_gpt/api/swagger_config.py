from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, Blueprint, render_template


def write_swagger_doc(openapi_yaml_content: str):
    with open("openapi.yaml", "w+") as openapi_file:
        openapi_file.write(openapi_yaml_content)


def bind_swagger(flask_app: Flask):
    from re_edge_gpt.api.re_edge_gpt_blueprint import chat
    from re_edge_gpt.api.re_edge_gpt_blueprint import image

    flask_api_docs_view = [
        chat, image
    ]

    spec = APISpec(
        title="ReEdgeGPT Example API Doc",
        version="1.0.0",
        openapi_version="3.0.2",
        servers=[{"url": "http://localhost:8888"}],
        plugins=[FlaskPlugin()]
    )

    with flask_app.app_context():
        for doc_view in flask_api_docs_view:
            spec.path(view=doc_view)

    write_swagger_doc(spec.to_yaml())
