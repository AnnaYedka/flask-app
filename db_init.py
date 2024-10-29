from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base


# ********** sync engine ********** #
sync_engine = create_engine(
    url=f"postgresql+psycopg://postgres:postgres@localhost:5432/sa",
    echo=True,  # Показать SQL в консоли
    pool_size=5,  # Количеством соединений с базой данных, которые могут быть открыты одновременно
    max_overflow=10,  # Дополнительные соединения, которые могут быть созданы
)


# with engine.connect() as conn: -> AUTO ROLLBACK
# with engine.begin() as conn:   -> AUTO COMMIT


# ********** sync var ********** #
# with engine.connect() as conn:
#     res = conn.execute(text("SELECT 1,2,3 UNION SELECT 4, 5, 6"))
#     print(f"{res.all()=}")
#     print(f"{res.first()=}")



# Фабрика синхронных сессий
session = sessionmaker(sync_engine)

def create_tables(metadata_obj=None):
    # sync_engine.echo = False
    # metadata_obj.drop_all(sync_engine)
    # metadata_obj.create_all(sync_engine)
    # sync_engine.echo = True
    Base.metadata.create_all(sync_engine)

if __name__ == "__main__":
    create_tables()
