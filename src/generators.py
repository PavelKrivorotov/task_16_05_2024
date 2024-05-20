import random

from src.managers import UserManager


def generate_users(
    count: int = 100,
    fio_first_word: str = 'F',
    sex: str = 'Male'
) -> list[UserManager]:
    
    objs = []
    for c in range(count):    
        f = ''.join(
            [fio_first_word]
            + [chr(random.randint(97, 122)) for i in range(random.randint(3, 15))]
        )
        i = ''.join([chr(random.randint(97, 122)) for i in range(random.randint(3, 8))])
        o = ''.join([chr(random.randint(97, 122)) for i in range(random.randint(3, 10))])

        fio = '{0} {1} {2}'.format(
            f.capitalize(),
            i.capitalize(),
            o.capitalize()
        )

        month = random.randint(1, 12)
        day = random.randint(1, 15)
        dob = '{}-{}-{}'.format(
            '2000',
            str(month) if month > 9 else '0' + str(month),
            str(day) if day > 9 else '0' + str(day)
        )
        # sex = ['Male', 'Female'][random.randint(0, 1)]

        obj = UserManager(fio=fio, dob=dob, sex=sex)
        objs.append(obj)
    
    return objs

