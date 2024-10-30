from . import bp
from flask import render_template
from app import db
from models import Ingredient
from typing import List


@bp.route('/')
def index():
	ingredients: List[Ingredient] = db.session.query(Ingredient).all()
	return render_template('ingredient/index.html', ingredients=ingredients)
