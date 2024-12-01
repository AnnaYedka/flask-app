from sqlalchemy.orm import Mapped

from .base import Base
from .type_annotations import smallint_pk, str_50


class Unit(Base):
	__tablename__ = "unit"

	id: Mapped[smallint_pk]
	name: Mapped[str_50]
