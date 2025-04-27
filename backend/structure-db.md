# 📚 Guía Completa de la Base de Datos - Lixwi

## 🌟 Introducción

/backend/
├── app/
│   ├── db/                # <-- Aquí ponemos todo de base de datos
│   │   ├── base.py         # Configuración inicial del ORM
│   │   ├── models/         # Modelos de tablas
│   │   │   ├── user.py
│   │   │   ├── chat_history.py
│   │   │   └── exercise.py
│   │   ├── crud/           # Operaciones CRUD
│   │   │   ├── user.py
│   │   │   ├── chat_history.py
│   │   │   └── exercise.py
│   │   └── session.py      # Manejo de la conexión DB (engine, session local)

## 📋 Modelos de Datos
### 1. Usuario (User)
```python
class User:
    id          → Identificador único
    username    → Nombre de usuario
    email       → Correo (opcional)
    created_at  → Fecha de creación
```
**¿Para qué sirve?**

- Identifica usuarios únicos en el sistema
- Permite seguimiento de actividades por usuario
- Facilita la personalización de la experiencia

### 2. Historial de Chat (ChatHistory)
```python
class ChatHistory:
    id          → Identificador único
    user_id     → Referencia al usuario
    question    → Pregunta del usuario
    answer      → Respuesta del sistema
    created_at  → Fecha y hora
```
**¿Para qué sirve?**

- Guarda el historial de conversaciones
- Permite análisis de interacciones
- Mejora la personalización de respuestas

### 3. Ejercicios (Exercise)
```python
class Exercise:
    id          → Identificador único
    user_id     → Referencia al usuario
    subject     → Materia académica
    problem     → Enunciado del ejercicio
    solution    → Solución detallada
    difficulty  → Nivel de dificultad
    created_at  → Fecha de creación
```

**¿Para qué sirve?**

- Almacena ejercicios generados
- Facilita el seguimiento del progreso
- Permite personalizar la dificultad

## 🔧 Tecnologías Utilizadas
### SQLAlchemy (ORM)
- ¿Qué es? Un traductor entre Python y SQL
- ¿Por qué? Permite escribir código Python en lugar de SQL
- Ventaja: Más intuitivo y menos propenso a errores
### PostgreSQL
- ¿Qué es? Motor de base de datos robusto
- ¿Por qué? Excelente para datos relacionales
- Ventaja: Confiable y con buen rendimiento
## 🎯 Conceptos Clave
### 1. ORM (Object-Relational Mapping)
- Convierte clases Python en tablas
- Traduce métodos Python a consultas SQL
- Ejemplo: User.query.filter_by(username="ana") → SELECT * FROM users WHERE username = 'ana'
### 2. Sesiones
- Conexiones temporales a la base de datos
- Gestionan transacciones
- Aseguran la consistencia de datos
### 3. Relaciones
- One-to-Many: Un usuario tiene muchos ejercicios
- Foreign Keys: Conectan tablas relacionadas
- Cascade: Acciones automáticas en datos relacionados

## 💡 Mejores Prácticas
1. Siempre usar el ORM
   
   - No escribir SQL directo
   - Mantener el código consistente
2. Gestión de Sesiones
   
   - Usar with o contextos seguros
   - Cerrar sesiones después de usarlas
3. Variables de Entorno
   
   - Nunca hardcodear credenciales
   - Usar .env para configuración
## 🚀 Ejemplo de Uso
```python
# Crear un nuevo usuario
user = User(username="ana", email="ana@example.com")
db.add(user)
db.commit()

# Guardar un ejercicio
exercise = Exercise(
    user_id=user.id,
    subject="Matemáticas",
    problem="Resolver 2x + 5 = 13",
    solution="x = 4",
    difficulty="medium"
)
db.add(exercise)
db.commit()
```

## 📋 Mini Plan (pasos):

Instalar dependencias necesarias.

Configurar conexión a Postgres.

Definir modelos de tablas (User, ChatHistory, Exercise).

Crear operaciones CRUD.

Hacer una primera migración.

Probar guardar un dato real desde el backend.

## ✨ Primera definición: Estructura básica de tablas

Tabla | Campos principales | ¿Para qué sirve?
--- | --- | ---
User | id, nombre, email (opcional) | Identificar al usuario (puede ser anónimo al inicio).
ChatHistory | id, user_id, pregunta, respuesta, timestamp | Guardar conversaciones.
Exercise | id, user_id, enunciado, solucion, dificultad, materia, timestamp | Guardar ejercicios generados y resueltos.

Así tendríamos un backend capaz de memorizar interacciones, lo cual sube MUCHO la calidad de tu agente.

## 📚 Conceptos que debes conocer

Concepto | Explicación Rápida
--- | ---
ORM (Object Relational Mapping) | Permite interactuar con bases de datos usando clases en Python.
SQLAlchemy | Biblioteca en Python para ORM.
Session | Una conexión temporal a la base de datos para hacer consultas o insertar datos.
Engine | Manejador de conexión a la base de datos.
Base.metadata.create_all | Crea automáticamente todas las tablas de los modelos definidos.

### ❗Nota
* Los modelos (tablas) deben heredar de Base.

* El engine se conecta usando el DATABASE_URL de .env.

* Nunca pongas tus claves o URLs directo en el código.

## 📌 Recordatorios Importantes
1. Siempre activar el entorno virtual
2. Mantener actualizado el archivo .env
3. Hacer respaldos regulares
4. Usar migraciones para cambios en la estructura
## 🔍 Recursos Adicionales
- Documentación SQLAlchemy
- Tutorial PostgreSQL
- Guías de migración con Alembic