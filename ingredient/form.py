from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SubmitField


class IngredientForm(FlaskForm):
	name = StringField("name", (validators.data_required(), validators.length(max=50)))
	is_allergen = BooleanField("is allergen")

	save = SubmitField("save")
