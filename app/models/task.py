from sqlalchemy import Column, Integer, String
from .model import Model


class Task(Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    description = Column(String(120), nullable=False)
