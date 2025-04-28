/frontend
├── public/
│   └── index.html
├── src/
│   ├── assets/              
│   │   └── (imágenes, logos, iconos)
│   ├── components/          
│   │   ├── Navbar.jsx
│   │   ├── Footer.jsx
│   │   └── LoadingSpinner.jsx
│   ├── features/             
│   │   ├── agents/           # Funciones relacionadas con AGENTES
│   │   │   ├── AgentsPage.jsx
│   │   │   ├── AgentRunner.jsx
│   │   │   └── agentStore.js (Zustand para manejar estado de agentes)
│   │   ├── plugins/          # Funciones relacionadas con PLUGINS
│   │   │   ├── PluginsPage.jsx
│   │   │   ├── PluginRunner.jsx
│   │   │   └── pluginStore.js
│   │   ├── exercise/         # Funciones específicas para CREAR EJERCICIOS
│   │   │   ├── ExerciseCreator.jsx
│   │   │   └── exerciseStore.js
│   │   ├── correction/       # Funciones específicas para CORRECCIÓN DE TEXTO
│   │   │   ├── TextCorrector.jsx
│   │   │   └── correctionStore.js
│   │   └── chat/             # Chat (opcional para interacción general IA)
│   │       ├── ChatView.jsx
│   │       ├── MessageBubble.jsx
│   │       └── chatStore.js
│   ├── hooks/                
│   │   └── useFetch.js (hook para llamadas HTTP genéricas)
│   ├── layouts/              
│   │   ├── MainLayout.jsx (Navbar + Footer + contenido)
│   │   └── DashboardLayout.jsx
│   ├── lib/                  
│   │   ├── apiClient.js      (axios configurado)
│   │   └── skClient.js       (para llamadas específicas a tus SK plugins/agents)
│   ├── pages/                
│   │   ├── Home.jsx
│   │   ├── Dashboard.jsx
│   │   └── NotFound.jsx
│   ├── providers/            
│   │   └── SessionProvider.jsx (para manejar sesiones de usuario, tokens etc.)
│   ├── router/               
│   │   └── routes.jsx (todas las rutas centralizadas aquí)
│   ├── styles/               
│   │   └── globals.css (Tailwind conectado)
│   ├── App.jsx               
│   ├── main.jsx              
├── .env
├── tailwind.config.js
├── shadcn.config.json
├── postcss.config.js
├── package.json
└── vite.config.js
