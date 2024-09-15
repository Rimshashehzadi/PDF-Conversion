from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://neondb_owner:8EG0IaWfuTJM@ep-cool-butterfly-a5jzey8j.us-east-2.aws.neon.tech/neondb?sslmode=require"  # SQLite or any other database URL

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
