from fastapi import APIRouter, HTTPException
import numpy as np
import matplotlib.pyplot as plt
import ast
import re

router = APIRouter()

@router.get("/")
async def visualize_expression(expression: str, x_range: str, variable: str = "x"):
    try:
        # Validar variable
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable):
            raise ValueError("El nombre de la variable debe ser un identificador válido")

        # Validar que x_range tenga exactamente dos valores
        parts = x_range.split(",")
        if len(parts) != 2:
            raise ValueError("x_range debe tener exactamente dos números separados por coma. Ejemplo: '0,10'.")

        try:
            start, end = map(float, parts)
        except ValueError:
            raise ValueError("Los valores del rango deben ser números válidos.")
        
        if start >= end:
            raise ValueError("El valor inicial del rango debe ser menor que el final.")
        
        # Generar puntos para la variable
        points = np.linspace(start, end, 100)
        
        # Definir funciones permitidas
        allowed_names = {
            variable: points,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'sqrt': np.sqrt,
            'abs': abs,
            'pi': np.pi,
            'e': np.e,
            'log': np.log,
            'ln': np.log,
            'log10': np.log10,
            'x': points
        }
        
        # Diccionario de traducciones español-inglés
        translations = {
            'sen': 'sin',  # Mover 'sen' aquí
            'seno': 'sin',
            'coseno': 'cos',
            'tangente': 'tan',
            'tg': 'tan',
            'raiz': 'sqrt',
            'exponencial': 'exp',
            'logaritmo': 'log',
            'absoluto': 'abs'
        }
        
        try:
            # Preprocesar la expresión
            expression = expression.lower().strip()
            
            # Reemplazar funciones en español
            for esp, eng in translations.items():
                expression = re.sub(r'\b' + esp + r'\b', eng, expression)
            
            # Manejar multiplicación implícita
            # Reemplazar casos como "2x" por "2*x"
            expression = re.sub(r'(\d+)([a-zA-Z])', r'\1*\2', expression)
            # Reemplazar casos como "2(..." por "2*(..."
            expression = re.sub(r'(\d+)\(', r'\1*(', expression)
            # Reemplazar casos como ")2" por ")*2"
            expression = re.sub(r'\)(\d+)', r')*\1', expression)
            # Reemplazar casos como "x(" por "x*("
            expression = re.sub(r'([a-zA-Z])\(', r'\1*(', expression)
            # Reemplazar casos como ")x" por ")*x"
            expression = re.sub(r'\)([a-zA-Z])', r')*\1', expression)
            
            # Reemplazar potencias
            expression = expression.replace('^', '**')
            
            # Validar la expresión
            tree = ast.parse(expression, mode='eval')
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and node.id not in allowed_names:
                    raise ValueError(f"Función o variable no permitida: {node.id}")
            
            # Compilar y evaluar
            code = compile(expression, "<string>", "eval")
            y = eval(code, {"__builtins__": {}}, allowed_names)
            
            if not isinstance(y, np.ndarray):
                raise ValueError("La expresión no generó resultados válidos")
                
            if np.any(np.isinf(y)) or np.any(np.isnan(y)):
                raise ValueError("La expresión genera valores infinitos o indefinidos")
                
            return {
                "title": f"Gráfica de {expression}",
                "x": points.tolist(),
                "y": y.tolist(),
                "variable": variable
            }
        except Exception as e:
            raise ValueError(f"Error al evaluar la expresión: {str(e)}")
            
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
