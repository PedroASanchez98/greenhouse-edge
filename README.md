# greenhouse-edge

Edge pipeline "invernadero" en Raspberry Pi:

- MQTT (Mosquitto) como bus de mensajes
- InfluxDB 1.8 como base de datos de series temporales
- Publicador de telemetría real (CPU temp) y ingestor MQTT→Influx

## Arquitectura (v0)

Publisher (Python) → MQTT → Ingestor (Python) → InfluxDB

## Requisitos

- Raspberry Pi OS
- Docker + Docker Compose
- Python 3 + venv

## Arranque

1) Levantar servicios:

```bash
sudo docker compose up -d
```

2) Crear entorno Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install paho-mqtt requests
```

3) Ejecutar ingestor

```bash
python mqtt_to_influx.py
```

4) Ejecutar publisher

```bash
python publish_cpu_temp.py
```

## MQTT Topics

Ver docs/topics.md

## Influx Schema

Ver docs/influx_schema.md
