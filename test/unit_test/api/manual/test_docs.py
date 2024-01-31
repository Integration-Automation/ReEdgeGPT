import os

from re_edge_gpt.api.main_flask import create_app

if __name__ == '__main__':
    # Init Flask with blueprint
    app = create_app()
    # Create new secret key using urandom 24
    app.secret_key = os.urandom(24)
    app.run(port=8888, debug=True)
else:
    app = create_app()
    # Create new secret key using urandom 24
    app.secret_key = os.urandom(24)
