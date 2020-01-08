import pytest

from rvlocals.app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def cliente(app):
    with app.test_cliente() as clie:
        yield clie
