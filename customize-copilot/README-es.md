# Lab 02 — Instrucciones Personalizadas de Copilot

Enséñale a **GitHub Copilot** a hablar el idioma de tu proyecto. Las instrucciones personalizadas, las reglas específicas por archivo y los archivos de prompt reutilizables convierten a Copilot de un asistente genérico en un experto en tu dominio que conoce tus convenciones de memoria.

## Lo que Aprenderás

El objetivo de hoy es aprender a **personalizar el comportamiento de GitHub Copilot** para que su salida sea consistente con los estándares de tu proyecto — sin repetir las mismas indicaciones en cada prompt.

- **Instrucciones Personalizadas** — Dale a Copilot contexto a nivel de proyecto, personal y de organización
- **Instrucciones Específicas por Archivo** — Aplica convenciones a archivos o directorios específicos
- **Archivos de Prompt** — Crea comandos slash reutilizables que automatizan flujos de trabajo de varios pasos
- **Skills** — Empaqueta conocimiento experto para que Copilot escriba mejor código en áreas especializadas

Al final de este lab habrás configurado instrucciones personalizadas en todos los ámbitos, corregido contenido no conforme, creado archivos de prompt para automatizar tareas repetitivas, y creado un skill que mejora el JavaScript y la seguridad de tu sitio web — todo en un sitio web de turismo con FastAPI y Uvicorn. 🌊

> ⚠️ **Importante:** Todos los archivos de personalización creados durante este lab — `copilot-instructions.md`, archivos de instrucciones (`*.instructions.md`), archivos de prompt (`*.prompt.md`), y skills (SKILL.md) — deben estar dentro del directorio **`.github`**, y este directorio `.github` **debe estar en la raíz del workspace** donde se clonó el repositorio de GitHub. Si la carpeta `.github` se coloca en otro lugar, VS Code y Copilot no la detectarán y las instrucciones/prompts no tendrán efecto.
>
> ```
> <raíz-del-repo>/          ← raíz del workspace (donde clonaste el repo)
> ├── .github/
> │   ├── copilot-instructions.md          ← instrucciones a nivel de repositorio
> │   ├── instructions/
> │   │   └── activities.instructions.md   ← instrucciones específicas por archivo
> │   ├── prompts/
> │   │   └── new-activity.prompt.md       ← archivos de prompt reutilizables
> │   └── skills/
> │       └── web-enhancer/
> │           └── SKILL.md                 ← skills de conocimiento experto
> ├── main.py
> ├── config.json
> ├── README.md
> └── ...
> ```

## Paso 1: Configuración de Instrucciones Personalizadas

Bienvenido a **SunVoyage Tours** — un portal de turismo donde los visitantes exploran actividades, vuelos y alojamientos en destinos mediterráneos. ✈️ 🏖️ 🍽️

En este paso configuraremos el entorno de desarrollo, exploraremos el sitio web, y configuraremos las instrucciones personalizadas de Copilot en los **tres niveles de ámbito**: organización, repositorio y personal.

### 📖 Teoría: ¿Qué son las Instrucciones Personalizadas?

Las instrucciones personalizadas son **reglas en lenguaje natural** que proporcionas a Copilot. Una vez configuradas, se incluyen automáticamente en cada solicitud, asegurando respuestas consistentes y con contexto en todo tu flujo de trabajo.

Piensa en ellas como una chuleta que le das a un nuevo compañero de equipo el primer día — excepto que Copilot la lee cada vez, nunca la olvida y nunca se desvía de las directrices.

Copilot soporta instrucciones en **tres niveles de ámbito**. Cada uno está diseñado para una audiencia diferente.

| Nivel | Ámbito | Configurado por | Dónde se encuentra |
| ----- | ------ | --------------- | ------------------ |
| **🥉 Organización** | Todos los miembros en todos los repos | Propietarios de la organización | GitHub.com → Configuración de la Org → Copilot → Instrucciones Personalizadas |
| **🥈 Repositorio** | Cualquiera que trabaje en este repo | Cualquier contribuidor | `.github/copilot-instructions.md` en el repo |
| **🥇 Personal** | Tus conversaciones en todas partes | Tú | `settings.json` de VS Code o configuración personal en GitHub.com |

Cuando se aplican múltiples niveles, Copilot usa **todos ellos** pero respeta esta prioridad (de mayor a menor): **Personal > Repositorio > Organización**. Las reglas que no entran en conflicto de cada nivel se combinan; cuando hay conflicto, el nivel de mayor prioridad gana.

> 💡 **Consejo:** Evita contradicciones entre niveles. Si obtienes resultados inesperados, revisa qué instrucciones están activas en cada ámbito.

---

### Actividad: Explora el proyecto con Copilot 🔍

Antes de configurar ninguna instrucción, pongamos el sitio web en marcha y usemos Copilot para aprender sobre su estructura.

1. Clona o abre este repositorio en VS Code.

2. En la barra lateral izquierda, haz clic en la pestaña **Extensiones** y verifica que las extensiones **GitHub Copilot** y **Python** estén instaladas y habilitadas.

3. Abre una terminal e instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicia el servidor de desarrollo:

   ```bash
   python main.py
   ```

5. Abre tu navegador en **http://127.0.0.1:8000** y explora el sitio web de SunVoyage Tours.

   > ❕ **Importante:** Mantén el servidor en ejecución durante todo el lab para ver los cambios en vivo.

6. Tómate un momento para mirar el sitio web. Deberías ver cuatro tarjetas de actividades, tres rutas de vuelos y tres listados de alojamientos. Nota que algunas tarjetas se ven pulidas mientras que a otras claramente les falta información — **¡las arreglaremos más adelante!**

7. Ahora preguntemos a Copilot sobre el proyecto. Abre el panel de **Copilot Chat** y asegúrate de estar en **Ask Mode**.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Por favor, explica brevemente la estructura de este proyecto.
   > ¿Qué stack tecnológico usa y cómo están organizadas las actividades?
   > ```

   > 💡 **Consejo:** Puedes arrastrar archivos (como `main.py` o `config.json`) al panel del chat para dar más contexto a Copilot. También puedes usar `#codebase` para que Copilot busque en todo el repo.

8. Navega por los archivos del proyecto para verificar la explicación de Copilot:

   | Ruta | Propósito |
   | ---- | --------- |
   | `main.py` | Aplicación FastAPI servida con Uvicorn |
   | `config.json` | Configuración central — actividades, vuelos, alojamientos |
   | `templates/index.html` | Plantilla HTML Jinja2 para la página principal |
   | `templates/activity-template.md` | Plantilla Markdown que cada README de actividad debe seguir |
   | `activities/` | Una subcarpeta por actividad, cada una con un `README.md` |
   | `static/` | Recursos CSS y JavaScript |

---

### 📖 Instrucciones a Nivel de Organización

Las instrucciones a nivel de organización son configuradas por los **propietarios de la organización** (planes GitHub Business o Enterprise) y se aplican a **todos los miembros** en todos los repositorios de la organización. Piensa en esto como la "política de empresa" que cada miembro del equipo hereda automáticamente.

**Cómo configurar:**

Como las instrucciones de organización requieren **acceso de administrador a una organización de GitHub**, esta parte es una revisión guiada en lugar de un ejercicio práctico.

1. Navega a la **Configuración** de tu organización en GitHub.com.
2. En la barra lateral, haz clic en **Copilot → Custom instructions**.
3. Añade tus instrucciones en lenguaje natural y haz clic en **Save changes**. Aquí tienes un ejemplo de lo que SunVoyage Tours podría configurar a nivel de organización:

   ```text
   SunVoyage Tours is a Mediterranean tourism company headquartered in Spain.
   All customer-facing content must be professional and inviting.
   Prices must always be displayed in euros (€).
   All dates should use European format (DD/MM/YYYY).
   Comply with EU GDPR regulations when handling user data.
   Prefer Python for backend services and vanilla JS for frontend code.
   ```

4. **Pregunta para discusión:** Si esta fuera tu organización, ¿qué estándares adicionales a nivel de empresa añadirías?

   <details>
   <summary>Ideas de ejemplo 💡</summary>

   - _"Todas las respuestas de la API deben incluir códigos de estado HTTP adecuados"_
   - _"Nunca hacer commit de secretos o claves API al repositorio"_
   - _"Escribir documentación en inglés con un tono profesional"_
   - _"Preferir type hints en todas las firmas de funciones Python"_

   </details>

> 📚 Documentación completa: [Adding organization custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-organization-instructions)

> 🪧 **Nota:** Las instrucciones de organización actualmente están soportadas para Copilot Chat en GitHub.com, revisión de código de Copilot, y el agente de codificación de Copilot.

---

### 📖 Instrucciones a Nivel de Repositorio

Las instrucciones de repositorio viven dentro del repo en un archivo llamado **`.github/copilot-instructions.md`**. Se adjuntan automáticamente a cada solicitud de Copilot Chat realizada en el contexto de ese repositorio.

**Cómo configurar:**

1. Crea un archivo `.github/copilot-instructions.md` en la raíz de tu repositorio.
2. Escribe instrucciones en lenguaje natural describiendo tu proyecto.
3. Guarda — Copilot lo detecta inmediatamente.

> 📚 Documentación completa: [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=visualstudio)

> 💡 **Consejo:** Mantén las instrucciones cortas y enfocadas en el **"cómo"** del proyecto: propósito, estructura de carpetas, estándares de código, herramientas clave, formatos esperados, etc.

### Actividad: Crea instrucciones de repositorio con Copilot 🤖

Ahora mismo Copilot no conoce **verdaderamente** las convenciones de nuestro proyecto. Si le pedimos crear contenido, podría usar el formato de precio incorrecto, duraciones inconsistentes o un tono informal. Vamos a arreglar eso creando instrucciones a nivel de repositorio.

En lugar de crear el archivo manualmente, ¡usemos el **Modo Agente** para hacer el trabajo pesado!

1. Abre el panel de **Copilot Chat** y cambia al modo **Agent**.

2. Pide a Copilot que cree el archivo de instrucciones. Proporciona suficiente contexto para que entienda lo que debe contener:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a .github/copilot-instructions.md file for this project.
   > It should describe:
   > - The project (a tourism portal built with Python/FastAPI/Uvicorn)
   > - The tech stack (FastAPI, Jinja2, vanilla JS, JSON config)
   > - The project structure (main.py, config.json, templates/, activities/, static/)
   > - Conventions: prices in €XX / person format, locations as City Country,
   >   durations in full words, Title Case categories, activity READMEs must follow
   >   the template in templates/activity-template.md, professional tone.
   > ```

3. Revisa el archivo que Copilot crea. Debería parecerse a esto:

   <details>
   <summary>Contenido esperado 📄</summary>

   ```markdown
   # SunVoyage Tours — Project Instructions

   ## Project Description

   SunVoyage Tours is a tourism portal built with **Python and FastAPI**, served via **Uvicorn**. Visitors can browse tourist activities, flights, and accommodations across Mediterranean destinations.

   ## Tech Stack

   - **Backend:** Python 3 / FastAPI / Uvicorn
   - **Templating:** Jinja2 (HTML templates in `templates/`)
   - **Frontend:** Vanilla HTML, CSS, and JavaScript (in `static/`)
   - **Data:** JSON-based configuration (`config.json`)

   ## Project Structure

   - [`main.py`](../main.py) — FastAPI application entry point
   - [`config.json`](../config.json) — Central data source for activities, flights, and accommodations
   - [`templates/`](../templates/) — Jinja2 HTML templates and content templates
   - [`activities/`](../activities/) — Each activity has its own subfolder with a `README.md`
   - [`static/`](../static/) — CSS stylesheets and JavaScript files

   ## Conventions

   - All prices must use the euro symbol and include "/ person" or "/ night" suffix (e.g., `€75 / person`)
   - Locations must follow the format `City, Country` (e.g., `Costa del Sol, Spain`)
   - Duration values must use full words (e.g., `2 hours` not `2h`)
   - Activity categories must use Title Case (e.g., `Water Sports` not `water`)
   - Every activity folder must contain a `README.md` following the structure in [`templates/activity-template.md`](../templates/activity-template.md)
   - Keep the website professional and customer-friendly in tone
   ```

   </details>

4. Si al resultado de Copilot le faltan algunas convenciones, proporciona feedback de seguimiento para refinarlo. Recuerda — Copilot mantiene el historial de conversación, ¡así que puedes iterar!

5. **Acepta los cambios** y guarda el archivo.

   > ❕ **Importante:** El archivo debe estar exactamente en `.github/copilot-instructions.md`. Si Copilot lo colocó en otro sitio, muévelo.

### Actividad: Prueba tus instrucciones de repositorio ✅

Ahora verifiquemos que Copilot realmente usa las instrucciones que acabas de crear.

1. Asegúrate de estar en modo **Agent** en Copilot Chat.

2. Haz a Copilot una pregunta que ejercite tus convenciones:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > What conventions does the project have regarding the city, the money and the title of the activity?
   > ```

3. Copilot debería responder con `€50 / person` — siguiendo la convención que estableciste.

4. Revisa la sección **References** en la parte inferior de la respuesta de Copilot. Deberías ver `.github/copilot-instructions.md` listado, confirmando que fue utilizado.

   <details>
   <summary>¿No ves la referencia? 🔍</summary>

   - Asegúrate de que el archivo está guardado exactamente en `.github/copilot-instructions.md` (no en una subcarpeta).
   - Reinicia VS Code si el archivo se acaba de crear.
   - Verifica que la configuración **"Enable custom instructions"** está marcada en la configuración de VS Code (busca `copilot instructions`).

   </details>

5. Prueba una vez más — pide a Copilot que describa el proyecto con sus propias palabras:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Can you briefly describe the project structure?
   > ```

   Copilot ahora debería mencionar FastAPI, Uvicorn, actividades, vuelos y alojamientos — lenguaje que no habría conocido sin tus instrucciones. ¡Eso por sí solo es un gran impulso de productividad para incorporar compañeros de equipo!

   **🎯 Objetivo: Copilot referencia tu archivo de instrucciones y sigue las convenciones del proyecto. ✅**

---

### 📖 Instrucciones a Nivel Personal

Las instrucciones personales reflejan tu **rol individual y preferencias**. Te siguen en todos tus proyectos y no se incluyen en el repositorio.

**Cómo configurar (GitHub.com):**

1. Abre [Copilot Chat](https://github.com/copilot).
2. Haz clic en tu foto de perfil → **Personal instructions**.
3. Escribe tus preferencias y haz clic en **Save**.

**Cómo configurar (VS Code):**

Abre el **Chat Customizations editor** haciendo clic en **Configure Chat** (icono de engranaje) en la vista de Chat. Desde ahí puedes crear y gestionar archivos de instrucciones asociados a tu perfil de usuario.

> 📚 Documentación completa: [Adding personal custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-personal-instructions)
>
> 📚 Visión general de personalización en VS Code: [Customize AI in Visual Studio Code](https://aka.ms/vscode-ghcp-custom-instructions)

### Actividad: Añade instrucciones personales en VS Code 🧑‍💻

En este ejercicio, imagina que eres el **responsable de producto de Deportes Acuáticos** en SunVoyage Tours. Tu enfoque son las actividades acuáticas y quieres que Copilot siempre priorice esa área.

1. En el panel de **Copilot Chat**, haz clic en **Configure Chat** (icono de engranaje ⚙️) en la parte superior para abrir el **Chat Customizations editor**.

2. En la sección **Instructions**, haz clic en la flecha desplegable (▾) junto a **Generate Instructions** y selecciona **New Instructions (User)**.

   > 🪧 **Nota:** Seleccionar ámbito **User** significa que esta instrucción se aplica a todos tus proyectos — no solo a este repo. Eso es lo que la convierte en una instrucción *personal*.

3. Cuando se te pida introducir un nombre de archivo, escribe:

   ```text
   water-sports-manager
   ```

4. Selecciona el directorio **`.copilot\instructions`** (por ejemplo, `C:\Users\<tu-usuario>\.copilot\instructions`).

5. VS Code creará y abrirá un nuevo archivo `.instructions.md` con texto de ejemplo. Necesitas actualizar dos cosas:

   - **Reemplaza el placeholder de `description`** en el frontmatter con:

     ```text
     This instruction file should be used whenever the user asks for activities, suggestions, or content related to water sports. It ensures that the agent prioritizes water-based experiences and includes necessary safety warnings.
     ```

   - **Reemplaza el contenido del placeholder** (debajo del cierre `---` del frontmatter) con:

     ```text
     I am the Water Sports product manager. When listing, suggesting, or creating activities, always prioritize water-based experiences (jet skiing, kayaking, surfing, diving, sailing). Include detailed safety warnings for any water-related activity. When generating content in Spanish, use European Spanish.
     ```

6. Guarda el archivo.

### Actividad: Prueba las instrucciones personales 🏄

1. Abre **Copilot Chat** en modo **Agent** y pregunta:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Suggest three new activities we could add to the SunVoyage Tours website
   > ```

2. Observa que las sugerencias de Copilot **se inclinan hacia actividades acuáticas** — surf, buceo, snorkel, vela — reflejando tu instrucción personal.

3. Compara esto con lo que vería un compañero sin tus instrucciones personales. Obtendría una mezcla más equilibrada de tipos de actividades, porque las instrucciones del repositorio no priorizan ninguna categoría.

   > 🪧 **Nota:** Las instrucciones personales se almacenan localmente en tu configuración de VS Code y **no** se incluyen en el repositorio. Te siguen en todos tus proyectos.

   **🎯 Objetivo: Copilot recomienda principalmente actividades acuáticas porque tus instrucciones personales tienen la mayor prioridad. ✅**

---

### Resumen de Prioridades

Ahora que los tres niveles están configurados, asegurémonos de que el modelo de prioridad queda claro:

| Prioridad | Nivel | Lo que configuraste |
| --------- | ----- | ------------------- |
| 🥇 Más alta | **Personal** | Enfoque de responsable de Deportes Acuáticos |
| 🥈 Media | **Repositorio** | Estructura del proyecto, convenciones, reglas de formato |
| 🥉 Más baja | **Organización** | Estándares de empresa (euros, GDPR, tono profesional) |

**Pregunta para discusión:** ¿Qué pasa si la organización dice "usar inglés británico" pero tus instrucciones personales dicen "usar español europeo"?

<details>
<summary>Respuesta 💡</summary>

Los tres conjuntos de instrucciones se envían a Copilot, pero **las instrucciones personales tienen la mayor prioridad**, seguidas por las del repositorio y luego las de la organización. Si tu instrucción personal dice "usar español europeo", Copilot favorecerá eso sobre la preferencia de "inglés británico" de la org. Las instrucciones restantes que no entran en conflicto de todos los niveles se siguen aplicando.

</details>

---

## Paso 2: Instrucciones Específicas por Archivo — Corrección Guiada

¡Buen trabajo configurando instrucciones en los tres niveles! Ahora vamos a abordar un escenario más específico.

🐛 **HAY UN PROBLEMA EN LOS ARCHIVOS DE ACTIVIDADES** 🐛

Los archivos de contenido de actividades en este repositorio **no siguen todos los mismos estándares**. Abre `activities/kayaking/README.md` y compáralo con `activities/jet-skiing/README.md` — verás las inconsistencias inmediatamente. El archivo de kayaking tiene formato incorrecto, secciones faltantes y un tono poco profesional.

Necesitamos una forma de aplicar automáticamente la plantilla de actividades en cada archivo markdown de actividad. Ahí es donde entran las **instrucciones específicas por archivo**.

### 📖 Teoría: Archivos de Instrucciones Personalizadas

Los archivos de instrucciones (`*.instructions.md`) proporcionan a Copilot orientación específica para **archivos o directorios concretos**. A diferencia de las instrucciones de repositorio que se aplican en todas partes, estos usan el campo `applyTo` en el [frontmatter](https://jekyllrb.com/docs/front-matter/) con [sintaxis glob](https://code.visualstudio.com/docs/editor/glob-patterns) para apuntar a rutas específicas.

VS Code busca archivos `*.instructions.md` en el directorio `.github/instructions/` por defecto. Cuando Copilot trabaja en un archivo que coincide con el patrón glob, las instrucciones se **adjuntan automáticamente** — sin necesidad de acción manual.

> 💡 **Consejo:** Las instrucciones deben enfocarse en el **CÓMO** se debe hacer una tarea — las directrices, estándares y convenciones para esa parte particular del código.

### Actividad: Identifica el problema 🔍

1. Abre el archivo `activities/kayaking/README.md` y revisa su contenido.

2. Ahora abre `templates/activity-template.md` para ver la estructura esperada.

3. Compara los dos archivos. Nota que el archivo de kayaking tiene múltiples problemas:

   | Problema | Archivo Kayaking | Esperado |
   | -------- | ---------------- | -------- |
   | Título | `# Kayaking in Mallorca` | `# 🛶 Kayaking Adventure` (con emoji) |
   | Sección Overview | Falta completamente | Requerida con 1–2 frases |
   | Tabla de detalles | Texto plano (`Duration: 2h`) | Tabla markdown estructurada |
   | Formato de precio | `45 euro` | `€45 / person` |
   | Formato de duración | `2h` | `2 hours` |
   | Formato de ubicación | `Mallorca` | `Mallorca, Spain` |
   | What's Included | Falta | Requerido |
   | Safety Information | Falta | Requerido |
   | Requirements | Falta | Requerido (separado de "What to bring") |
   | Sección Booking | Falta | Requerida |
   | Tono | Informal (`trust us!`) | Profesional y orientado al cliente |

4. También revisa la entrada de kayaking en `config.json` — tiene problemas similares (imagen vacía, precio plano `"45"`, categoría en minúsculas `"water"`).

### Actividad: Crea instrucciones específicas de actividades con Copilot 🤖

En lugar de escribir el archivo de instrucciones desde cero, pidamos al **Modo Agente** que lo cree por nosotros — mientras también le enseñamos lo que el archivo necesita contener.

1. Abre **Copilot Chat** y cambia al modo **Agent**.

2. Arrastra el archivo `templates/activity-template.md` al chat como contexto, y luego pide a Copilot que genere el archivo de instrucciones:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a file at .github/instructions/activities.instructions.md
   > It should have an applyTo frontmatter targeting "activities/**/*.md"
   > and contain rules for activity markdown files:
   > - Must follow the structure in templates/activity-template.md
   > - Each activity must be a README.md in its own subfolder
   > - Section headers must include the correct emoji icons
   > - Prices: €XX / person format
   > - Durations: full words (2 hours not 2h)
   > - Locations: City, Country format
   > - Categories: Title Case
   > - Tone: professional and inviting, no slang
   > ```

3. Revisa el archivo que Copilot crea. Debería tener un bloque de frontmatter YAML con `applyTo: "activities/**/*.md"` y un conjunto de reglas claras en markdown.

   <details>
   <summary>Estructura esperada 📄</summary>

   El archivo debería ser similar a:

   ```markdown
   ---
   applyTo: "activities/**/*.md"
   ---

   # Activity Markdown Structure Guidelines

   All activity markdown files must follow these guidelines:

   ## 1. Template Usage

   - Activity markdown files must follow the structure in [`templates/activity-template.md`](../../templates/activity-template.md).
   - Each activity must be a `README.md` file inside its own subfolder of `activities/`.
   - Do not skip or remove required sections from the template.

   ## 2. Section Guidance

   The section headers must match the template structure exactly, including the emoji icons:

   - **Title**: Use a relevant emoji followed by the activity name (e.g., `# 🛶 Kayaking Adventure`).
   - **📋 Overview**: Write 1–2 sentences describing the experience. Use professional, customer-friendly language.
   - **📍 Details**: Present details as a markdown table with fields: Category, Location, Duration, Price, Difficulty, Min. Age.
   - **✅ What's Included**: Bullet list of what the customer gets.
   - **📝 Requirements**: Bullet list of prerequisites or things to bring.
   - **⚠️ Safety Information**: Bullet list of safety warnings.
   - **📞 Booking**: Contact information for reservations.

   ## 3. Formatting Rules

   - **Prices**: Always use the format `€XX / person` (euro symbol, space, slash, space, "person").
   - **Durations**: Use full words (e.g., `2 hours` not `2h`).
   - **Locations**: Use `City, Country` format (e.g., `Mallorca, Spain`).
   - **Categories**: Use Title Case (e.g., `Water Sports` not `water`).
   - **Tone**: Professional and inviting. Avoid slang or overly casual phrasing.
   ```

   </details>

4. **Acepta los cambios** y guarda el archivo.

### Actividad: Corrige la actividad de kayaking con Copilot 🛶

Ahora el archivo de instrucciones existe y se aplica automáticamente a cualquier archivo bajo `activities/**/*.md`. Pongámoslo a prueba.

1. Abre `activities/kayaking/README.md` en VS Code.

2. Abre **Copilot Chat** y asegúrate de estar en modo **Agent**.

3. Con el archivo de kayaking abierto, pide a Copilot que lo corrija:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Update this activity file to follow the project standards and template structure
   > ```

4. Observa cómo Copilot referencia **tanto** las instrucciones personales (`.github/instructions/water-sport-manager.md`) como las instrucciones específicas de actividades (`.github/instructions/activities.instructions.md`) en las referencias de su respuesta.

5. Revisa los cambios propuestos:
   - El título ahora debería tener un emoji
   - Se debería añadir una sección Overview
   - Los detalles deberían estar en una tabla markdown adecuada
   - Precios, duraciones y ubicaciones deberían seguir el formato correcto
   - Las secciones faltantes (What's Included, Safety, Requirements, Booking) deberían añadirse
   - El tono debería ser profesional

6. **Acepta los cambios** y guarda el archivo.

### Actividad: Corrige la entrada de kayaking en config 🔧

El README está corregido, pero la entrada de `config.json` para kayaking sigue sin cumplir. Arreglemos eso también.

1. Abre `config.json` y encuentra la entrada de `kayaking`.

2. En modo **Agent**, pide a Copilot:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > The kayaking entry in config.json doesn't follow our conventions.
   > Fix the category, price, duration, location, and image fields
   > to match the format used by the other activities.
   > ```

3. Verifica que la entrada actualizada se parezca a:

   ```json
   {
     "id": "kayaking",
     "name": "Kayaking Adventure",
     "category": "Water Sports",
     "price": "€45 / person",
     "duration": "2 hours",
     "location": "Mallorca, Spain",
     "image": "🛶",
     "folder": "activities/kayaking"
   }
   ```

4. **Reinicia el servidor** (`Ctrl+C` y luego `python main.py`) y refresca el navegador para verificar que la tarjeta de kayaking ahora se ve correcta en el sitio web.

   **🎯 Objetivo: La tarjeta de kayaking en el sitio web muestra un emoji adecuado, precio formateado, duración completa y ubicación correcta. ✅**

<details>
<summary>¿Tienes problemas? 🤷</summary>

- Asegúrate de que el archivo de instrucciones está en `.github/instructions/activities.instructions.md`.
- El campo `applyTo` debe ser `"activities/**/*.md"` — comprueba errores tipográficos.
- Reinicia VS Code si las instrucciones no parecen aplicarse.
- Si el sitio web no se actualiza, asegúrate de haber guardado `config.json` y reiniciado el servidor.

</details>

---

## Paso 3: Instrucciones Específicas por Archivo — ¡Tu Turno! 🏆

Has corregido exitosamente la actividad de kayaking con la ayuda de Copilot. ¡Ahora es tiempo de quitar las rueditas y aplicar lo que has aprendido por tu cuenta!

### El Escenario

Abre `activities/sightseeing/README.md`. Este archivo tiene un **conjunto diferente de problemas** comparado con el de kayaking:

- Al título le falta su icono emoji
- Los nombres de las secciones no coinciden con la plantilla (`"About this tour"` en lugar de `"📋 Overview"`, `"Extras"` en lugar de `"✅ What's Included"`)
- Los detalles están en una lista con viñetas en lugar de una tabla markdown
- Las secciones `"⚠️ Safety Information"` y `"📝 Requirements"` faltan completamente
- La sección `"📞 Booking"` usa un email diferente y le falta el número de teléfono

### Tu Tarea

1. Usa Copilot en modo **Agent** para **actualizar la actividad de sightseeing** para que coincida con la estructura de la plantilla de actividades — igual que hiciste con el archivo de kayaking.

2. Piensa si el archivo `.github/instructions/activities.instructions.md` existente ya cubre este caso, o si necesitas ajustarlo.

3. No olvides verificar que el resultado coincida con la plantilla comparándolo con `activities/jet-skiing/README.md` (un ejemplo correctamente formateado).

4. **Bonus:** Comprueba si la entrada de sightseeing en `config.json` también necesita correcciones. ¿El formato de precio, mayúsculas de categoría, u otros campos necesitan actualización?

<details>
<summary>Pistas 💡</summary>

- El archivo de instrucciones que creaste en el Paso 2 usa `applyTo: "activities/**/*.md"` — ¡también se aplica al archivo de sightseeing! Puedes reutilizar el mismo prompt de Copilot.
- Abre primero el archivo de sightseeing, luego pide a Copilot en modo **Agent**:

  > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
  >
  > ```prompt
  > Update this activity file to follow the project standards and template structure
  > ```

- Después de corregir el README, pide a Copilot que también revise y corrija la entrada de sightseeing en `config.json`.

</details>

<details>
<summary>Resultado esperado ✅</summary>

Después de la corrección, el `README.md` de sightseeing debería tener:
- Un título con emoji: `# 🏛️ City Sightseeing Tour`
- Las seis secciones requeridas con encabezados emoji correctos
- Una tabla de detalles estructurada con formato adecuado
- Lenguaje profesional y orientado al cliente en todo el contenido
- Información completa de contacto para reservas

</details>

**🎯 Objetivo: Ambas actividades no conformes (kayaking y sightseeing) están corregidas para coincidir con la plantilla. Todas las tarjetas de actividades en el sitio web se ven consistentes y profesionales. ✅**

---

## Paso 4: Archivos de Prompt Reutilizables — Guiado

Ahora que todas las actividades existentes siguen una estructura consistente, quieres facilitar la **creación de nuevas actividades** sin configurar manualmente cada archivo. Este es un escenario perfecto para un **archivo de prompt** — un comando slash reutilizable que automatiza flujos de trabajo repetitivos.

### 📖 Teoría: ¿Qué son los Archivos de Prompt?

Los archivos de prompt (`*.prompt.md`) definen prompts reutilizables que aparecen como **comandos slash** (`/`) en Copilot Chat. Pueden referenciar otros archivos del workspace (como plantillas y configuraciones) para proporcionar contexto.

| Aspecto | Detalles |
| ------- | -------- |
| **Extensión de archivo** | `.prompt.md` |
| **Ubicación por defecto** | Directorio `.github/prompts/` |
| **Invocación** | Escribe `/nombre-del-prompt` en la entrada de Copilot Chat |
| **Contexto** | Puede referenciar archivos usando enlaces markdown o sintaxis `#file:` |
| **Ámbito** | Reutilizable por cualquiera que clone el repositorio |

> 💡 **Consejo:** Usa archivos de prompt para definir tareas y flujos de trabajo repetibles. Enfócate en **QUÉ** necesita hacerse. Referencia instrucciones para el **CÓMO**.

Consulta la [documentación de VS Code: Prompt Files](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) para más información.

### Actividad: Crea el prompt de nueva actividad con Copilot 🤖

¡Usemos el **Modo Agente** para ayudarnos a escribir el archivo de prompt — los archivos de prompt son solo markdown, y Copilot es excelente escribiendo markdown!

1. Abre **Copilot Chat** en modo **Agent**.

2. Pide a Copilot que cree el archivo de prompt:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a reusable prompt file at .github/prompts/new-activity.prompt.md
   > that automates creating a new tourism activity.
   > It should:
   > - Have frontmatter with agent: agent, a description, and an argument-hint
   > - Step 1: Gather activity info from the user if not provided
   > - Step 2: Create a new directory in activities/ with a README.md
   >   following the structure from templates/activity-template.md
   > - Step 3: Update config.json with the new activity entry
   >   using the same field format as existing entries
   > Reference the template and config.json files using relative markdown links.
   > ```

3. Revisa el archivo que Copilot crea. Debería contener:

   <details>
   <summary>Contenido esperado 📄</summary>

   ```markdown
   ---
   agent: agent
   description: Create a new tourism activity for the SunVoyage website
   argument-hint: Provide the activity name and type (e.g., "Scuba Diving - Water Sports")
   ---

   # Create New Tourism Activity

   Your goal is to generate a new activity for the SunVoyage Tours website.

   ## Step 1: Gather Activity Information

   If not already provided by the user, ask for:
   - Activity name
   - Category (Water Sports, Cultural, Gastronomy, Adventure, Wellness, etc.)
   - Location (City, Country)
   - Approximate price and duration

   ## Step 2: Create Activity Structure

   1. Create a new directory in the `activities` folder with a kebab-case name based on the activity (e.g., `scuba-diving`)
   2. Create a `README.md` file in that directory following the structure from [activity-template.md](../../templates/activity-template.md)
   3. Fill in all sections with realistic, professional content appropriate for a tourism website

   ## Step 3: Update Website Configuration

   Update the activities list in [config.json](../../config.json) to include the new activity. Use the same field format as existing entries:
   - `id`: kebab-case identifier
   - `name`: display name
   - `category`: Title Case category
   - `price`: format `€XX / person`
   - `duration`: full words (e.g., `2 hours`)
   - `location`: `City, Country`
   - `image`: a relevant emoji
   - `folder`: path to the activity folder
   ```

   </details>

4. **Acepta los cambios** y guarda el archivo.

### Actividad: Prueba el prompt de nueva actividad 🧪

1. Abre **Copilot Chat** y asegúrate de estar en modo **Agent**.

2. Escribe `/new-activity` en la entrada del chat. Tienes dos opciones:

   - Escribe solo `/new-activity` sin detalles — Copilot preguntará de qué debería ser la actividad.
   - Incluye los detalles directamente: `/new-activity Sunset Sailing Cruise - Water Sports in Ibiza, Spain`

   <details>
   <summary>💡 Ideas de actividades para probar</summary>

   ```text
   Scuba Diving Adventure - Water Sports in Costa Brava, Spain
   ```

   ```text
   Flamenco Dance Workshop - Cultural in Seville, Spain
   ```

   ```text
   Mountain Hiking Trail - Adventure in Sierra Nevada, Spain
   ```

   ```text
   Tapas Cooking Class - Gastronomy in Valencia, Spain
   ```

   ```text
   Sunset Yacht Cruise - Water Sports in Mallorca, Spain
   ```

   </details>

3. Observa a Copilot trabajar. Debería:
   - Crear una nueva carpeta bajo `activities/`
   - Generar un `README.md` siguiendo la estructura de la plantilla
   - Actualizar `config.json` con una nueva entrada

4. **Reinicia el servidor** y verifica que la nueva actividad aparece en el sitio web.

5. Compara el contenido generado con tus actividades existentes. ¿Sigue todas las convenciones de tus instrucciones?

   > 🪧 **Nota:** Las instrucciones específicas de actividades (`activities.instructions.md`) se aplican automáticamente porque el nuevo archivo coincide con `activities/**/*.md`. ¡Tu archivo de prompt definió **qué** hacer, y el archivo de instrucciones impuso **cómo** hacerlo!

<details>
<summary>¿La actividad no aparece en el sitio web? 🔍</summary>

- Asegúrate de haber reiniciado el servidor después de los cambios.
- Verifica que `config.json` se actualizó correctamente (JSON válido, nueva entrada en el array `activities`).
- Comprueba que la nueva carpeta existe bajo `activities/` con un archivo `README.md`.

</details>

**🎯 Objetivo: Un solo comando slash genera una actividad completamente conforme — carpeta, README y entrada en config — en segundos. ✅**

---

## Paso 5: Archivos de Prompt Reutilizables — ¡Tu Turno! 🏆

Has automatizado la creación de actividades con un archivo de prompt. Ahora piensa en qué **otras tareas repetitivas** de este proyecto podrían beneficiarse del mismo enfoque.

### El Escenario

El sitio web de SunVoyage Tours también gestiona **vuelos** y **alojamientos** a través de `config.json`. Añadir nuevas entradas requiere conocer la estructura JSON exacta, los nombres de campos y las convenciones de formato. Esto es propenso a errores y lento cuando se hace manualmente.

### Tu Tarea

Crea un **nuevo archivo de prompt** que automatice uno de estos flujos de trabajo:

1. **Opción A:** Crea un prompt `/new-flight` que añada una nueva ruta de vuelo a `config.json`
2. **Opción B:** Crea un prompt `/new-accommodation` que añada un nuevo listado de alojamiento a `config.json`
3. **Opción C (Avanzado):** Crea un prompt `/travel-package` que combine un vuelo + alojamiento + actividad en un paquete especial y lo añada como nueva sección en `config.json` y el sitio web

### Requisitos

- El archivo de prompt debe estar en `.github/prompts/` con la extensión `.prompt.md`
- Debe incluir `agent: agent`, una `description` y un `argument-hint` en el frontmatter
- Debe referenciar `config.json` para que Copilot cree la nueva entrada que aparecerá en el sitio web
- Debe guiar a Copilot para seguir las mismas convenciones de formato (precios en euros, formato de ubicación, etc.)

> 💡 **Consejo:** ¡Puedes usar el **Modo Agente** para generar el archivo de prompt! — igual que hicimos en el Paso 4. Prueba pedir a Copilot:
>
> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
>
> ```prompt
> Create a prompt file similar to .github/prompts/new-activity.prompt.md
> but for adding a new flight route to the website.
> ```

<details>
<summary>Pistas 💡</summary>

- Mira las entradas de vuelos existentes en `config.json` para entender la estructura de campos (`id`, `route`, `airline`, `price`, `duration`, `frequency`).
- Tu archivo de prompt debería referenciar `config.json` con un enlace markdown relativo igual que el prompt de actividades: `[config.json](../../config.json)`.
- Para la Opción C, necesitarías añadir un nuevo array `"packages"` a `config.json` y actualizar `templates/index.html` para mostrarlo. Este es un reto mayor — ¡considera usar **Plan Agent** primero para diseñar el enfoque!
- Empieza con la Opción A o B si es tu primera vez — la Opción C es un reto adicional.

</details>

<details>
<summary>Ejemplo: estructura del prompt /new-flight ✅</summary>

```markdown
---
agent: agent
description: Add a new flight route to the SunVoyage website
argument-hint: Provide route details (e.g., "Berlin → Mallorca, 2h 45m, €159")
---

# Add New Flight Route

Your goal is to add a new flight route to the SunVoyage Tours website.

## Step 1: Gather Flight Information

If not already provided, ask for:
- Origin and destination cities
- Flight duration
- Price
- Frequency (which days of the week)

## Step 2: Update Configuration

Add the new flight to the `flights` array in [config.json](../../config.json) following the existing format:
- `id`: kebab-case short identifier (e.g., `ber-mal`)
- `route`: use arrow format (e.g., `Berlin → Mallorca`)
- `airline`: always `SunVoyage Air`
- `price`: euro format (e.g., `€159`)
- `duration`: compact format (e.g., `2h 45m`)
- `frequency`: comma-separated days or `Daily`
```

</details>

**🎯 Objetivo: Tienes al menos un archivo de prompt adicional que automatiza la adición de vuelos, alojamientos o paquetes al sitio web. ✅**

---

## Paso 6: Skills — Guiado

Has personalizado cómo Copilot entiende tu proyecto y automatizado la creación de contenido. Pero, ¿qué pasa con la **calidad del código** que escribe? Ahora mismo, cuando Copilot genera JavaScript para el sitio web, usa conocimiento genérico. No sabe que preferimos ciertos patrones o que nos importa la seguridad.

Ahí es donde entran los **Skills**. Un skill es un pequeño archivo de **conocimiento experto** que Copilot lee antes de escribir código — como darle una chuleta de un desarrollador senior.

### 📖 Teoría: ¿Qué son los Skills?

Un skill es un archivo `SKILL.md` que le da a Copilot conocimiento experto en un dominio. Mientras las instrucciones dicen "sigue estas reglas" y los prompts dicen "haz esta tarea", un skill dice **"así es como un experto lo hace — aplica este conocimiento."**

| Aspecto | Detalles |
| ------- | -------- |
| **Nombre del archivo** | `SKILL.md` |
| **Ubicación** | Dentro de una carpeta bajo `.github/skills/` |
| **Frontmatter** | `name` y `description` — le dice a Copilot cuándo usarlo |
| **Contenido** | Buenas prácticas, patrones, y lo que sí/no hacer |

> 💡 **Consejo:** Mantén los skills enfocados en un área. Un skill pequeño y específico es más útil que uno masivo y genérico.

❕ **Importante:** El campo `description` en el frontmatter es **la parte más crítica** de un skill. Copilot lo lee para decidir si cargar el skill para una tarea dada. Si la descripción no menciona las palabras clave correctas (por ejemplo, "JavaScript", "security", "web"), Copilot no sabrá cuándo aplicarlo — y tu skill será ignorado. Haz la descripción específica e incluye los términos clave que coincidan con el tipo de tareas para las que quieres que el skill se active.

Consulta la [documentación de VS Code: Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) para más información.

### Actividad: Crea un skill simple de web-enhancer 🧑‍💻

Vamos a construir un skill pequeño que enseñe a Copilot dos cosas: **patrones modernos de JavaScript** y **reglas básicas de seguridad**. Esto es suficiente para mejorar notablemente el código que genera para nuestro sitio web.

1. Crea el archivo del skill:

   ```text
   .github/skills/web-enhancer/SKILL.md
   ```

2. Añade el siguiente contenido:

   ```markdown
   ---
   name: web-enhancer
   description: 'Best practices for JavaScript and security in web projects. Use when writing or modifying HTML, CSS, or JavaScript code.'
   ---

   # Web Enhancer Skill

   Apply these rules when writing or modifying frontend code.

   ## JavaScript Rules

   - Use `const` and `let` — never `var`
   - Use `addEventListener` — never inline `onclick` attributes
   - Use `querySelector` / `querySelectorAll` for DOM selection
   - Use `async`/`await` with try/catch for fetch calls
   - Use template literals instead of string concatenation
   - Always handle the case where an element might not exist before using it

   ## Security Rules

   - Use `textContent` instead of `innerHTML` when inserting user-provided text
   - Never use `eval()` or `new Function()` with dynamic strings
   - Validate and sanitize any user input before using it
   - Do not store sensitive data in `localStorage`

   ## Do's and Don'ts

   - ✅ Use semantic HTML (`<nav>`, `<main>`, `<section>`, `<article>`)
   - ✅ Add `loading="lazy"` to images below the fold
   - ✅ Use `defer` for script tags
   - ✅ Provide error feedback to the user, not just console logs
   - ❌ Never insert unsanitized user input into the DOM
   - ❌ Never use inline styles — use CSS classes
   - ❌ Never ignore errors from fetch calls
   ```

3. Guarda el archivo.

### Actividad: Mira el skill en acción 🚀

Antes de probar el skill, tómate un momento para ver el estado actual del código. Abre `static/js/app.js` y `templates/index.html` y observa estos problemas — el sitio web funciona bien, pero el código está **lleno de malas prácticas**:

| Archivo | Problema | Regla del skill violada |
| ------- | -------- | ----------------------- |
| `app.js` | Usa `var` en todas partes | JS: usar `const`/`let` |
| `app.js` | Usa `getElementById` y `getElementsByTagName` | JS: usar `querySelector` |
| `app.js` | Usa `anchors[i].onclick = ...` | JS: usar `addEventListener` |
| `app.js` | Usa concatenación de strings (`"Loaded " + data.length`) | JS: usar template literals |
| `app.js` | `fetch()` sin manejo de errores (sin try/catch, sin `.catch()`) | JS: usar async/await con try/catch |
| `app.js` | Establece `innerHTML` con strings concatenados | Seguridad: usar `textContent` |
| `app.js` | Almacena `"demo-secret-token-abc123"` en `localStorage` | Seguridad: no almacenar secretos |
| `index.html` | Estilos inline en el subtítulo hero (`style="font-size:..."`) | No hacer: usar clases CSS |
| `index.html` | Botón de scroll-to-top creado enteramente con estilos inline | No hacer: usar clases CSS |
| `index.html` | Usa `btn.onclick = ...` y `window.onscroll = ...` | JS: usar `addEventListener` |
| `index.html` | Etiqueta script al final sin `defer` | Sí hacer: usar `defer` |

Ahora pidamos a Copilot que los corrija — con el skill guiando la salida.

1. Abre **Copilot Chat** en modo **Agent**.

2. Pide a Copilot que limpie el código:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Review the JavaScript in static/js/app.js and the inline scripts in
   > templates/index.html. Fix any code quality and security issues.
   > ```

> 💡 **Consejo:** Arrastra los archivos al chat para darle más contexto.

3. Revisa los cambios. Con el skill activo, Copilot debería:
   - Reemplazar `var` con `const`/`let`
   - Cambiar de `getElementById`/`getElementsByTagName` a `querySelector`/`querySelectorAll`
   - Reemplazar asignaciones `onclick`/`onscroll` con `addEventListener`
   - Usar template literals en lugar de concatenación de strings
   - Envolver `fetch()` en `async`/`await` con try/catch
   - Reemplazar `innerHTML` con `textContent` o alternativas seguras
   - Eliminar el token secreto de `localStorage`
   - Mover estilos inline a clases CSS
   - Añadir `defer` a la etiqueta script

4. **Acepta los cambios**, reinicia el servidor y verifica que todo sigue funcionando.

   **🎯 Objetivo: Copilot corrige todas las malas prácticas porque el skill proporciona orientación experta antes de modificar el código. ✅**

<details>
<summary>¿El skill no se aplica? 🤷</summary>

- Asegúrate de que el archivo está exactamente en `.github/skills/web-enhancer/SKILL.md`.
- La `description` en el frontmatter debe mencionar palabras clave como "JavaScript", "web", "HTML" para que Copilot sepa cuándo cargarlo.
- Reinicia VS Code si el skill se acaba de crear.

</details>

---

## Paso 7: Skills que Usan Archivos de Prompt — ¡Tu Turno! 🏆

Has visto cómo un skill mejora la calidad del código. Ahora descubramos otra función potente: **los skills pueden referenciar otros archivos** — incluyendo los archivos de prompt que ya creaste.

Esto significa que puedes construir un skill que combine conocimiento experto con un flujo de trabajo automatizado. Piensa en ello como darle a Copilot tanto el **"qué hacer"** (el prompt) como el **"cómo hacerlo bien"** (las reglas del skill).

### 📖 Teoría: Los Skills Pueden Referenciar Archivos

Dentro de un archivo `SKILL.md`, puedes enlazar a otros archivos de tu workspace usando enlaces markdown regulares — igual que los archivos de prompt. Cuando Copilot carga el skill, también lee los archivos enlazados para contexto adicional.

Esto es potente porque te permite **reutilizar** los archivos de prompt que ya creaste. Por ejemplo, un skill puede decir: "Cuando crees actividades, sigue el flujo de trabajo del archivo de prompt new-activity, pero también aplica estas reglas extra."

### Tu Tarea

Crea un nuevo skill que se especialice en crear actividades. En este ejercicio deberás:

- Referenciar el archivo de prompt `/new-activity` que creaste en el Paso 4 (para que Copilot conozca el flujo de trabajo)
- Sobreescribir la ubicación para que sea **siempre** `Mallorca, Spain`
- Sobreescribir la categoría para que sea **siempre** `WaterSport`
- Siempre preguntar al usuario por el **precio**, **nombre** y **duración** (no asumir)
- Dejar que Copilot complete el resto basándose en el archivo de prompt

### Cómo hacerlo

1. Crea el archivo del skill:

   ```text
   .github/skills/activity-creation/SKILL.md
   ```

2. Añade el siguiente contenido:

   ```markdown
   ---
   name: ##
   description: '##. Use when ##'
   ---

   # Activities Skill

   When creating new activities, follow the workflow in
   [enter-prompt-file-name](enter-path-to-prompt-file) but apply
   these additional rules:

   ## Location

   - 
   
   ## Category

   -   

   ## Required Information

   - 
   - 
   -  
   - If any of these fields are missing from the user's request, do NOT proceed. Instead, ask the user to provide the missing values before creating anything.
   - 
   ```

3. Guarda el archivo.

   > 🪧 **Nota:** ¿Ves cómo el skill enlaza a `new-activity.prompt.md`? Esto le dice a Copilot que lea el flujo de trabajo del archivo de prompt (crear carpeta, crear README, actualizar config.json) mientras aplica también las reglas específicas de la actividad. No tienes que repetir el flujo de trabajo completo — solo referéncialo y añade tus sobreescrituras.

### Actividad: Prueba el skill de creación de actividades 🏝️

1. Abre **Copilot Chat** en modo **Agent**.

2. Pide a Copilot que cree una nueva actividad:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a new scuba-diving activity
   > ```

3. Observa cómo se comporta Copilot:
   - **No debería preguntar** por la ubicación (el skill dice que siempre es Mallorca, Spain)
   - **No debería preguntar** por la categoría (el skill dice que siempre es WaterSport)
   - Debería seguir el mismo flujo de trabajo del archivo de prompt (crear carpeta, README, actualizar config.json)

4. **Reinicia el servidor** y verifica que la nueva actividad aparece en el sitio web con todo como especificaste.

   **🎯 Objetivo: El skill combina el flujo de trabajo del prompt new-activity con reglas específicas — demostrando que los skills pueden referenciar y extender archivos existentes. ✅**

<details>
<summary>¿El skill no funciona? 🤷</summary>

- Asegúrate de que la `description` menciona "creating" y "activity" — Copilot usa la descripción para decidir cuándo cargarlo.
- Comprueba que la ruta relativa al archivo de prompt es correcta: `../../prompts/new-activity.prompt.md`.
- Reinicia VS Code si el skill se acaba de crear.

</details>

---

## ¡Felicidades! 🎉

¡Has completado el **Lab 02 — Instrucciones Personalizadas de Copilot**! Aquí tienes un resumen de lo que aprendiste:

| Paso | Lo que Hiciste |
| ---- | -------------- |
| **Paso 1** | Configuraste instrucciones personalizadas en los tres niveles: organización (revisión), repositorio (práctico) y personal (práctico) |
| **Paso 2** | Creaste instrucciones específicas por archivo y las usaste para corregir la actividad de kayaking |
| **Paso 3** | Corregiste independientemente la actividad de sightseeing usando el mismo enfoque |
| **Paso 4** | Creaste un archivo de prompt reutilizable para automatizar la creación de nuevas actividades |
| **Paso 5** | Diseñaste tu propio archivo de prompt para vuelos, alojamientos o paquetes |
| **Paso 6** | Construiste un skill web-enhancer para mejorar la calidad del JavaScript y la seguridad |
| **Paso 7** | Creaste un skill que referencia archivos de prompt para especializar la creación de actividades |

### Conclusiones Clave

- Las **instrucciones personalizadas** eliminan orientación repetitiva — configúralas una vez, benefíciate siempre.
- **Tres niveles** te permiten adaptar Copilot en el ámbito de organización, repositorio y personal.
- **Orden de prioridad**: Personal > Repositorio > Organización — las preferencias personales siempre ganan.
- Las **instrucciones específicas por archivo** (`*.instructions.md`) se aplican solo a los archivos que las necesitan usando patrones glob.
- Los **archivos de prompt** (`*.prompt.md`) empaquetan flujos de trabajo de varios pasos en comandos slash reutilizables.
- Los **Skills** (`SKILL.md`) le dan a Copilot conocimiento experto en dominios para que escriba código de mayor calidad y más especializado.
- ¡El **Modo Agente** puede crear los archivos de instrucciones, archivos de prompt y skills por ti — deja que Copilot haga el trabajo pesado!

### ¿Qué Sigue?

- Explora la [Customization Library](https://docs.github.com/en/copilot/tutorials/customization-library) para más ejemplos de instrucciones
- Prueba a crear instrucciones para tus propios proyectos
- Experimenta combinando múltiples archivos de instrucciones para diferentes áreas de tu código
- Comparte tus archivos de prompt con tu equipo para estandarizar flujos de trabajo comunes
