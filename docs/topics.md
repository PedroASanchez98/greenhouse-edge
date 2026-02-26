# MQTT Topics & Payload (v0)

## Scope
Contrato mínimo para telemetría en edge, pensado para:
- empezar con métricas reales del propio sistema (Raspberry Pi)
- escalar a sensores reales de invernadero sin romper compatibilidad

## Topics

### Telemetry (1 métrica por mensaje)
`greenhouse/<gh_id>/<zone_id>/<sensor_id>/telemetry`

Ejemplo (Raspberry como “sensor”):
`greenhouse/gh1/zoneA/rpi/telemetry`

### Events (derivados: alarmas, anomalías, etc.)
`greenhouse/<gh_id>/<zone_id>/<sensor_id>/events`

Ejemplo:
`greenhouse/gh1/zoneA/rpi/events`

## Payload: Telemetry

JSON con una métrica por mensaje:

```json
{
  "ts": "2026-02-24T22:35:10.123Z",
  "metric": "cpu_temp_c",
  "value": 35.8
}
