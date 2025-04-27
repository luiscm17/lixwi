# Memoria de Conversación en el Backend

## 🧠 Memoria Básica de Conversación

### Situación Actual
Actualmente, cuando envías un mensaje al `/chat`, el bot solo responde a ese mensaje sin recordar el contexto previo. Vamos a implementar un sistema para que el bot mantenga un historial durante una "sesión" de conversación.

### Ejemplo de Funcionamiento
- Usuario: "¿Qué es la energía cinética?" → Bot responde
- Usuario: "¿Y cómo se calcula?" → Bot entiende que se refiere a energía cinética

### 🛠️ Implementación
**Versión inicial simple:**
- Cada sesión de usuario tendrá un historial guardado en memoria RAM (diccionario en Python)
- No persistirá en base de datos (implementación posterior)

### ✏️ Plan de Acción Técnico
1. Crear `/core/memory.py`
   - Implementar diccionario global para historiales
2. Actualizar `llm_service.py`
   - Añadir soporte para envío de historial a OpenAI
3. Modificar endpoint `/chat`
   - Implementar manejo de `session_id`

## 📚 Memoria Avanzada

### Niveles de Implementación

| Nivel | Funcionalidad | Base de Datos |
|-------|---------------|---------------|
| 1 | Conversación actual | No |
| 2 | Persistencia entre sesiones | Sí |
| 3 | Conocimiento personalizado | Sí + Embeddings |

### Estructura de Base de Datos
Entidades a considerar:
- Usuarios
- Conversaciones
- Mensajes
- Temas/Materias
- Recursos multimedia

> 💡 Recomendación: Comenzar con SQLite o PostgreSQL para simplicidad inicial

### 📦 Estado Actual
- ✅ Memoria actual: Solo sesión
- 🔄 Memoria avanzada: Pendiente implementación con BD
- 📋 Próximo paso: Diseño de modelo entidad-relación

## 🔧 Mejoras en Desarrollo

### 1. Optimización de upload.py
- Validación de tipos de imagen
- Almacenamiento en `/tmp_uploads/`
- Sistema de confirmación

#### Componentes Principales
| Componente | Función |
|------------|---------|
| UploadFile | Manejo eficiente de archivos grandes |
| content_type.startswith("image/") | Validación de tipo |
| shutil.copyfileobj | Gestión de archivos |
| ./tmp_uploads/ | Almacenamiento temporal |

### 2. Mejoras en visualize.py
- Generación de gráficos simples
- Conversión de JSON a visualizaciones

## 🎯 Nuevo Sistema de Generación de Ejercicios

### Objetivo
Implementar un sistema para generar ejercicios originales adaptados a diferentes materias y niveles.

### 🏗️ Arquitectura

#### 1. Servicio de Generación
**Archivo:** `app/services/exercise_generator.py`

```python
def generate_exercise(subject: str, difficulty: str) -> str
```
- Parámetros:
  - subject: materia académica
  - difficulty: nivel de dificultad
 
#### 2. API Endpoint
Configuración:

- Ruta: /generate-exercise
- Método: POST
- Formato de entrada:
    ```json
    {
      "subject": "física",
      "difficulty": "medio"
    }
    ```
#### 3. Sistema de Prompts
Plantilla base:

"Crea un ejercicio original de nivel {dificultad} en {materia}, adecuado para un estudiante universitario."
    
### 📚 Conceptos relacionados para investigar (opcional):

Concepto | Qué es
--- | ---
Prompt Engineering | Diseño de instrucciones para LLMs
Multimodal prompting | Usar imagen+texto para entrada al LLM
Few-shot prompting | Dar ejemplos para mejorar calidad de generación
Control de temperatura/top_p | Controlar creatividad del modelo


