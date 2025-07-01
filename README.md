# API Library

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy (with Alembic for migrations)
- **Authentication**: JWT (JSON Web Tokens) with OAuth2
- **Data Validation**: Pydantic
- **ASGI Server**: Uvicorn
- **Containers**: Docker
- **Version Control**: Git
- **Deployment**: Google Cloud Run

## Commands

### Create virtual env
```bash
python -m venv venv
```

### Activate virtual env for Win
```bash
.\venv\Scripts\activate
```

### Activate virtual env for Mac / Linux
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install "fastapi[all]" sqlalchemy psycopg2-binary alembic pydantic-settings
```
### or
```bash
pip3 install "fastapi[all]" sqlalchemy psycopg2-binary alembic pydantic-settings
```

### Execute server
```bash
uvicorn main:app --reload
```

### Execute docker
```bash
docker-compose up -d
```

### Configure alembic
```bash
alembic init alembic
```

### Create migration
```bash
alembic revision --autogenerate -m "Create authors and books tables"
alembic upgrade head
```
