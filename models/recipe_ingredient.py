from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .type_annotations import bigint_pk, smallint, bigint


class RecipeIngredient(Base):
	__tablename__ = "recipe_ingredient"

	id: Mapped[bigint_pk]
	amount: Mapped[int]
	unit_id: Mapped[smallint] = mapped_column(ForeignKey('unit.id'))
	unit: Mapped["Unit"] = relationship()
	recipe_id: Mapped[bigint] = mapped_column(ForeignKey("recipe.id"))
	ingredient_id: Mapped[bigint] = mapped_column(ForeignKey("ingredient.id"))

	recipe: Mapped["Recipe"] = relationship(back_populates="ingredients")
	ingredient: Mapped["Ingredient"] = relationship()
