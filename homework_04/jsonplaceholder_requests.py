import logger
from dataclasses import dataclass
from typing import Optional
from aiohttp import ClientSession

log = logger.get_logger(__name__)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class Users:
    id: int
    name: str
    username: str
    email: str


@dataclass
class Posts:
    user_id: int
    id: int
    title: str
    body: str


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_users(url = USERS_DATA_URL) -> Optional[list]:
    async with ClientSession() as session:
        data = await fetch_json(session, url)
    
    users = [Users(df['id'],
                   df['name'],
                   df['username'],
                   df['email']) for df in data]
    
    log.info("Fetched %s users", len(users))
    
    return users


async def fetch_posts(url = POSTS_DATA_URL) -> Optional[list]:
    async with ClientSession() as session:
        data = await fetch_json(session, url)

    posts = [Posts(post['userId'],
                   post['id'],
                   post['title'],
                   post['body']) for post in data]    
    log.info("Fetched %s posts", len(posts))
    
    return posts
