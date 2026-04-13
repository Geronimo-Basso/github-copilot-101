# Lab 01 — Copilot Chat

Explora **GitHub Copilot Chat** — tu programador en pareja con IA que vive dentro de tu IDE. Pídele que explique código, corrija errores, escriba tests y más.

## Lo que aprenderás

El objetivo de hoy será aprender sobre GitHub Copilot Chat, la interfaz de usuario con IA que ofrece GitHub, y cómo sacar el máximo provecho de los tres modos diferentes que proporciona:

- **Modo Ask** — Incorporarte a un proyecto, explorar código y obtener respuestas
- **Modo Agent** — Deja que Copilot corrija errores, agregue funcionalidades e itere sobre el código de forma autónoma
- **Plan Agent** — Diseña un plan de implementación antes de escribir código

Al final de este laboratorio habrás utilizado los tres modos para corregir un bug, agregar nuevas funcionalidades y escribir tests para una aplicación web FastAPI.

## Paso 1: Hola Copilot

¡Bienvenido/a al ejercicio **"Primeros pasos con GitHub Copilot"**!

En este ejercicio, utilizarás diferentes funcionalidades de GitHub Copilot para trabajar en un sitio web que permite a los estudiantes de Mergington High School inscribirse en actividades extracurriculares. 🎻 ⚽️ ♟️

### 📖 Teoría: Conociendo GitHub Copilot

GitHub Copilot es un asistente de código con IA que te ayuda a escribir código más rápido y con menos esfuerzo, permitiéndote enfocar más energía en la resolución de problemas y la colaboración.

Se ha demostrado que GitHub Copilot aumenta la productividad de los desarrolladores y acelera el ritmo del desarrollo de software. Para más información, consulta [Research: quantifying GitHub Copilot's impact on developer productivity and happiness en el blog de GitHub.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

Mientras trabajas en tu IDE, interactuarás con GitHub Copilot principalmente de las siguientes maneras:

| Modo de interacción       | 📝 Descripción                                                                                                                           | 🎯 Ideal para                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **⚡ Sugerencias inline**  | Sugerencias de código con IA que aparecen mientras escribes, ofreciendo completados contextuales desde líneas individuales hasta funciones completas. | Completar la línea actual, a veces un bloque de código completamente nuevo                                          |
| **💭 Chat Inline**         | Chat interactivo limitado a tu archivo o selección actual. Haz preguntas sobre bloques de código específicos.                             | Explicaciones de código, depuración de funciones específicas, mejoras puntuales                                     |
| **💬 Modo Ask**            | Optimizado para responder preguntas sobre tu codebase, programación y conceptos tecnológicos generales.                                   | Entender cómo funciona el código, lluvia de ideas, hacer preguntas                                                  |
| **🤖 Modo Agent**          | Modo predeterminado recomendado para la mayoría de tareas de código: ediciones autónomas, uso de herramientas y seguimiento hasta completar la tarea. | Tareas de código diarias, desde correcciones puntuales hasta implementaciones en múltiples archivos                 |
| **🧭 Plan Agent**          | Optimizado para redactar un plan y hacer preguntas aclaratorias antes de realizar cambios en el código.                                   | Cuando quieres un plan revisado primero, para luego pasar a la implementación                                       |

Mientras trabajas, encontrarás que GitHub Copilot puede ayudar en varios lugares del sitio web `github.com` y en tus entornos de desarrollo favoritos como VS Code, JetBrains y Xcode.

> [!TIP]
> Puedes aprender más sobre las funcionalidades actuales y futuras en la documentación de [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features).

### Actividad: Obtén una introducción al proyecto con Copilot Chat

Iniciemos nuestro entorno de desarrollo, usemos Copilot para aprender un poco sobre el proyecto y luego hagamos una prueba.

1. Comienza clonando este repositorio en tu máquina local.

2. Si estás en Visual Studio Code, en la barra lateral izquierda, haz clic en la pestaña de extensiones y verifica que las extensiones `GitHub Copilot` y `Python` estén instaladas y habilitadas.

1. En la parte superior de VS Code, localiza y haz clic en el **ícono de Toggle Chat** para abrir un panel lateral de Copilot Chat.

   > 🪧 **Nota:** Si es tu primera vez usando GitHub Copilot, necesitarás aceptar los términos de uso para continuar.

1. Asegúrate de estar en **Modo Ask** para nuestra primera interacción.

1. Ingresa el siguiente prompt para pedirle a Copilot que te presente el proyecto.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Por favor, explica brevemente la estructura de este proyecto.
   > ¿Qué debo hacer para ejecutarlo?
   > ```

   Ahora agrega la carpeta src como contexto y repite la misma pregunta.

   También puedes usar #codespace, que permitirá a Copilot ver todo el contenido del repositorio y su código fuente.

1. Ahora que sabemos un poco más sobre el proyecto, ¡intentemos ejecutarlo!

### Actividad: Usa Copilot para recordar un comando de terminal 🙋

¡Buen trabajo! Ahora que estamos familiarizados con la app y sabemos que funciona, pidamos ayuda a Copilot para crear una rama y así poder hacer algunas personalizaciones.

1. En el panel inferior de VS Code, selecciona la pestaña **Terminal** y en el lado derecho haz clic en el signo más `+` para crear una nueva ventana de terminal.

   > 🪧 **Nota:** Esto evitará detener la sesión de depuración existente que está alojando nuestro servicio web.

1. Dentro de la nueva ventana de terminal, usa el atajo de teclado `Ctrl + I` (Windows) o `Cmd + I` (Mac) para abrir el **Chat Inline de Terminal de Copilot**.

1. Pidamos a Copilot que nos ayude a recordar un comando que hemos olvidado: crear una rama y publicarla.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, ¿cómo puedo crear y publicar una nueva rama de Git llamada "accelerate-with-copilot"?
   > ```

   > 💡 **Tip:** Si Copilot no te da exactamente lo que quieres, siempre puedes seguir explicando lo que necesitas. Copilot recordará el historial de la conversación para las respuestas siguientes.

1. Presiona el botón `Run` para que Copilot inserte el comando de terminal por nosotros. ¡No es necesario copiar y pegar!

1. Después de un momento, mira en la barra de estado inferior de VS Code, a la izquierda, para ver la rama activa. Ahora debería decir `accelerate-with-copilot`. Si es así, ¡has terminado este paso!

## Paso 2: Trabajando con Copilot

En el paso anterior, GitHub Copilot nos ayudó a incorporarnos al proyecto. Eso solo ya es un gran ahorro de tiempo, ¡pero ahora pongámonos a trabajar!

:bug: **HAY UN BUG EN EL SITIO WEB** :bug:

Hemos descubierto que algo anda mal en el flujo de inscripción.
¡Los estudiantes actualmente pueden registrarse en la misma actividad **más de una vez**! Veamos hasta dónde puede llevarnos Copilot para descubrir la causa y diseñar una solución limpia.

Antes de empezar, un breve repaso de cómo funciona Copilot. 🧑‍🚀

### 📖 Teoría: Cómo funciona Copilot

En resumen, puedes pensar en Copilot como un compañero de trabajo muy especializado. Para ser efectivo con él, necesitas proporcionarle contexto y dirección clara (prompts). Además, diferentes personas son mejores en diferentes cosas debido a sus experiencias únicas (modelos).

- **¿Cómo proporcionamos contexto?:** En nuestro entorno de desarrollo, Copilot considerará automáticamente el código cercano y las pestañas abiertas. Si estás usando el chat, también puedes referirte explícitamente a archivos.

- **¿Qué modelo debemos elegir?:** Para nuestro ejercicio, no debería importar mucho. ¡Experimentar con diferentes modelos es parte de la diversión! ¡Esa es otra lección! 🤖

- **¿Cómo hago prompts?:** Ser explícito y claro ayuda a Copilot a hacer el mejor trabajo. Pero a diferencia de algunos sistemas tradicionales, siempre puedes aclarar tu dirección con prompts de seguimiento.

### Actividad: Usa Copilot para corregir nuestro bug de registro :bug:

1. Pidamos a Copilot que sugiera de dónde podría venir nuestro bug. Abre el panel de **Copilot Chat** en **modo Ask** y pregunta lo siguiente.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Los estudiantes pueden registrarse dos veces en una actividad.
   > ¿De dónde podría venir este bug?
   > ```

1. Ahora que sabemos que el problema está en el archivo `backend/app.py` y en el método `signup_for_activity`, sigamos la recomendación de Copilot y vayamos a corregirlo (semi-manualmente). Comenzaremos con un comentario y dejaremos que Copilot complete la corrección.
   1. Abre el archivo `backend/app.py`.

      > 💡 **Tip:** Si Copilot mencionó `backend/app.py` en el chat, puedes hacer clic en el archivo directamente en la vista de chat para abrirlo.

   1. Cerca del final del archivo, encuentra la función `signup_for_activity`.

   1. Encuentra la línea de comentario que describe agregar un estudiante. Arriba de esta es donde lógicamente debería ir nuestra verificación de registro.

   1. Ingresa el siguiente comentario y presiona enter para ir a la siguiente línea. Después de un momento, aparecerá texto sombreado temporal con una sugerencia de Copilot. ¡Genial! :tada:

      Comentario:

      ```python
      # Validate student is not already signed up
      ```

   1. Presiona `Tab` para aceptar la sugerencia de Copilot y convertir el texto sombreado en código.

   <details>
   <summary>Ejemplo de resultados</summary><br/>

   Copilot crece cada día y puede que no siempre produzca los mismos resultados. Si no estás satisfecho con las sugerencias, aquí tienes un ejemplo de un resultado válido que produjimos durante la creación de este ejercicio. Puedes usarlo para continuar.

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### Actividad: Deja que Copilot genere datos de ejemplo 📋

En nuevos desarrollos de proyectos, a menudo es útil tener datos falsos de aspecto realista para pruebas. Copilot es excelente en esta tarea, así que agreguemos más actividades de ejemplo e introduzcamos otra forma de interactuar con Copilot usando **Chat Inline**.

**Chat Inline** y el panel de **Copilot Chat** son similares, pero difieren en alcance: Copilot Chat maneja preguntas más amplias, de múltiples archivos o exploratorias; Chat Inline es más rápido cuando quieres ayuda puntual en la línea o bloque exacto que tienes frente a ti.

1. Cerca de la parte superior del archivo `backend/app.py` (alrededor de la línea 23), encuentra la variable `activities`, donde están configuradas nuestras actividades extracurriculares de ejemplo.

1. Selecciona todo el diccionario `activities` haciendo clic y arrastrando el ratón desde la parte superior hasta la inferior del diccionario. Esto ayudará a proporcionar contexto a Copilot para nuestro siguiente prompt.

1. Abre el Chat Inline de Copilot usando el comando de teclado `Ctrl + I` (Windows) o `Cmd + I` (Mac).

   > 💡 **Tip:** Otra forma de abrir el Chat Inline de Copilot es: `clic derecho` en cualquiera de las líneas seleccionadas -> `Open Inline Chat`.

1. Ingresa el siguiente texto de prompt y presiona enter o el botón **Send** a la derecha.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Agrega 2 actividades deportivas más, 2 actividades artísticas
   > más y 2 actividades intelectuales más.
   > ```

1. Después de un momento, Copilot comenzará directamente a hacer cambios en el código. Los cambios tendrán un estilo diferente para que las adiciones y eliminaciones sean fáciles de identificar. Tómate un momento para inspeccionar y verificar los cambios, y luego presiona el botón **Keep**.

   <details>
   <summary>Ejemplo de resultados</summary><br/>

   Copilot crece cada día y puede que no siempre produzca los mismos resultados. Si no estás satisfecho con las sugerencias, aquí tienes un ejemplo de resultado que produjimos durante la creación de este ejercicio. Puedes usarlo para continuar si tienes dificultades.

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. Ahora puedes ir a tu sitio web y verificar que las nuevas actividades sean visibles.

### Actividad: Usa Copilot para describir nuestro trabajo 💬 (Opcional)

¡Buen trabajo corrigiendo ese bug y expandiendo las actividades de ejemplo! Ahora hagamos commit de nuestro trabajo y subámoslo a GitHub, ¡nuevamente con la ayuda de Copilot!

1. En la barra lateral izquierda, selecciona la pestaña `Source Control`.

   > 💡 **Tip:** Abrir un archivo desde el área de control de código fuente mostrará las diferencias con el original en lugar de simplemente abrirlo.

1. Encuentra el archivo `app.py` y presiona el signo `+` para reunir tus cambios en el área de staging.

1. Encima de la lista de cambios en staging, encuentra el cuadro de texto **Message**, pero **no escribas nada** por ahora.
   - Normalmente, escribirías una breve descripción de los cambios aquí, ¡pero ahora tenemos a Copilot para ayudarnos!

1. A la derecha del cuadro de texto **Message**, encuentra y haz clic en el botón **Generate Commit Message** (ícono de destellos).

1. Presiona el botón **Commit** y el botón **Sync Changes** para subir tus cambios a GitHub.

## Paso 3: Activa el Hiperdrive - Copilot Agent Mode 🚀

### 📖 Teoría: ¿Qué es Copilot Agent Mode?

Copilot [Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) es la siguiente evolución en codificación asistida por IA. Actuando como un programador en pareja autónomo, ejecuta tareas de código en múltiples pasos bajo tu comando.

Copilot Agent Mode responde a errores de compilación y lint, monitorea la salida del terminal y de los tests, y se autocorrige en un bucle hasta que la tarea se completa.

#### Agent Mode (en resumen)

| Aspecto | 👩‍🚀 Agent Mode |
| --- | --- |
| Autonomía y planificación | Descompone solicitudes de alto nivel en trabajo de múltiples pasos e itera hasta que la tarea se completa. |
| Recopilación de contexto | Usa tu contexto actual y puede descubrir archivos relevantes adicionales cuando sea necesario. |
| Uso de herramientas | Selecciona e invoca herramientas automáticamente; también puedes dirigir herramientas con menciones como `#codebase`. |
| Aprobación y puertas de seguridad | Las acciones sensibles pueden requerir aprobación antes de ejecutarse, ayudándote a mantener el control. |

#### 🧰 Herramientas de Agent Mode

Agent Mode usa herramientas para realizar tareas especializadas mientras procesa una solicitud del usuario. Ejemplos de estas tareas son:

- Encontrar archivos relevantes para completar tu prompt
- Obtener contenidos de una página web
- Ejecutar tests o comandos de terminal

¡Ahora, probemos **Agent Mode**! 👩‍🚀

### Actividad: ¡Usa Copilot para agregar una nueva funcionalidad! :rocket:

Nuestro sitio web lista actividades, pero mantiene la lista de invitados en secreto 🤫

¡Usemos Copilot para cambiar el sitio web y mostrar los estudiantes inscritos en cada actividad!

1. En la parte inferior de la ventana de Copilot Chat, usa el menú desplegable para cambiar al modo **Agent**.

1. Abre los archivos relacionados con nuestra página web y arrastra cada ventana de editor (o archivo) al panel de chat, indicándole a Copilot que los use como contexto.

   - `frontend/app.js`
   - `frontend/index.html`
   - `frontend/styles.css`

   > 🪧 **Nota:** Agregar archivos como contexto es opcional. Si omites esto, Copilot Agent Mode aún puede usar herramientas como `#codebase` para buscar archivos relevantes a partir de tu prompt. Agregar archivos específicos ayuda a orientar a Copilot en la dirección correcta, lo cual es especialmente útil en bases de código grandes.

   > 💡 **Tip:** También puedes usar el botón **Add Context...** para proporcionar otras fuentes de contexto, como un issue de GitHub o los resultados de una ventana de terminal.

1. Pídele a Copilot que actualice nuestro proyecto para mostrar los participantes actuales de las actividades. Espera un momento para que las sugerencias de edición lleguen y se apliquen.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, ¿puedes editar las tarjetas de actividades para agregar una sección de participantes?
   > Mostrará qué participantes ya están inscritos en esa actividad como una lista con viñetas.
   > ¡Recuerda hacerlo bonito!
   > ```

   Después de que Copilot termine su trabajo, tú tienes el control de qué cambios se quedan.

   Usando los botones **Keep** que se muestran a continuación, puedes aceptar/descartar todos los cambios o revisar y decidir cambio por cambio. Esto se puede hacer desde la vista del panel de chat o mientras inspeccionas cada archivo editado.

1. Antes de simplemente aceptar los cambios, revisa nuestro sitio web nuevamente y verifica que todo esté actualizado como se esperaba.

   Aquí tienes un ejemplo de una tarjeta de actividad actualizada. Puede que necesites reiniciar la app o refrescar la página.

   > 🪧 **Nota:** Tu tarjeta de actividad puede verse diferente. Copilot no siempre producirá los mismos resultados.

1. Ahora que hemos confirmado que nuestros cambios están bien, usa el panel para recorrer cada edición sugerida y presiona **Keep** para aplicar el cambio.

   > 💡 **Tip:** Puedes aceptar los cambios directamente, modificarlos o proporcionar instrucciones adicionales para refinarlos usando la interfaz de chat.

### Actividad: Usa Agent Mode para agregar botones funcionales de "cancelar inscripción"

Experimentemos con algunas solicitudes más abiertas que agregarán más funcionalidad a nuestra aplicación web.

Si no obtienes los resultados deseados, puedes probar otros modelos o proporcionar retroalimentación de seguimiento para refinar los resultados.

1. Asegúrate de que tu Copilot todavía esté en modo **Agent**.

1. Haz clic en el ícono de **Tools** y explora todas las herramientas actualmente disponibles para Copilot Agent Mode.

1. ¡Hora de nuestra prueba! Pidamos a Copilot que agregue funcionalidad para eliminar participantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Por favor, agrega un ícono de eliminar junto a cada participante y oculta las viñetas.
   > Al hacer clic, cancelará la inscripción de ese participante de la actividad.
   > ```

   La herramienta `#codebase` es utilizada por Copilot para encontrar archivos relevantes y fragmentos de código pertinentes a la tarea.

   > 🪧 **Nota:** En este laboratorio incluimos explícitamente la herramienta `#codebase` para obtener los resultados más reproducibles.
   > Siéntete libre de probar el prompt **sin** `#codebase` y observa si Agent Mode decide recopilar contexto más amplio del proyecto por su cuenta.

1. Cuando Copilot termine, inspecciona los cambios en el código y los resultados en el sitio web. Si te gustan los resultados, presiona el botón **Keep**. Si no, intenta proporcionar retroalimentación a Copilot para refinar los resultados.

   > 🪧 **Nota:** Si no ves actualizaciones en el sitio web, puede que necesites reiniciar el código.

1. Pídele a Copilot que corrija un bug de registro.

   > 💡 **Tip:** Te recomendamos probar el flujo de registro tú mismo para que puedas ver claramente el comportamiento antes/después de los cambios.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > He notado que parece haber un bug.
   > Cuando se registra un participante, hay que refrescar la página para ver el cambio en la actividad.
   > ```

1. Cuando Copilot termine, inspecciona los resultados y valida el flujo de registro en el sitio web.

   Si te gustan los resultados, presiona el botón **Keep**. Si no, intenta proporcionar retroalimentación a Copilot.

## Paso 4: Planifica tu implementación con el Planning Agent 🧭

En el paso anterior, Agent Mode nos ayudó a avanzar rápido y entregar nueva funcionalidad. 🚀

Ahora vamos a ir más despacio por una ronda y trabajar como arquitectos: definir una estrategia de testing sólida primero, para luego pasarla a implementación. Esto nos da mayor claridad, menos sorpresas y resultados más limpios. 🧪

### 📖 Teoría: ¿Qué es Copilot Plan Agent?

Copilot [Plan Agent](https://code.visualstudio.com/docs/copilot/agents/planning) te ayuda a diseñar una solución antes de que se cambie cualquier código.

En lugar de saltar directamente a las ediciones, investiga tu solicitud, hace preguntas aclaratorias y redacta un plan de implementación que puedes refinar.

#### Plan Agent (en resumen)

| Aspecto | 🧭 Plan Agent |
| --- | --- |
| Propósito | Crea un plan de implementación estructurado antes de que comience la codificación. |
| Recopilación de contexto | Usa investigación de solo lectura para entender requisitos y restricciones. |
| Estilo de colaboración | Hace preguntas aclaratorias, luego actualiza el plan usando tus respuestas. |
| Iteración | Soporta múltiples pases de refinamiento antes de la implementación. |
| Seguridad | No edita archivos hasta que apruebes el plan y lo pases a **Agent Mode**. |
| Traspaso | El botón **Start implementation** pasa el plan aprobado a **Agent Mode** para la codificación. |

> [!TIP]
> Puedes comenzar con una solicitud de alto nivel y luego agregar restricciones y detalles en prompts de seguimiento.

### ⌨️ Actividad: Planifica e implementa tests de backend

Tu backend aún tiene cero cobertura de tests. Usa **Plan Agent** para crear un plan, responder preguntas y luego lanzar la implementación.

1. Abre el panel de **Copilot Chat** y cambia a **Plan Agent**.

1. Comencemos con un prompt amplio y Copilot nos ayudará a completar los detalles:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Quiero agregar tests de backend FastAPI en un directorio de tests separado.
   > ```

1. Espera a que Copilot genere su primer plan. Si te hace alguna pregunta, respóndela lo mejor que puedas.

   > 🪧 **Nota:** No te preocupes por hacerlo perfecto, siempre puedes refinar el plan después.

1. Puedes refinar el plan y proporcionar detalles adicionales en prompts de seguimiento.

   Aquí hay algunos ejemplos:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Usemos el patrón de testing AAA (Arrange-Act-Assert) para estructurar nuestros tests
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Asegúrate de que usemos `pytest` y agrégalo al archivo `requirements.txt`
   > ```

1. Revisa el plan propuesto y cuando estés satisfecho, haz clic en **Start implementation** para pasarlo a **Agent Mode**.

   Nota que al hacer clic en el botón se cambió de **Plan** a **Agent Mode**. A partir de este punto, Copilot puede editar tu código, igual que antes.

1. Observa cómo Copilot implementa el plan que acabas de crear. Puede pedirte permisos para ejecutar ciertas herramientas (por ejemplo, ejecutar comandos o crear entornos virtuales). Aprueba estos permisos para que pueda continuar trabajando.

1. Revisa los cambios y asegúrate de que los tests se ejecuten exitosamente. Si es necesario, continúa guiando hasta que la implementación esté completa.

   **🎯 Objetivo: Lograr que todos los tests pasen (verde) antes de avanzar. ✅**

   > 🪧 **Nota:** Agent Mode puede completar esto en un solo pase, o puede necesitar prompts de seguimiento de tu parte.

## Paso 5: Vuela Solo — Ponlo Todo Junto 🧑‍✈️

En los pasos anteriores, recorrimos cada modo de Copilot con prompts guiados. ¡Ahora es hora de quitar las ruedas de entrenamiento! En este paso implementarás nuevas funcionalidades y mejorarás el código usando GitHub Copilot como tu compañero — pero **no te daremos los prompts exactos**. Piensa en lo que has aprendido hasta ahora y crea tus propios prompts para hacer el trabajo.

> 💡 **Tip:** Recuerda que la clave para obtener grandes resultados con Copilot es contexto claro y dirección explícita. No dudes en iterar — si el primer resultado no es perfecto, refina tu prompt o proporciona instrucciones de seguimiento.

### 📖 Teoría: Crafting de Prompts — Pensando Como un Copilot Whisperer

Antes de comenzar, aquí hay algunos principios a tener en cuenta al escribir tus propios prompts:

| Principio | 📝 Descripción | 🎯 Ejemplo |
| --- | --- | --- |
| **Sé específico** | Dile a Copilot exactamente lo que quieres, dónde y cómo. | _"Lee las actividades de `data/activities.json` en lugar del diccionario hardcodeado en `app.py`"_ |
| **Proporciona contexto** | Adjunta archivos relevantes o usa `#codebase` para que Copilot conozca el panorama completo. | Arrastra `app.py` y `activities.json` al panel de chat. |
| **Divídelo** | Las tareas grandes funcionan mejor como una serie de solicitudes más pequeñas y enfocadas. | Primero mover los datos, luego agregar nuevas entradas, luego verificar. |
| **Itera y refina** | Copilot recuerda la conversación — haz seguimiento si el resultado necesita ajustes. | _"Eso se ve bien, pero también agrega manejo de errores para un archivo JSON faltante."_ |
| **Elige el modo correcto** | Usa **Ask** para explorar, **Agent** para implementar y **Plan** para diseñar la arquitectura. | Usa el Modo Ask para aprender sobre Swagger, luego Agent Mode para agregar anotaciones. |

---

### Actividad: Reemplaza los datos hardcodeados con un archivo JSON 📂 (Paso 5.1)

Actualmente, todos los datos de actividades viven como un diccionario Python hardcodeado dentro de `backend/app.py`. En una aplicación real, estos datos vendrían de una base de datos, un archivo de configuración o una API externa. Para nuestro proyecto, ya tenemos un archivo JSON esperando en `backend/data/activities.json` — ¡solo necesitamos conectarlo!

#### Parte A: Mover la fuente de datos a JSON

1. Comienza explorando el estado actual de las cosas. Abre `backend/app.py` y `backend/data/activities.json` lado a lado para que puedas ver ambos archivos.

   > 💡 **Tip:** Puedes usar **Modo Ask** primero para entender cómo están estructurados los datos hardcodeados actualmente y qué cambios serían necesarios para cargarlos desde un archivo.

1. Abre el panel de **Copilot Chat** y cambia al modo **Agent**.

1. Agrega tanto `backend/app.py` como `backend/data/activities.json` como contexto arrastrándolos al panel de chat.

1. Ahora, crea un prompt que le pida a Copilot:
   - Cargar los datos de actividades desde el archivo `data/activities.json` en lugar del diccionario hardcodeado.
   - Asegurarse de que el archivo JSON se lea al iniciar la aplicación.
   - Eliminar o reemplazar el viejo diccionario `activities` hardcodeado.

   > 🪧 **Nota:** Intencionalmente no proporcionamos el prompt exacto aquí. Piensa en qué información necesita Copilot para realizar esta tarea. ¡Recuerda los principios de la sección de teoría anterior!

1. Revisa los cambios que Copilot propone. Presta atención a:
   - ¿Es correcta la ruta del archivo y relativa a donde se ejecuta la app?
   - ¿Maneja el caso en que el archivo JSON podría no existir?
   - ¿Es la estructura JSON compatible con cómo se usaba `activities` antes?

1. Si todo se ve bien, presiona **Keep**. Si no, proporciona instrucciones de seguimiento para refinar el resultado.

1. **¡Pruébalo!** Reinicia tu servidor backend y verifica que el sitio web todavía cargue todas las actividades correctamente.

   **🎯 Objetivo: La app debería funcionar exactamente como antes, pero ahora leyendo datos de `activities.json`. ✅**

   > 🪧 **Nota:** Si encuentras errores de importación o de archivo no encontrado, ¡pídele a Copilot que te ayude a depurar! Esta es una gran oportunidad para practicar proporcionando contexto de errores en tus prompts.

#### Parte B: Expandir el catálogo de actividades

Ahora que nuestros datos viven en un archivo JSON, es mucho más fácil gestionarlos. Hagamos que el catálogo extracurricular de nuestra escuela se vea más impresionante agregando más actividades.

1. Abre `backend/data/activities.json` en el editor.

1. Piensa en un prompt que le pida a Copilot agregar más actividades al archivo JSON. Considera:
   - ¿Cuántas actividades nuevas quieres?
   - ¿Qué categorías deberían cubrir? (deportes, artes, académicas, tecnología, etc.)
   - ¿Deberían tener horarios, descripciones y límites de participantes realistas?

1. Usa ya sea **Chat Inline** (`Cmd + I` / `Ctrl + I`) con el archivo seleccionado, o **Agent Mode** en el panel de chat — lo que prefieras.

1. Después de que Copilot genere las nuevas actividades, revísalas para verificar consistencia:
   - ¿Siguen la misma estructura JSON que las entradas existentes?
   - ¿Son los horarios realistas y no se superponen?
   - ¿Tienen sentido los valores de `max_participants` para cada tipo de actividad?

1. Reinicia el backend y refresca el frontend para verificar que las nuevas actividades aparezcan en el sitio web.

   **🎯 Objetivo: Tu página de actividades ahora debería mostrar un catálogo rico y diverso de opciones extracurriculares. ✅**

   > 💡 **Tip:** Si el diseño del frontend se ve apretado o roto con más actividades, puedes pedirle a Copilot que ajuste el grid CSS o el diseño de tarjetas para acomodar mejor la lista más grande.

---

### Actividad: Agrega una funcionalidad de retiro 🚪 (Paso 5.2)

Hasta ahora, nuestra app solo permite a los estudiantes inscribirse en actividades. Pero, ¿qué pasa cuando un estudiante necesita abandonar una actividad por un conflicto de horarios o una emergencia de último momento? Sería genial permitir a los estudiantes retirarse para que otro estudiante pueda tomar su lugar.

Esta es una **funcionalidad full-stack** — necesitarás cambios tanto en el backend como en el frontend. Esto es lo que se necesita:

#### 📖 Entendiendo los requisitos

Antes de escribir código, desglosemos lo que necesita esta funcionalidad:

| Componente | Lo que se necesita |
| --- | --- |
| **Backend** | Un nuevo endpoint de API que acepte un nombre de actividad y un email de estudiante, y luego elimine a ese estudiante de la lista de participantes de la actividad. |
| **Frontend (JS)** | Una función que llame al nuevo endpoint del backend cuando un estudiante haga clic en un botón de "retirarse" o "cancelar inscripción". |
| **Frontend (HTML/CSS)** | Un elemento de UI (botón o ícono) junto a cada participante o en la tarjeta de actividad que active la acción de retiro. |

> 💡 **Tip:** ¡Este es un gran candidato para **Plan Agent**! Puedes primero pedirle a Copilot que cree un plan de implementación, revisarlo y luego pasarlo a Agent Mode para la codificación real.

#### Parte A: Planifica la implementación

1. Abre el panel de **Copilot Chat** y cambia a **Plan Agent**.

1. Crea un prompt describiendo la funcionalidad de retiro. Asegúrate de mencionar:
   - La necesidad de un nuevo endpoint de backend (piensa en qué método HTTP tiene sentido — ¿`DELETE`? ¿`POST`?).
   - El frontend necesita una forma de activar el retiro.
   - La UI debería actualizarse inmediatamente sin requerir refrescar la página.

1. Espera a que Copilot genere un plan. Revísalo cuidadosamente:
   - ¿Cubre el plan tanto los cambios de backend como de frontend?
   - ¿Incluye manejo de errores adecuado (por ejemplo, ¿qué pasa si el estudiante no está registrado)?
   - ¿Menciona actualizar la UI después de un retiro exitoso?

1. Si tienes retroalimentación, refina el plan con prompts de seguimiento. Por ejemplo:
   - _"Usa un endpoint DELETE para el retiro"_
   - _"Muestra una confirmación antes de retirarse"_
   - _"Asegúrate de que la lista de participantes se actualice en tiempo real"_

#### Parte B: Implementa la funcionalidad

1. Una vez que estés satisfecho con el plan, haz clic en **Start implementation** para pasarlo a **Agent Mode**.

1. Observa cómo Copilot hace cambios en múltiples archivos. Debería modificar al menos:
   - `backend/app.py` — nuevo endpoint
   - `frontend/app.js` — nueva función JavaScript
   - `frontend/index.html` y/o `frontend/styles.css` — actualizaciones de UI

1. Cuando Copilot termine, revisa todos los cambios propuestos archivo por archivo.

   > 🪧 **Nota:** Presta especial atención al endpoint del backend. Asegúrate de que valide que:
   > - La actividad existe
   > - El estudiante está realmente registrado antes de intentar eliminarlo
   > - Se devuelvan códigos de estado HTTP apropiados para cada caso de error

1. **Prueba el flujo completo:**
   - Inscribe a un estudiante en una actividad
   - Verifica que aparezca en la lista de participantes
   - Retira a ese estudiante usando la nueva funcionalidad
   - Verifica que sea eliminado de la lista
   - Intenta retirar a un estudiante que no está registrado y verifica el manejo de errores

   **🎯 Objetivo: Los estudiantes pueden inscribirse y retirarse de actividades, con la UI actualizándose en tiempo real. ✅**

   <details>
   <summary>¿Atascado? Aquí hay algunas pistas</summary><br/>

   - Para el backend, un endpoint `DELETE /activities/{activity_name}/withdraw?email=...` es un enfoque limpio.
   - En el frontend, probablemente necesites un event listener en el botón de eliminar de cada participante que llame a `fetch()` con el método `DELETE`.
   - No olvides re-renderizar la tarjeta de actividad después de un retiro exitoso — reutiliza o refactoriza la lógica de renderizado existente.

   </details>

---

### Actividad: Documenta tu API con Swagger 📜 (Paso 5.3)

Hemos hecho mucho trabajo construyendo nuestra API — tenemos endpoints para listar actividades, inscribirse y ahora retirarse. Pero, ¿cómo sabría otro desarrollador cómo usar nuestra API? Ahí es donde entra la **documentación de API**.

#### 📖 Teoría: ¿Qué es Swagger / OpenAPI?

FastAPI viene con soporte integrado para la [especificación OpenAPI](https://swagger.io/specification/) (anteriormente conocida como Swagger). Esto significa que tu API obtiene automáticamente documentación interactiva — ¡sin configuración adicional!

| Funcionalidad | 📝 Descripción |
| --- | --- |
| **Swagger UI** | Una página web interactiva donde puedes ver todos los endpoints y probarlos directamente desde el navegador. Disponible en `/docs`. |
| **ReDoc** | Una vista de documentación alternativa con un diseño limpio y legible. Disponible en `/redoc`. |
| **OpenAPI Schema** | Una especificación JSON legible por máquinas de tu API. Disponible en `/openapi.json`. |

> 🪧 **Nota:** Por defecto, FastAPI genera documentación a partir de las firmas de tus funciones Python y docstrings. ¡Cuanto más detalle agregues a tu código, mejor será la documentación!

#### Parte A: Explora la documentación actual

1. Asegúrate de que tu servidor backend esté ejecutándose.

1. Abre tu navegador y navega a `http://localhost:8000/docs` (ajusta el puerto si es necesario).

1. Tómate un momento para explorar la Swagger UI actual:
   - ¿Qué endpoints están listados?
   - ¿Cuánto detalle muestra cada endpoint?
   - ¿Están los modelos de request/response claramente descritos?

1. También puedes usar **Modo Ask** en Copilot para aprender más sobre Swagger y qué hace una buena documentación de API:

   > 🪧 **Nota:** Este es un gran ejemplo de usar **Modo Ask** para aprender en lugar de codificar. ¡No todo necesita Agent Mode!

   Piensa en preguntas como:
   - _"¿Qué es Swagger y cómo lo usa FastAPI?"_
   - _"¿Cuáles son las mejores prácticas para documentar endpoints de FastAPI?"_
   - _"¿Cómo agrego modelos de request/response, descripciones y ejemplos a mis endpoints?"_

#### Parte B: Mejora la documentación de los endpoints

Ahora mejoremos la documentación de la API agregando metadatos más ricos a nuestros endpoints.

1. Cambia al **Modo Agent** en el panel de Copilot Chat.

1. Agrega `backend/app.py` como contexto.

1. Crea un prompt pidiendo a Copilot que mejore la documentación de Swagger. Piensa en agregar:
   - Campos descriptivos de **summary** y **description** para cada endpoint
   - **Modelos de respuesta** adecuados usando clases Pydantic `BaseModel`
   - **Valores de ejemplo** para los parámetros de request
   - **Descripciones de códigos de estado HTTP** (por ejemplo, 200, 400, 404)
   - **Tags** para agrupar endpoints relacionados (por ejemplo, "Activities", "Registration")

   > 💡 **Tip:** No tienes que hacerlo todo de una vez. Comienza con una mejora (como agregar modelos de respuesta), verifica que funcione en la Swagger UI, y luego pide más mejoras.

1. Después de que Copilot haga los cambios, reinicia el backend y revisita `http://localhost:8000/docs`.

1. Compara la documentación antes y después. Deberías ver:
   - Descripciones más ricas para cada endpoint
   - Esquemas de request y response claramente definidos
   - Valores de ejemplo que facilitan probar endpoints directamente desde la Swagger UI

   **🎯 Objetivo: Tu documentación de Swagger debería describir claramente cada endpoint, sus parámetros, posibles respuestas e incluir ejemplos útiles. ✅**

   <details>
   <summary>Ejemplo de mejoras a buscar</summary><br/>

   Aquí hay algunas cosas que hacen que la documentación de Swagger brille:

   - **Tags:** Endpoints agrupados por categoría (por ejemplo, `Activities`, `Registration`)
   - **Modelos de respuesta:** En lugar de devolver un dict crudo, define modelos Pydantic como `ActivityResponse`, `SignupResponse`, etc.
   - **Códigos de estado:** Cada endpoint documenta qué sucede en éxito (200/201), solicitud incorrecta (400) y no encontrado (404).
   - **Descripciones:** Cada endpoint tiene un resumen claro de una línea y una descripción más larga explicando su comportamiento.
   - **Ejemplos:** Ejemplos de request y response para que los desarrolladores puedan entender rápidamente el formato esperado.

   </details>

#### Parte C: Valida y prueba desde Swagger UI

1. Con tu documentación mejorada en su lugar, usa la **Swagger UI** en `/docs` para probar cada endpoint interactivamente:
   - Intenta listar todas las actividades
   - Inscribe a un estudiante en una actividad
   - Retira a un estudiante de una actividad
   - Intenta operaciones inválidas (por ejemplo, inscribirse dos veces, retirar a alguien que no está registrado)

1. Verifica que las respuestas de error coincidan con la documentación — los códigos de estado y mensajes de error deberían ser consistentes.

   > 💡 **Tip:** Si encuentras inconsistencias entre el comportamiento real de la API y la documentación, ¡pídele a Copilot que las corrija! Esta es una tarea común del mundo real — ¡mantener la documentación y el código sincronizados!

## Paso 6: Hora de hacer commit

Pídele a GitHub Copilot Chat que haga un resumen de todo lo que has hecho hasta ahora, puedes hacer commit de esto si quieres o simplemente guardarlo como un resumen personal.

## ¡Felicidades! 🎉

¡Has completado el Lab 02! Aquí tienes un resumen de lo que aprendiste:

- **Modo Ask** — Usaste Copilot Chat para incorporarte a un nuevo proyecto, entender su estructura y recordar comandos de terminal
- **Sugerencias Inline y Chat Inline** — Corregiste un bug de registro duplicado con completados de código y generaste datos de ejemplo usando Chat Inline
- **Agent Mode** — Dejaste que Copilot agregara autónomamente una visualización de participantes, botones de cancelar inscripción y corrigiera un bug de refresco de UI en múltiples archivos
- **Plan Agent** — Diseñaste una estrategia de testing de forma colaborativa antes de pasar la implementación a Agent Mode

Ahora estás equipado/a para usar los tres modos de Copilot Chat en tu flujo de trabajo diario. ¡Dirígete a los otros laboratorios en este repositorio para seguir explorando!
