from flask import Blueprint

bp = Blueprint('ingredient', __name__)

from . import routes
