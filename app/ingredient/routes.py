from . import bp
from flask import render_template, redirect, url_for
from app import db
from models import Ingredient
from typing import List
from .form import IngredientForm
from flask_login import login_required
from auth import admin_required


@bp.route('/', methods=['GET', 'POST'])
def index():
	form = IngredientForm()
	if form.validate_on_submit():
		db.session.add(Ingredient(name=form.name.data, is_allergen=form.is_allergen.data))
		db.session.commit()
		return redirect(url_for('.index'))
	ingredients: List[Ingredient] = db.session.query(Ingredient).all()
	return render_template('ingredient/index.html', ingredients=ingredients, form=form)


@bp.route('/protected_view')
@login_required
@admin_required
def protected_view():
	return 'logged in'
