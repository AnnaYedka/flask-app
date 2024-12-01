from typing import List
from sqlalchemy import Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .type_annotations import bigint_pk, str_50


class Ingredient(Base):
	__tablename__ = "ingredient"

	id: Mapped[bigint_pk]
	name: Mapped[str_50] = mapped_column(unique=True)
	is_allergen: Mapped[bool] = mapped_column(Boolean)
	recipes: Mapped[List["Recipe"]] = relationship(secondary="recipe_ingredient")
