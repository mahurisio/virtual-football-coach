# Metricas de jugadores

Este documento define las metricas iniciales para evaluar jugadores dentro de Virtual Football Coach.

La primera version del proyecto no pretende reemplazar el criterio del entrenador. Su objetivo es ordenar datos simples para que la evaluacion sea mas clara, mas constante y mas facil de comparar.

## Datos basicos del jugador

- Nombre completo.
- Edad.
- Posicion principal.
- Pie dominante.
- Equipo.
- Observaciones generales.

## Metricas de participacion

### Minutos jugados

Permite medir cuanto participa el jugador en cada partido.

Uso posible:

- Comparar rendimiento entre jugadores con minutos similares.
- Revisar si un jugador rinde mejor entrando desde el inicio o desde el banco.
- Medir continuidad deportiva.

### Calificacion del entrenador

Valor de 0 a 10 asignado por el entrenador.

Uso posible:

- Registrar percepcion tecnica del partido.
- Comparar la opinion del entrenador con los datos numericos.
- Medir evolucion con el tiempo.

## Metricas ofensivas

### Goles

Cantidad de goles anotados por el jugador.

### Asistencias

Pases o acciones directas que terminan en gol.

### Pases correctos

Cantidad de pases que llegaron a un companero.

### Pases fallidos

Cantidad de pases perdidos.

### Precision de pase

Se calcula asi:

```text
pases correctos / total de pases * 100
```

Interpretacion inicial:

- 80% o mas: buena precision.
- Entre 60% y 79%: precision aceptable, pero mejorable.
- Menos de 60%: requiere trabajo tecnico.

## Metricas defensivas

### Recuperaciones

Acciones donde el jugador recupera la pelota para su equipo.

### Duelos ganados

Disputas individuales ganadas ante un rival.

### Faltas cometidas

Sirve para analizar agresividad, mala ubicacion o problemas de tiempo en la marca.

### Tarjetas

Permite medir riesgo disciplinario.

## Lectura inicial por posicion

### Portero

Metricas futuras importantes:

- Atajadas.
- Goles recibidos.
- Salidas exitosas.
- Juego con los pies.
- Comunicacion defensiva.

### Defensa

Metricas importantes:

- Recuperaciones.
- Duelos ganados.
- Faltas cometidas.
- Precision de pase.
- Errores en salida.

### Mediocampista

Metricas importantes:

- Precision de pase.
- Recuperaciones.
- Asistencias.
- Participacion general.
- Toma de decisiones.

### Delantero

Metricas importantes:

- Goles.
- Asistencias.
- Duelos ganados.
- Participacion ofensiva.
- Efectividad frente al arco.

## Recomendaciones iniciales

El sistema puede generar recomendaciones sencillas con reglas basicas.

Ejemplos:

- Si la precision de pase es baja, recomendar ejercicios de pase bajo presion.
- Si las recuperaciones son bajas, recomendar trabajo de ubicacion y presion defensiva.
- Si la calificacion del entrenador es baja, recomendar revision tactica y participacion en el juego.
- Si hay muchas faltas, recomendar trabajo de temporizacion defensiva.

## Evolucion futura

En una version posterior se podran incluir metricas mas avanzadas:

- Distancia recorrida.
- Velocidad maxima.
- Zonas de calor.
- Pases progresivos.
- Perdidas en campo propio.
- Acciones bajo presion.
- Expected goals.
- Expected assists.
- Analisis de video.
