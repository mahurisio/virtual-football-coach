# Requisitos del proyecto

Este documento define los requisitos iniciales de Virtual Football Coach.

El sistema busca registrar informacion deportiva basica, evaluar jugadores y generar recomendaciones de entrenamiento a partir de datos simples y observaciones tecnicas.

## Problema que se busca resolver

En muchos procesos deportivos pequenos, la evaluacion de jugadores depende solamente de la memoria del entrenador o de impresiones generales despues del partido.

Eso puede funcionar en parte, pero tambien deja problemas:

- No siempre se mide la evolucion del jugador.
- Las decisiones pueden depender demasiado de la percepcion.
- Es dificil comparar rendimiento por posicion.
- No se registran debilidades repetidas.
- No hay reportes claros para entrenar mejor.
- Se pierde informacion entre partidos y entrenamientos.

Virtual Football Coach busca organizar esa informacion para que el entrenador tenga una lectura mas clara del jugador y del equipo.

## Usuarios principales

### Entrenador

Usuario principal del sistema. Registra jugadores, partidos, evaluaciones y revisa recomendaciones.

### Analista deportivo

Usuario encargado de apoyar el registro de datos y revisar patrones de rendimiento.

### Coordinador deportivo

Usuario que puede revisar informacion general del equipo, evolucion de jugadores y necesidades de entrenamiento.

## Requisitos funcionales iniciales

### Gestion de jugadores

El sistema debe permitir registrar jugadores con informacion basica:

- Nombre completo.
- Edad.
- Posicion.
- Pie dominante.
- Equipo.
- Observaciones generales.

### Gestion de partidos

El sistema debe permitir registrar partidos con informacion general:

- Rival.
- Fecha del partido.
- Goles del equipo.
- Goles del rival.
- Observaciones del partido.

### Evaluacion individual

El sistema debe permitir registrar estadisticas basicas por jugador:

- Minutos jugados.
- Goles.
- Asistencias.
- Pases correctos.
- Pases fallidos.
- Recuperaciones.
- Duelos ganados.
- Faltas cometidas.
- Tarjetas amarillas.
- Tarjetas rojas.
- Calificacion del entrenador.
- Observaciones tecnicas.

### Recomendaciones

El sistema debe generar una recomendacion basica a partir de la evaluacion del jugador.

La recomendacion debe incluir:

- Fortalezas.
- Debilidades.
- Recomendaciones de entrenamiento.

## Requisitos no funcionales

### Simplicidad

La herramienta debe ser facil de usar por entrenadores, docentes o monitores deportivos que no necesariamente tengan conocimiento tecnico en software.

### Claridad

Los datos deben presentarse de forma comprensible. El objetivo no es llenar pantallas de numeros, sino convertir los datos en decisiones utiles.

### Escalabilidad

El proyecto debe poder crecer hacia base de datos, interfaz web, analisis avanzado e inteligencia artificial.

### Trazabilidad

Cada evaluacion debe quedar registrada para poder revisar la evolucion del jugador con el tiempo.

## Alcance inicial

La primera version incluye:

- Registro de jugadores.
- Registro de partidos.
- Registro de evaluaciones.
- Recomendaciones simples.
- API ejecutable con FastAPI.
- Documentacion inicial.

## Alcance futuro

En versiones posteriores se podra agregar:

- Base de datos real.
- Interfaz grafica.
- Reportes por jugador.
- Reportes por equipo.
- Comparacion por posicion.
- Analisis de video.
- Integracion con datos externos.
- Modelos de IA para recomendaciones mas precisas.

## Criterio de exito

El proyecto sera exitoso si logra demostrar que el rendimiento deportivo puede organizarse en datos simples y convertirse en recomendaciones utiles para mejorar el entrenamiento de jugadores y equipos.
