from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

import os
from pathlib import Path

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
            assert "extracted_text" in response.json() 
    finally:
        if test_image_path.exists():
            test_image_path.unlink()