from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .role import Role
from .type_annotations import bigint_pk, smallint, str_100
from .user_saved_recipe import user_saved_recipe


class User(Base):
	__tablename__ = "user"

	id: Mapped[bigint_pk]
	email: Mapped[str_100] = mapped_column(unique=True)
	username: Mapped[str_100]
	password: Mapped[str] = mapped_column(String(256))
	role_id: Mapped[smallint] = mapped_column(ForeignKey('role.id'))
	role: Mapped[Role] = relationship(back_populates="users")
	recipes: Mapped[List["Recipe"]] = relationship(back_populates="author")
	saved_recipes: Mapped[List["Recipe"]] = relationship(secondary=user_saved_recipe)
