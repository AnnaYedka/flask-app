from typing import List
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .user import User
from .type_annotations import bigint_pk, bigint, str_100
from .user_saved_recipe import user_saved_recipe


class Recipe(Base):
	__tablename__ = "recipe"

	id: Mapped[bigint_pk]
	title: Mapped[str_100]
	description: Mapped[str] = mapped_column(Text)
	author_id: Mapped[bigint] = mapped_column(ForeignKey("user.id"))
	author: Mapped[User] = relationship(back_populates="recipes")

	users: Mapped[User] = relationship(secondary=user_saved_recipe, back_populates="saved_recipes")
	ingredients: Mapped[List["RecipeIngredient"]] = relationship(back_populates="recipe")
