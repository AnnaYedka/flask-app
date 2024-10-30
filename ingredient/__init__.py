from flask import Blueprint

bp = Blueprint('ingredient', __name__, url_prefix='/ingredient')

from . import routes
