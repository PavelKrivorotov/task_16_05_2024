import datetime

from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] =  mapped_column(
        Integer,
        primary_key=True
    )
    fio: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )
    dob: Mapped[datetime.date] = mapped_column(
        Date,
        nullable=False
    )
    sex: Mapped[str] = mapped_column(
        String(6),
        nullable=False   
    )

