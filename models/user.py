from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .base import Base
from .role import Role
from .type_annotations import bigint_pk, smallint, str_100
from .user_saved_recipe import user_saved_recipe


class User(UserMixin, Base):
	__tablename__ = "user"

	id: Mapped[bigint_pk]
	email: Mapped[str_100] = mapped_column(unique=True)
	username: Mapped[str_100]
	password: Mapped[str] = mapped_column(String(256))
	role_id: Mapped[smallint] = mapped_column(ForeignKey('role.id'))
	role: Mapped[Role] = relationship(back_populates="users")
	recipes: Mapped[List["Recipe"]] = relationship(back_populates="author")
	saved_recipes: Mapped[List["Recipe"]] = relationship(secondary=user_saved_recipe)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)
