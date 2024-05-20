import asyncio
import sys
from pathlib import Path

from alembic.config import Config
from alembic import command

from src import settings
from src.db import url
from src.managers import UserManager
from src.cruds import user_crud
from src.generators import generate_users


def _get_alembic_config() -> Config:
    path = Path(settings.Base_Dir, 'alembic.ini')

    config = Config(path)
    config.set_main_option(
        name='sqlalchemy.url',
        value=url.render_as_string(hide_password=False)
    )

    return config


def init_db():
    config = _get_alembic_config()
    command.upgrade(config, 'afbfe2268939')


async def create_user() -> None:
    async def _create_user(fio: str, dob: str, sex: str) -> None:
        user = UserManager(
            fio=fio,
            dob=dob,
            sex=sex
        )
        await user.send_object_to_db()

    fio, dob, sex = sys.argv[2:5]
    return await _create_user(fio, dob, sex)


async def list_unique_users() -> None:
    users = await user_crud.list_unique()
    for user in users:
        manager = UserManager(user.fio, user.dob, user.sex)
        represent = '{0}, {1}, {2}, {3}, {4}'.format(
            user.id,
            manager.fio,
            manager.dob_str,
            manager.sex,
            manager.complete_years
        )
        print(represent)


def bulk_insert() -> None:
    try:
        if sys.argv[2] == '--only-100-males-with-fio-startswith-f':
            users = generate_users()
            asyncio.run(UserManager.bulk_insertion_objects(users))
        
        else:
            print(
                'Invalid argument `{0}`. Allowded only `--only-100-males-with-fio-startswith-f` argument or WITHOUT'.format(
                    sys.argv[2]
                )
            )
            
    except IndexError:
        config = _get_alembic_config()
        command.upgrade(config, '4b352e695ac5')


async def list_users_with_filters() -> None:
    t, users  = await user_crud.list_with_filters()
    print('Time query: ', t*1000, ' ms')


def list_users_with_filters_upgrade() -> None:
    config = _get_alembic_config()
    command.upgrade(config, '60ab68b4cc2f')

    t, users  = asyncio.run(user_crud.list_users_with_filters_upgrade())
    print('Time query: ', t*1000, ' ms')


def clear_db() -> None:
    config = _get_alembic_config()
    command.downgrade(config, 'base')


def main():
    match sys.argv[1]:
        case '1':
            # print('First command: ', '1')
            init_db()
        
        case '2':
            # print('Second command: ', '2')
            asyncio.run(create_user())

        case '3':
            # print('Thrid command: ', '3')
            asyncio.run(list_unique_users())

        case '4':
            # print('Four command: ', '4')
            bulk_insert()
        
        case '5':
            # print('Five command: ', '5')
            asyncio.run(list_users_with_filters())

        case '6':
            # print('Six command: ', '6', ' (Upgrade table and query)')
            list_users_with_filters_upgrade()

        case '7':
            # print('Seven commang: ', '7', ' (Downgrade to init_db())')
            clear_db()


if __name__ == '__main__':
    main()

