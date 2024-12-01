from typing_extensions import Annotated
from sqlalchemy import BigInteger, SmallInteger, String
from sqlalchemy.orm import mapped_column

bigint_pk = Annotated[int, mapped_column(BigInteger, primary_key=True)]
smallint_pk = Annotated[int, mapped_column(SmallInteger, primary_key=True)]

bigint = Annotated[int, mapped_column(BigInteger)]
smallint = Annotated[int, mapped_column(SmallInteger)]

str_100 = Annotated[str, mapped_column(String(100))]
str_50 = Annotated[str, mapped_column(String(50))]
