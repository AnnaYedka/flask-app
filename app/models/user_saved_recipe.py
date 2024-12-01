from sqlalchemy import Table, Column, ForeignKey
from .base import Base

user_saved_recipe = Table(
	"user_saved_recipe",
	Base.metadata,
	Column("user_id", ForeignKey("user.id"), primary_key=True),
	Column("recipe_id", ForeignKey("recipe.id"), primary_key=True),
)
