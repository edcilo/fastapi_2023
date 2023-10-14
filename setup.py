from setuptools import setup

setup(
    name='fastapi',
    version='0.1.0',
    description='FastAPI boilerplate',
    author='edcilo',
    author_email='me@edcilo.com',
    packages=['app'],
    python_requires='>=3.11',
    install_requires=[
        "SQLAlchemy==2.0.22",
        "asyncpg==0.28.0",
    ],
    extras_require={
        'dev': [],
    },
)
