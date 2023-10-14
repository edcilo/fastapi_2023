from sqlalchemy import Column, Integer, String
from app.models.model import Model


class Foo(Model):
    __tablename__ = "foo"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
