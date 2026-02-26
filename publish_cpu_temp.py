import time
import json
import subprocess
from datetime import datetime, timezone
import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "localhost"
PORT = 1883
USERNAME = "usuario1"
PASSWORD = "1234"

TOPIC = "greenhouse/gh1/zoneA/rpi/telemetry"

def read_cpu_temp():
    output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    # output example: "temp=35.8'C\n"
    value_str = output.split("=")[1].split("'")[0]
    return float(value_str)

def build_payload(value):
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "metric": "cpu_temp_c",
        "value": value
    }

def main():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(BROKER, PORT, 60)
    for _ in range (0, 12):
        temp = read_cpu_temp()
        payload = build_payload(temp)
        client.publish(TOPIC, json.dumps(payload))
        print(f"Publicando payload: {payload}")
        splitted_topic = TOPIC.split("/")
        dt = datetime.fromisoformat(payload["ts"])   # ya incluye +00:00
        ts_ns = int(dt.timestamp() * 1_000_000_000)
        print(f"Lo que debería sacar el ingestor: {splitted_topic[4]},gh_id={splitted_topic[1]},zone_id={splitted_topic[2]},sensor_id={splitted_topic[3]},metric=cpu_temp_c value={payload["value"]} {ts_ns}")
        time.sleep(5)
    client.disconnect()

if __name__ == "__main__":
    main()
