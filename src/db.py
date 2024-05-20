import time

from sqlalchemy import event
from sqlalchemy import URL
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src import settings


url = URL.create(
    drivername=settings.DATABASE['MIDDLWARE'],
    username=settings.DATABASE['USER'],
    password=settings.DATABASE['PASSWORD'],
    database=settings.DATABASE['NAME'],
    host=settings.DATABASE['HOST'],
    port=settings.DATABASE['PORT']
)

async_engine = create_async_engine(url=url)
async_session_maker = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession,
)


class Base(DeclarativeBase):
    pass




# # 
# # 

# @event.listens_for(Engine, "before_cursor_execute")
# def before_cursor_execute(
#     conn,
#     cursor,
#     statement,
#     parameters,
#     context,
#     executemany
# ):
    
#     conn.info.setdefault("query_start_time", []).append(time.time())

# @event.listens_for(Engine, "after_cursor_execute")
# def after_cursor_execute(
#     conn,
#     cursor,
#     statement,
#     parameters,
#     context,
#     executemany
# ):

#     total = time.time() - conn.info["query_start_time"].pop(-1)
#     print(total * 1000, ' ms')

