# Libraries
import paho.mqtt.client as mqtt
from gtts import gTTS
import os

# Configuration
MQTT_BROKER = "192.168.1.10"
MQTT_PORT = 1883
MQTT_TOPIC = "tts/pi"
MQTT_USER = ""
MQTT_PASS = ""
LANGUAGE = "sv"
AUDIO_DEVICE = "plughw:3,0"
TEMP_FILE = "/tmp/tts.mp3"

# Checking connection and subscribing to topic
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[TTS] Conneced to MQTT {MQTT_BROKER}:{MQTT_PORT}")
        client.subscribe(MQTT_TOPIC)
        print(f"[TTS] INFO: Subscibing to '{MQTT_TOPIC}'")
    else:
        print(f"[TTS] ERR: Failed to connect (Code {rc})")

# Message handling
def on_message(client, userdata, msg):
    text = msg.payload.decode().strip()
    print(f"[TTS] INFO: Message recieved: '{text}'")
    if not text:
        print("[TTS] WARN: Empty message, skipping")
        return

    try:
        # Generating TTS to file using gTTS
        tts = gTTS(text=text, lang=LANGUAGE)
        tts.save(TEMP_FILE)
		
		# Check file size
        if os.path.exists(TEMP_FILE) and os.path.getsize(TEMP_FILE) > 0:
			
			# Play audio file on speaker
			print(f"[TTS] INFO: TTS file created: {TEMP_FILE} ({os.path.getsize(TEMP_FILE)} bytes)")
            os.system(f"mpg321 -q -a {AUDIO_DEVICE} {TEMP_FILE}")
        else:
            print("[TTS] ERR: TTS file seems empty")
	
    except Exception as e:
        print("[TTS] ERR: Something went wrong with TTS or audio play:", e)
    finally:
        if os.path.exists(TEMP_FILE):
            os.remove(TEMP_FILE)

# Configuration of the MQTT Client
client = mqtt.Client()
if MQTT_USER and MQTT_PASS:
    client.username_pw_set(MQTT_USER, MQTT_PASS)
client.on_connect = on_connect
client.on_message = on_message

# Connecting to MQTT Broker
print(f"[TTS] Connecting to {MQTT_BROKER}:{MQTT_PORT}...")
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
