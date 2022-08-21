import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale


Base = declarative_base()

DSN = "postgresql://postgres:wsxzaq!1@localhost:5432/HomeWork6"
engine = sqlalchemy.create_engine(DSN)

Session = sqlalchemy.sessionmaker(bind=engine)
session = Session()



def searching_publisher_name():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите имя (name) издателя: ')
    query_result = query_join.filter(Publisher.name == query_publisher_name)
    for result in query_result.all():
        print(f'Издатель "{query_publisher_name}" найден в магазине "{result.name}" с идентификатором {result.id}')


def searching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите идентификатор (id) издателя: ')
    query_result = query_join.filter(Publisher.id == query_publisher_name)
    for result in query_result.all():
        print(
            f'Издатель c id: {query_publisher_name} найден в магазине "{result.name}" '
            f'с идентификатором {result.id}')


if __name__ == '__main__':
    searching_publisher_name()
    searching_publisher_id()


session.close()
