from sqlalchemy.orm import Mapped, mapped_column
from .model import Model


class Task(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(nullable=False)
