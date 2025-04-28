import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.db.session import Base, get_db
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL").replace("lixwi_db", "test_lixwi")

@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        # Mantener algunas opciones útiles para pruebas
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=0
    )
    # Crear todas las tablas para las pruebas
    Base.metadata.create_all(bind=engine)
    yield engine
    # Limpiar después de las pruebas
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    SessionLocal = sessionmaker(bind=connection)
    session = SessionLocal()
    
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def test_user(client, db_session):
    user_data = {
        "username": "testuser",
        "email": "test@example.com"  # Eliminado password ya que no está en el modelo
    }
    response = client.post("/api/v1/users/", json=user_data)
    return response.json()