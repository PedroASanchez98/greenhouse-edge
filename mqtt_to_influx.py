import json
import requests
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
USERNAME = "usuario1"
PASSWORD = "1234"

INFLUX_URL = "http://localhost:8086/write?db=greenhouse"

TOPIC = "greenhouse/+/+/+/telemetry"


def on_message(client, userdata, msg):
    topic_parts = msg.topic.split("/")
    gh_id = topic_parts[1]
    zone_id = topic_parts[2]
    sensor_id = topic_parts[3]
    measurement = topic_parts[4]

    payload = json.loads(msg.payload.decode())

    dt = datetime.fromisoformat(payload["ts"])
    ts_ns = int(dt.timestamp() * 1_000_000_000)

    metric = payload["metric"]
    value = payload["value"]

    line = f"{measurement},gh_id={gh_id},zone_id={zone_id},sensor_id={sensor_id},metric={metric} value={value} {ts_ns}"

    print("Mensaje recibido:")
    print("  Topic:", msg.topic)
    print("  Line protocol:", line)
    resp = requests.post(INFLUX_URL, data=line)
    if resp.status_code != 204:
        print("  Influx write failed:", resp.status_code, resp.text)

def main():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
    client.loop_forever()


if __name__ == "__main__":
    main()
