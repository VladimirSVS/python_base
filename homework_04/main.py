"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import logger
import asyncio
from jsonplaceholder_requests import fetch_users, fetch_posts
from models import Session, engine, Base, User, Post
from sqlalchemy.exc import SQLAlchemyError


log = logger.get_logger(__name__)


async def loads_users(users, session):
    for user in users:
        user_d = User(id = user.id,
                      name = user.name,
                      username = user.username,
                      email = user.email)
        session.add(user_d)


async def load_posts(posts, session):
    for post in posts:
        post_d = Post(id = post.id,
                      title = post.title,
                      body = post.body,
                      user_id = post.user_id)
        session.add(post_d)


async def async_main():
    users_data, posts_data = await asyncio.gather(
        fetch_users(),
        fetch_posts(),
    )
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        log.info(f"database has been successfully rebuilt")
    
    session = Session()
    try:
        await loads_users(users_data, session)
        await load_posts(posts_data, session)
        await session.commit()
        log.info(f"data has been successfully loaded into the database")
    except SQLAlchemyError as e:
        log.error(e)
        await session.rollback()
    finally:
        await session.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
