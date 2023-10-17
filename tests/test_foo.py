import pytest

from sqlalchemy.future import select

from .fixtures import api
from app.core.db import get_db
from app.models import Task


@pytest.mark.asyncio
async def test_new_foo_model(api):
    async for db in get_db():
        task = Task(description="write tests")
        db.add(task)

        await db.commit()

        assert task.description == "write tests"
        assert task.id is not None


@pytest.mark.asyncio
async def test_list_foo_model(api):
    async for db in get_db():
        task1 = Task(description="task-1")
        task2 = Task(description="task-2")
        db.add_all([task1, task2])
        await db.commit()

        result = await db.execute(select(Task))
        tasks = result.scalars().all()

        assert len(tasks) == 2


@pytest.mark.asyncio
async def test_find_foo_model(api):
    async for db in get_db():
        task = Task(description="task")
        db.add(task)
        await db.commit()

        result = await db.execute(
            select(Task).where(Task.id == task.id)
        )
        _task = result.scalars().first()

        assert _task.description == "task"


@pytest.mark.asyncio
async def test_update_foo_model(api):
    async for db in get_db():
        task = Task(description="task")
        db.add(task)
        await db.commit()

        result = await db.execute(
            select(Task).where(Task.id == task.id)
        )
        _task = result.scalars().first()

        assert _task.description == "task"

        _task.description = "task-1"
        db.add(_task)
        await db.commit()

        result = await db.execute(
            select(Task).where(Task.id == task.id)
        )
        _task = result.scalars().first()

        assert _task.description == "task-1"


@pytest.mark.asyncio
async def test_delete_foo_model(api):
    async for db in get_db():
        task = Task(description="task")
        db.add(task)
        await db.commit()

        result = await db.execute(
            select(Task).where(Task.id == task.id)
        )
        _task = result.scalars().first()

        assert _task.description == "task"

        await db.delete(_task)
        await db.commit()

        result = await db.execute(
            select(Task).where(Task.id == task.id)
        )
        _task = result.scalars().first()

        assert _task is None
