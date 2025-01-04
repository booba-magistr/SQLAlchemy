from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, String, ForeignKey
from typing import Annotated
from sqlalchemy import DateTime, text
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


PKint = Annotated[int, mapped_column(primary_key=True)]

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f'{cls.__name__.lower()}'
    
    created: Mapped[DateTime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"))
    updated: Mapped[DateTime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"), 
                                              onupdate=text("TIMEZONE('utc', now())"))

class Worker(Base):
    id: Mapped[PKint]
    username: Mapped[str]
    first_name: Mapped[str] = mapped_column(String(64))


class CVModel(Base):
    id: Mapped[PKint]
    worker_id: Mapped[int] = mapped_column(ForeignKey('worker.id', ondelete='CASCADE'))
    title: Mapped[str]
    salary: Mapped[float] = mapped_column(Numeric(6, 2), nullable=True)