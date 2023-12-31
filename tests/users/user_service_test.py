from src.packages.users.services.users_service import UsersService


async def test_get_user_mocking_sql_alchemy(
    fixture_users_repository_mocking_sqlalchemy,
):
    service = UsersService(repository=fixture_users_repository_mocking_sqlalchemy)  # noqa: E501

    user = await service.get_user(name="Gabrielzim")
    assert user.email == "talk@gabrielaranha.com"


async def test_get_user_mocking_users_repository(fixture_users_repository):
    service = UsersService(repository=fixture_users_repository)

    user = await service.get_user(name="Gabrielzim")
    assert user.email == "talk@gabrielaranha.com"
