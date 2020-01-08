from .bp import bp


@bp.route('/')
def home():
    return "home"
