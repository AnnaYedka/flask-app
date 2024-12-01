from typing import List
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .type_annotations import smallint_pk


class Role(Base):
	__tablename__ = "role"

	id: Mapped[smallint_pk]
	name: Mapped[str] = mapped_column(String(10), unique=True)
	users: Mapped[List["User"]] = relationship("User", back_populates="role")
