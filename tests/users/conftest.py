from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient
from src.database import get_db
from src.packages.users.repository.users_repository import UsersRepository  # noqa: E501
from src.packages.users.schemas.users import User


@pytest.fixture
def fixture_user_repository_mocking_sqlalchemy():
    users_repository = UsersRepository()
    users_repository.db_session = MagicMock()
    users_repository.db_session.query.return_value.filter.return_value.first.return_value = (  # noqa: E501
        User(first_name="Gabrielzim", email="talk@gabrielaranha.com")
    )
    return users_repository


@pytest.fixture
def fixture_user_repository():
    users_repository = UsersRepository()
    users_repository.get_by_license_plate = AsyncMock(
        return_value=User(first_name="Gabrielzim", email="talk@gabrielaranha.com")  # noqa: E501
    )
    return users_repository


def override_database_session_for_http_requests():
    db_session = MagicMock()
    db_session.query.return_value.filter.return_value.first.return_value = User(  # noqa: E501
        first_name="Gabrielzim", email="talk@gabrielaranha.com"
    )
    return db_session


@pytest.fixture(scope="function")
def client():
    from src.app import create_app

    initiated_app = create_app()

    initiated_app.dependency_overrides[get_db] = override_database_session_for_http_requests  # noqa: E501

    client = TestClient(initiated_app)
    return client
