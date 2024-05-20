import datetime
from typing import Union

from src.cruds import user_crud


class UserManager:
    def __init__(self, fio: str, dob: Union[str, datetime.date], sex: str) -> None:
        self.fio = self._validate_fio(fio)
        self.sex = self._validate_sex(sex)

        if isinstance(dob, str):
            self.dob = self._validate_dob(dob)
        else:
            self.dob = dob

    @property
    def dob_str(self) -> str:
        return self.dob.strftime('%Y-%m-%d')

    @property
    def complete_years(self) -> int:
        delta = datetime.datetime.now() \
            - datetime.datetime(
                year=self.dob.year,
                month=self.dob.month,
                day=self.dob.day
            )
        return delta.days // 365

    async def send_object_to_db(self) -> None:
        user = await user_crud.create(self.fio, self.dob, self.sex)

    @staticmethod
    async def bulk_insertion_objects(users: list['UserManager']) -> None:
        objs = []
        for user in users:
            objs.append({
                'fio': user.fio,
                'dob': user.dob,
                'sex': user.sex
            })

        await user_crud.bulk_insert(objs)
    
    def _validate_fio(self, fio: str) -> str:
        return fio
    
    def _validate_dob(self, dob: str) -> datetime.date:
        return datetime.date.fromisoformat(dob)
    
    def _validate_sex(self, sex: str) -> str:
        if sex.lower() != 'male' and sex.lower() != 'female':
            raise ValueError('A valid value for the sex parameter is `Male` or `Female`')
        
        return sex.capitalize()

