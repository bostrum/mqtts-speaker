# mqtts-speaker
Listening for messages from MQTT broker to alert as audio on speaker.  
Currently using it with Home Assistant to send voice alerts when my coffee is done brewing ☕

# Prerequisites
- MQTT Broker like Mosquitto setup.
- Integration of some kind to send messages, Home Assistant etc.
- Device with a speaker that can run Python.

# Getting started
1. Check that all prerequisites are prepared and setup.
3. Install libraries paho and gtts using pip or other package manager.
4. Clone the repository.
5. Edit the .py file and change variables under '# Configuration' where needed.
6. MQTT_BROKER and AUDIO_DEVICE most likely. Run below to find your speaker.
````
aplay -l
````
5. Setup .py with systemd for example to run on start.

# Example
- Mosquitto Broker installed on server or add-on in Home Assistant.
- HA Automation for sending MQTT message to the broker on trigger. YAML example [here](https://github.com/bostrum/mqtts-speaker/tree/main/ha).
- Raspberry Pi and [this](https://thepihut.com/products/mini-external-usb-stereo-speaker) speaker.
<img width="537" height="298" alt="image" src="https://github.com/user-attachments/assets/40080599-120f-4a14-8c85-c0b9d857cd77" />

# Dependencies
- Python libraries
  - __paho__ (MQTT Client for subscribing to broker)
  - __gtts__ (Google Text-to-Speech)
- Binaries
  - __mpg321__ (For playing audio file)
