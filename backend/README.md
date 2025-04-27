# LIXWI API - Backend 🚀

## Descripción
Backend para un sistema de tutoría inteligente que utiliza modelos de lenguaje avanzados para proporcionar asistencia educativa personalizada a estudiantes de ingeniería.

## Características Principales ✨
- Chat inteligente con manejo de sesiones
- Procesamiento y análisis de imágenes
- Generación de visualizaciones y gráficos
- Sistema de logging robusto
- Manejo centralizado de errores
- Memoria de conversación por usuario

## Tecnologías 🛠
- **FastAPI**: Framework web rápido y moderno
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **GitHub Models**: Integración con modelos de IA
- **Pydantic**: Validación de datos y serialización
- **Matplotlib**: Generación de gráficos
- **Python-dotenv**: Gestión de variables de entorno
- **Pytest**: Framework de testing

## Estructura del Proyecto 📁
backend/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/       # Rutas de la API
│   │   │   ├── error_handlers.py
│   │   │   └── schemas.py
│   ├── core/                    # Configuración central
│   ├── services/                # Lógica de negocio
│   ├── models/                  # Modelos de datos
│   ├── utils/                   # Utilidades
│   └── main.py                  # Punto de entrada
├── tests/                       # Pruebas unitarias
└── requirements.txt             # Dependencias

## Instalación 🔧

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/yourusername/ai-agent-python.git
    cd ai-agent-python/backend
    ```
2. Crear entorno virtual:
    ```bash
    git clone https://github.com/yourusername/ai-agent-python.git
    cd ai-agent-python/backend
    ```
3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Configurar variables de entorno:
    ```bash
    cp .env.example .env # Editar .env con tu GITHUB_TOKEN
    ```

# Editar .env con tu GITHUB_TOKEN

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
### Chat
```http
POST /api/v1/chat
```

Maneja interacciones de chat con el tutor IA, incluyendo manejo de sesiones y contexto.

### Visualizaciones
```http
GET /api/v1/visualize
```

Genera visualizaciones y gráficos explicativos.

### Subida de Archivos
```http
POST /api/v1/upload
```

Procesa imágenes y documentos.

## Desarrollo 👨‍💻
### Pruebas
```bash
pytest
```

### Logging
Los logs se guardan en `app.log` y también se muestran en consola. Configuración en `core/logging_config.py`.

### Manejo de Errores
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