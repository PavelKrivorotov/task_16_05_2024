import time
import datetime

from sqlalchemy import select, insert
from sqlalchemy import  text, tuple_
from sqlalchemy import func

from src.db import async_session_maker
from src.models import User


class UserCRUD:
    async def create(self, fio: str, dob: datetime.date, sex: str) -> User:
        user = User(
            fio=fio,
            dob=dob,
            sex=sex
        )

        async with async_session_maker() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
        
    async def bulk_insert(self, raw_users: list[dict]) -> None:
        query = insert(User).values(raw_users)

        async with async_session_maker() as session:
            await session.execute(query)
            await session.commit()

    async def list_unique(self) -> list[User]:
        query = (
            select(User)
            .where(
                tuple_(
                    User.fio,
                    User.dob
                )
                .in_(
                    select(
                        User.fio,
                        User.dob
                    )
                    .group_by(
                        User.fio,
                        User.dob
                    )
                    .having(func.count() == 1)
                )
            )
            .order_by(User.fio)
        )
        
        async with async_session_maker() as session:
            users = await session.scalars(query)
            return users.all()
        
    async def list_with_filters(self) -> tuple[int, list[User]]:
        query = (
            select(User).where(
                User.fio.like('F%'),
                User.sex == 'Male'
            )
        )

        async with async_session_maker() as session:
            start = time.time()
            users = await session.scalars(query)
            stop = time.time()

            return (stop - start, users.all())
        
    async def list_users_with_filters_upgrade(self) -> tuple[int, list[User]]:
        query = (
            select(User).where(
                text('users.fio_first_word = :fio_first_word'),
                User.sex == 'Male'
            )
        )

        async with async_session_maker() as session:
            start = time.time()
            users = await session.execute(query, {'fio_first_word': 'F'})
            stop = time.time()

            return (stop - start, users.all())

user_crud = UserCRUD()

