# Virtual Football Coach

Sistema en construccion para analisis deportivo, evaluacion de jugadores y recomendaciones de entrenamiento usando datos, criterios tecnicos e inteligencia artificial de forma progresiva.

Este proyecto nace de una idea personal: siempre me ha llamado la atencion ser tecnico de futbol. Me interesa la direccion de equipos, la lectura del juego, el rendimiento de los jugadores y la posibilidad de convertir el deporte en algo mas competitivo, ordenado y medible.

La intencion no es empezar pensando en equipos profesionales grandes. El punto de partida es mas realista: colegios, escuelas deportivas, clubes pequenos y procesos de formacion donde muchas decisiones todavia se toman solo por intuicion. La intuicion del entrenador es importante, pero cuando se apoya en datos puede volverse mas precisa.

## Objetivo del proyecto

Crear una herramienta que permita registrar jugadores, partidos, estadisticas y evaluaciones para detectar fortalezas, debilidades y posibles recomendaciones de entrenamiento.

El sistema busca ayudar a responder preguntas como:

- Que jugador esta rindiendo mejor segun su posicion.
- Que virtudes tecnicas tiene cada jugador.
- Que defectos debe trabajar.
- Como se comporta el equipo en ataque y defensa.
- Que aspectos colectivos deben entrenarse.
- Como tomar decisiones con datos y no solo con impresion visual.

## Alcance inicial

La primera version sera sencilla y manual. El entrenador o analista podra registrar informacion basica de jugadores y partidos.

Datos iniciales:

- Jugadores.
- Posiciones.
- Partidos.
- Minutos jugados.
- Goles.
- Asistencias.
- Pases correctos e incorrectos.
- Recuperaciones.
- Duelos ganados.
- Faltas.
- Tarjetas.
- Calificacion del partido.
- Observaciones tecnicas.

## Estado actual

El proyecto ya cuenta con una primera API construida con FastAPI. La version inicial permite:

- Registrar jugadores.
- Listar jugadores.
- Registrar partidos.
- Listar partidos.
- Registrar evaluaciones individuales.
- Listar evaluaciones.
- Generar una recomendacion basica por jugador.

## Tecnologias actuales

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git y GitHub

## Tecnologias previstas

- Base de datos SQL.
- PostgreSQL o SQLite para primeras pruebas.
- HTML, CSS y JavaScript.
- React en una etapa futura.
- AWS para despliegue, almacenamiento y analisis de datos.
- Modelos de IA para recomendaciones futuras.

## Estructura actual del proyecto

```text
virtual-football-coach/
|-- docs/
|   |-- project-vision.md
|   |-- requirements.md
|   |-- player-metrics.md
|   |-- roadmap.md
|-- src/
|   |-- __init__.py
|   |-- main.py
|   |-- app.py
|   |-- database.py
|   |-- models.py
|   |-- routes/
|       |-- __init__.py
|       |-- players.py
|       |-- games.py
|       |-- evaluations.py
|-- .gitignore
|-- requirements.txt
|-- README.md
```

## Como ejecutar el proyecto en local

### 1. Clonar el repositorio

```bash
git clone https://github.com/mahurisio/virtual-football-coach.git
cd virtual-football-coach
```

### 2. Crear entorno virtual

En Windows:

```bash
python -m venv .venv
.venv/Scripts/activate
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API

```bash
uvicorn src.main:app --reload
```

### 5. Abrir la documentacion automatica

```text
http://localhost:8000/docs
```

## Rutas iniciales

```text
GET  /
GET  /health
GET  /players/
POST /players/
GET  /players/{player_id}
GET  /games/
POST /games/
GET  /evaluations/
POST /evaluations/
GET  /evaluations/{player_id}/recommendation
```

## Documentacion del proyecto

- [Vision del proyecto](docs/project-vision.md)
- [Requisitos iniciales](docs/requirements.md)
- [Metricas de jugadores](docs/player-metrics.md)
- [Roadmap](docs/roadmap.md)

## Vision futura

A futuro, el proyecto puede crecer hacia:

- Analisis de datos publicos.
- Comparacion por posicion.
- Reportes individuales.
- Reportes colectivos.
- Recomendaciones automaticas de entrenamiento.
- Analisis de video.
- Datos fisicos como distancia recorrida, velocidad y zonas de esfuerzo.
- Modelos de inteligencia artificial para apoyar decisiones tecnicas.

## Autor

Daniel Mauricio Padilla Gonzalez  
Tecnologo industrial y estudiante de Ingenieria de Software  
Manizales, Caldas, Colombia
