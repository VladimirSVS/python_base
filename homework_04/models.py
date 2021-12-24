"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    relationship,
    sessionmaker,
)
from sqlalchemy.orm.decl_api import declared_attr
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.ext.declarative import declarative_base


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or \
    "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=False)

async_session_factory = sessionmaker(bind=engine, class_=AsyncSession)
Session = async_scoped_session(async_session_factory, scopefunc=current_task)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __str__(self) -> str:
        attributes = [
            f"{name}= {(getattr(self, name))!r}"
            for name, value in self.__class__.__dict__.items()
            if not name.startswith("_") and not isinstance(value, InstrumentedAttribute)
        ]
        return f"{self.__class__.__name__}({', '.join(attributes)})"
    
    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(String(40), unique=True)
    username = Column(String(50))
    email = Column(String(80),unique=True)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    title = Column(String(256), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="posts")
