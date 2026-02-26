# InfluxDB schema (v0)

Measurement: telemetry

Tags:
- gh_id: <from topic>
- zone_id: <from topic>
- sensor_id: <from topic>
- metric: <from payload.metric>

Fields:
- value: <from payload.value>

Time:
- payload.ts parsed as UTC
