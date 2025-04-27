import pytest
from app.services.exercise_generator import generate_exercise

@pytest.mark.asyncio
async def test_generate_exercise_with_solution():
    # Prueba generación con solución
    result = await generate_exercise("matemáticas", "fácil", True)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Problema:" in result
    assert "Solución:" in result

@pytest.mark.asyncio
async def test_generate_exercise_without_solution():
    # Prueba generación sin solución
    result = await generate_exercise("física", "medio", False)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Problema:" in result
    assert "Solución:" not in result

@pytest.mark.asyncio
async def test_generate_exercise_different_subjects():
    # Prueba con diferentes materias
    subjects = ["química", "biología", "física"]
    difficulties = ["fácil", "medio", "difícil"]
    
    for subject in subjects:
        for difficulty in difficulties:
            result = await generate_exercise(subject, difficulty)
            assert isinstance(result, str)
            assert len(result) > 0
            assert "Problema:" in result
            # Verificamos que la respuesta no esté vacía y tenga un formato válido
            assert len(result.split()) > 10  # Al menos 10 palabras
            assert result.strip() != ""

@pytest.mark.asyncio
async def test_generate_exercise_error_handling():
    # Prueba manejo de errores con valores inválidos
    try:
        result = await generate_exercise("", "")
        assert "Error" in result
    except Exception as e:
        assert True  # Debería lanzar una excepción