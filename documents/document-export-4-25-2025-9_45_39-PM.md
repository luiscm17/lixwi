# 

graph TD
A[Usuario] --> B[Frontend - Aplicación Web]
B --> B1[React o Next.js]
B --> B2[Tailwind CSS]
B --> B3[Interfaz tipo chat]
B --> B4[Subida de imágenes]
B --> B5[Visualización paso a paso]

B --> C[Backend - API Python]
C --> C1[FastAPI o Flask]
C --> C2[LangChain o Semantic Kernel]
C --> C3[Generación de gráficos e imágenes]
C --> C4[Manejo de memoria/contexto]

C --> D[Modelo LLM - OpenAI]
D --> D1[GPT vía GitHub Copilot o API]

C --> E[Memoria y Datos]
E --> E1[DB Vectorial (FAISS o ChromaDB)]
E --> E2[Base estructurada (MongoDB o PostgreSQL)]
E --> E3[Archivos / Imágenes (S3 o local)]

C --> F[Infraestructura]
F --> F1[Desarrollo local]
F --> F2[Despliegue opcional: Vercel, Railway, Render]

D1 --> C3
E1 --> C2
E2 --> C2
E3 --> C3
C3 --> B5 

