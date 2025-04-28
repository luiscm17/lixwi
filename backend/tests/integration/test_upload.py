from fastapi.testclient import TestClient
from app.main import app
import pytest
from pathlib import Path
import io

client = TestClient(app)

def test_upload_image():
    try:
        test_image_path = Path("tests/resources/test_image.jpg")
        test_image_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(test_image_path, "wb") as f:
            f.write(b"fake image content")
        
        with open(test_image_path, "rb") as img:
            response = client.post("/api/v1/upload/", files={"file": ("test_image.jpg", img, "image/jpeg")})
            assert response.status_code == 200
            assert "filename" in response.json()
            # Removemos la verificación de extracted_text ya que no es parte de la respuesta
            assert response.json()["filename"] == "test_image.jpg"
    finally:
        if test_image_path.exists():
            test_image_path.unlink()

def test_upload_large_file():
    # Crear un archivo que exceda el límite de 5MB
    large_file = io.BytesIO(b"0" * (6 * 1024 * 1024))
    response = client.post(
        "/api/v1/upload/",
        files={"file": ("large_file.jpg", large_file, "image/jpeg")}
    )
    assert response.status_code == 400
    assert "demasiado grande" in response.json()["detail"]

def test_upload_invalid_format():
    response = client.post(
        "/api/v1/upload/",
        files={"file": ("test.txt", b"text content", "text/plain")}
    )
    assert response.status_code == 400
    assert "Formato no soportado" in response.json()["detail"]