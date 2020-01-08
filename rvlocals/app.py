from flask import Flask


def create_app(app):
    app = Flask(__name__)

    # Blueprint

    from rvlocals.blueprints.core import bp as bp_core
    bp_core.config(app)

    return app
