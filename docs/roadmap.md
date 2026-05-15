# Roadmap del proyecto

Este documento organiza la ruta de trabajo de Virtual Football Coach.

La idea es avanzar por fases pequenas, claras y defendibles. El proyecto debe crecer como una herramienta real, no como una promesa inflada.

## Fase 1: Base del proyecto

Estado: en progreso.

Objetivo: crear una estructura inicial clara y ejecutable.

Tareas:

- Crear README principal.
- Crear dependencias iniciales.
- Crear archivo .gitignore.
- Crear estructura base del backend.
- Crear modelos de jugadores, partidos y evaluaciones.
- Crear rutas iniciales.
- Crear documentacion del proyecto.

## Fase 2: API inicial

Estado: en construccion.

Objetivo: permitir registrar informacion deportiva basica.

Tareas:

- Registrar jugadores.
- Listar jugadores.
- Registrar partidos.
- Listar partidos.
- Registrar evaluaciones.
- Listar evaluaciones.
- Generar recomendaciones basicas por jugador.
- Probar la API desde /docs.

## Fase 3: Mejorar la logica de recomendaciones

Estado: pendiente.

Objetivo: crear reglas mas utiles para evaluar rendimiento.

Tareas:

- Evaluar precision de pase.
- Evaluar recuperaciones.
- Evaluar duelos ganados.
- Evaluar disciplina.
- Evaluar rendimiento segun posicion.
- Crear recomendaciones diferenciadas para defensa, mediocampo, ataque y porteria.

## Fase 4: Base de datos real

Estado: pendiente.

Objetivo: reemplazar el almacenamiento temporal por una base de datos.

Opciones iniciales:

- SQLite para pruebas locales.
- PostgreSQL para una version mas profesional.
- Amazon RDS para una etapa futura en AWS.

## Fase 5: Interfaz web

Estado: pendiente.

Objetivo: crear una interfaz sencilla para entrenadores.

Pantallas iniciales:

- Registro de jugadores.
- Registro de partidos.
- Evaluacion individual.
- Reporte de jugador.
- Recomendaciones de entrenamiento.

## Fase 6: Analisis colectivo

Estado: pendiente.

Objetivo: analizar el comportamiento del equipo, no solo de jugadores individuales.

Funciones futuras:

- Rendimiento por posicion.
- Balance ofensivo y defensivo.
- Debilidades colectivas.
- Comparacion entre partidos.
- Reporte general del equipo.

## Fase 7: Inteligencia artificial

Estado: vision futura.

Objetivo: usar IA para apoyar la toma de decisiones tecnicas.

Posibles funciones:

- Recomendaciones de entrenamiento mas precisas.
- Analisis de texto de observaciones del entrenador.
- Clasificacion de fortalezas y debilidades.
- Prediccion de mejora por jugador.
- Asistente virtual para planificar entrenamientos.

## Fase 8: Datos avanzados y video

Estado: vision futura.

Objetivo: integrar datos mas complejos del rendimiento deportivo.

Posibles funciones:

- Analisis de video.
- Distancia recorrida.
- Velocidad maxima.
- Mapas de calor.
- Zonas de mayor participacion.
- Seguimiento de acciones por jugador.

## Criterio de avance

Cada fase debe dejar evidencia en GitHub:

- Codigo organizado.
- Documentacion clara.
- Commits con mensajes entendibles.
- Proyecto ejecutable.
- Nuevas rutas o funcionalidades probables.

El objetivo es construir una herramienta realista para ayudar a entrenadores y procesos formativos a competir mejor con datos, criterio y tecnologia.
