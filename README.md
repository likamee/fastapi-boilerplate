# fastapi-boilerplate

## Summary

- [Summary](#-summary)
- [Technologies used](#-technologies-used)
- [Folder structure](#-folder-structure)
- [Running the project](#-running-the-project)
- [Extra commands](#-extra-commands)
- [How to use this project](#-how-to-use-this-project)


## Technologies and Patterns used

For the development of this project, the following technologies were used:

- **Python 3.9**
- **FastAPI (Rest API)**
- **Poetry** (Python package manager)
- **SQLAlchemy** (ORM)
- **Alembic** (Migrations)
- **AioRedis** (Async Cache)

This project has a structure that aims for maximum decoupling between layers in order to support the creation of components that are reusable throughout the business domain. It includes a simple User CRUD with examples of package organization and tests.

Among others, the main pattern that guides this project is the Hexagonal (+ Clean Architecture) pattern, which provides a way to organize code so that business logic is encapsulated but separated from the delivery mechanism. This allows for better maintenance and fewer dependencies.

The code structure follows a domain-driven package organization, meaning that if User is a domain mapped in our domain structure, we will have the `src.packages.users` folder that contains all the necessary code for handling users with low coupling and well-defined context.

## Folder Structure

```bash
/src
  /adapters # Global adapters (inbound or outbound adapters)
  /database # If you choose to use a database, here are stored the migrations, connection rule and also the ORM models
  /exceptions # Global exception classes
  /packages # Each folder within packages refers to a domain
    /users
      /controllers # Or inbound adapters
      /exceptions # Domain-specific exception classes
      /ports # Interfaces which our adapters and services should implement
      /repository # Or outbound adapters
      /schemas # Domain entities, which may or may not contain business rules (At discretion)
      /services # Use case layer that can implement business rules, or application rules
  /ports # Global interfaces
  /utils # Secondary functions, which are out of the domain context
  /tests
    /users # As a suggestion, we should isolate our test suites by domain
```

## Running the Project

### Option 1 - Via Docker Compose

#### Run docker-compose

Finally, run the project and its dependencies in the background using the command
```bash
docker-compose up -d
```

### Option 2 - Via IDE (Pycharm)

When importing the project, the tool will identify two standard configurations versioned in the `.idea/runConfigurations` folder:
- Run App

#### Run App Config

To use the `Run App` config, you must have installed the `EnvFile` plugin, then just add a `.env` file at the root of your project and add the environment variables manually.

### Preparing the Dependencies

For this project, we use **Poetry** as the package manager. Its choice was due to the simplicity in handling packages and its impressive ability to solve dependency problems.

After importing the project, install poetry according to the documentation https://python-poetry.org/docs/

After installing and configuring poetry, install the project dependencies:
```bash
poetry install
```

You can find more instructions about poetry in its [official documentation](https://python-poetry.org/docs/)

## Extra Commands

The project has a `Makefile` file with some make commands that facilitate the preparation of dependencies.

Create a new migration:
```bash
make migrate-revision
```

Run the migrations:
```bash
make migrate-upgrade
```

Run revision and update in the container
```bash
docker-compose run web {make COMMAND}
```

Raise all dependencies:
```bash
make up
```

Run all tests:
```bash
make tests
```

## How to Use This Project

Create a new user:
```bash
$ --request POST 'http://{ENDPOINT}/api/users/' \
   --header 'Content-Type: application/json' \
   --data-raw '{
                 "email": "talk@gabrielaranha.com",
                 "first_name": "Gabriel",
                 "last_name": "Aranha",
                 "age": 30
               }'
```
Response: 
```json
{
    "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
    "email": "talk@gabrielaranha.com",
    "first_name": "Gabriel",
    "last_name": "Aranha",
    "age": 30
}
```

Get a user:
```bash
$ curl --request GET 'http://{ENDPOINT}/api/users/acba5cb6-c4ef-40ae-b6ca-4a34e138f9de'
```
Response:
```json
{
    "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
    "email": "talk@gabrielaranha.com",
    "first_name": "Gabriel",
    "last_name": "Aranha",
    "age": 30
}
```

List all users:
```bash
$ curl --request GET 'http://{ENDPOINT}/api/users/' 
```
Response:
```json
[
    {
        "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
        "email": "talk@gabrielaranha.com",
        "first_name": "Gabriel",
        "last_name": "Aranha",
        "age": 30
    }
]
```

Update a user:
```bash
$ curl --request PUT 'http://{ENDPOINT}/api/users/032f682b-5dec-4819-9fef-c57c761a8e3e' \
       --header 'Content-Type: application/json' \
       --data-raw '{
            "email": "gabriel.aranha@makes.ai",
            "first_name": "Gabrielzim",
            "last_name": "Dieguim",
            "age": 30
       }'
```
Response:
```json
{
    "id": "b49dc1ff-0897-4b73-bdc0-811533586b9a",
    "email": "gabriel.aranha@makes.ai",
    "first_name": "Gabrielzim",
    "last_name": "Dieguim",
    "age": 30
}
```

Remove a user:
```bash
$ curl --request DELETE 'http://{ENDPOINT}/api/users/b49dc1ff-0897-4b73-bdc0-811533586b9a'
```


## References

- [Hexagonal Architecture](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/)
- [Domain Driven Design - DDD](https://lyz-code.github.io/blue-book/architecture/domain_driven_design/)
- [Repository Pattern](https://lyz-code.github.io/blue-book/architecture/repository_pattern/)
- [Service Layer Pattern](https://www.cosmicpython.com/book/chapter_04_service_layer.html)
- [SQL Alchemy](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)