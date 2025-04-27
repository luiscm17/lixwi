# 🧠 Lixwi AI - Tutor Inteligente para Matemáticas 🚀

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green.svg)](https://fastapi.tiangolo.com/)

Plataforma de tutoría inteligente que combina modelos de lenguaje avanzados con herramientas especializadas para el aprendizaje interactivo de matemáticas.

## 🌟 Características Principales
- 🗣️ Chat interactivo con seguimiento de contexto
- 📈 Generación de ejercicios personalizados
- 🖼️ Procesamiento de imágenes matemáticas
- 📊 Visualizaciones gráficas interactivas
- 🔌 Sistema de plugins extensible
- 📚 Memoria de aprendizaje por usuario

## 🛠️ Stack Tecnológico
| **Categoría**       | **Tecnologías**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| Framework Web        | FastAPI, Uvicorn, Pydantic                                                     |
| Base de Datos        | SQLAlchemy, PostgreSQL                                                         |
| Inteligencia Artificial | OpenAI API, Transformers                                                    |
| Procesamiento        | Pillow (imágenes), Matplotlib (gráficos), NumPy (cálculos)                     |
| Desarrollo           | Pytest, MyPy, Black, Flake8                                                     |
| DevOps               | Docker, GitHub Actions                                                          |

## 🚀 Primeros Pasos

### Requisitos
- Python 3.10+
- PostgreSQL 14+
- OpenAI API Key

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/tuusuario/lixwi.git
cd lixwi/backend
```

# Configurar entorno virtual
```python -m venv env
env\Scripts\activate
```
# Instalar dependencias
```python
pip install -r requirements.txt
```

# Configurar variables de entorno
```python 
cp .env.example .env
```

### Variables de Entorno (.env)
```python
OPENAI_API_KEY=tu_clave_apiDATABASE_URL=postgresql://user:password@localhost:5432/lixwiAPI_VERSION=1.0.0DEBUG=true
```

## 🏗️ Estructura del Proyecto
```
lixwi/
├── backend/
│   ├── app/
│   │   ├── agents/          # Gestión de agentes IA
│   │   ├── api/             # Endpoints de la API
│   │   ├── core/            # Configuración central
│   │   ├── plugins/         # Plugins especializados
│   │   ├── services/        # Lógica de negocio
│   │   └── main.py          # Punto de entrada
├── tests/                   # Pruebas automatizadas
└── docs/                    # Documentación técnica
```
## 📡 Endpoints Clave
### Generar Ejercicio
```http
POST /api/v1/exercises/generate
```

```json
{  "tema": "álgebra",  "dificultad": "intermedia",  "tipo":   "ecuaciones_lineales"}
```

### Procesar Imagen Matemática
```http
POST /api/v1/upload
```

```python

files = {'file': ('ecuacion.jpg', open('ecuacion.jpg', 'rb'), 'image/jpeg')}
```

### Chat Interactivo
```http
POST /api/v1/chat
```

```json
{  "mensaje": "¿Cómo resuelvo   ecuaciones cuadráticas?",  "historial": []}
```

### 🛠️ Desarrollo
```bash
# Ejecutar tests
pytest -v
# Iniciar servidor local
uvicorn app.main:app --reload
# Verificar tipos
mypy app/
```

## 🤝 Contribución
* Haz fork del repositorio
* Crea una rama: git checkout -b feature/nueva-funcionalidad
* Realiza commits descriptivos
* Abre un Pull Request detallando los cambios


## 📧 Contacto
¿Preguntas o sugerencias? Abre un issue

¡Descubre el futuro de la educación matemática! 🚀🧮