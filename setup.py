from setuptools import find_packages, setup

setup(
    name="api",
    version="0.1.0",
    license="MIT",
    url="https://github.com/edcilo/fastapi_2023",
    description="FastAPI boilerplate",
    author="edcilo",
    author_email="me@edcilo.com",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    python_requires=">=3.11",
    install_requires=[
        "asyncpg==0.28.0",
        "loguru==0.7.2",
        "SQLAlchemy==2.0.22",
    ],
    extras_require={
        "dev": [
            "pytest==7.4.2",
            "pytest-asyncio==0.21.1",
            "pytest-cov==4.1.0",
        ],
    },
)
