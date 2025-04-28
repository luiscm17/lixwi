# LIXWI API - Backend 🚀

## Descripción
Backend para un sistema de tutoría inteligente que utiliza modelos de lenguaje avanzados para proporcionar asistencia educativa personalizada a estudiantes de ingeniería.

## Características Principales ✨
- Chat inteligente con manejo de sesiones
- Sistema de plugins extensible
- Generación de ejercicios matemáticos
- Procesamiento y análisis de imágenes
- Visualizaciones gráficas interactivas
- Sistema de logging centralizado
- Manejo de errores unificado
- Memoria de conversación por usuario

## Tecnologías 🛠
- **FastAPI**: Framework web moderno
- **SQLAlchemy**: ORM para gestión de base de datos
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **GitHub Models**: Integración con modelos de IA
- **Pydantic**: Validación de datos y serialización
- **Matplotlib**: Generación de gráficos
- **Pillow**: Procesamiento de imágenes
- **Python-dotenv**: Gestión de variables de entorno
- **Pytest**: Framework de testing

## Estructura del Proyecto 📁
backend/
├── app/
│   ├── agents/
│   │   └── agent_manager.py
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── agent.py
│   │   │   │   ├── chat.py
│   │   │   │   ├── exercise.py
│   │   │   │   ├── upload.py
│   │   │   │   └── visualize.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging_config.py
│   ├── plugins/
│   │   ├── exercise_creator/
│   │   └── graph_generator/
│   ├── services/
│   │   ├── exercise_generator.py
│   │   └── llm_service.py
│   └── main.py
├── tests/
│   ├── integration/
│   └── unit/
└── requirements.txt

## Instalación 🔧

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/yourusername/ai-agent-python.git
    cd ai-agent-python/backend
    ```
2. Crear entorno virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Configurar variables de entorno:
    ```bash
    cp .env.example .env # Editar .env con tu GITHUB_TOKEN
    ```

# Editar .env con tu LLM_API_KEY

## Uso 🚀
1. Iniciar el servidor:
    ```bash
    uvicorn app.main:app --reload
    ```
2. Acceder a la documentación:
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- 
## Endpoints Principales 🌐

### Agentes IA
```http
POST /api/v1/agent/execute
```
### Ejercicios Matemáticos
```http
POST /api/v1/exercises/
```
### Chat
```http
POST /api/v1/chat
```

Maneja interacciones de chat con Lixwi, incluyendo manejo de sesiones y contexto.

### Subida de Archivos
```http
POST /api/v1/upload
```

Procesa imágenes y documentos.

## Desarrollo 👨‍💻
### Ejecutar Tests
```bash
pytest
```
### Iniciar Servidor de Desarrollo
```bash
uvicorn app.main:app --reload
```

### Logging
Los logs se guardan en `app.log` y también se muestran en consola. Configuración en `core/logging_config.py`.

### Manejo de Errores
Sistema centralizado de manejo de errores en `api/v1/error_handlers.py`.

## Contribución 🤝
- Fork el proyecto
- Crea tu rama de características ( `git checkout -b feature/AmazingFeature` )
- Commit tus cambios ( `git commit -m 'Add: nueva característica'` )
- Push a la rama ( `git push origin feature/AmazingFeature` )
- Abre un Pull Request
## Licencia 📄
Este proyecto está bajo la Licencia MIT.

## Contacto 📧
- Proyecto: GitHub Issues
Nota : Este proyecto está en desarrollo activo. Las características y la documentación se actualizan regularmente.