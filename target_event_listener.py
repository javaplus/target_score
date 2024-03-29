import paho.mqtt.client as mqtt
import json
import score_keeper
import os
import urllib2

serverIP = os.environ['pi_server_ip']

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected Target Event Listener with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("global/events")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    eventMessage = {}
    eventMessage = json.loads(msg.payload)
    print("On Message Called")
    print(msg.topic+" "+str(msg.payload))
    print("event message=" + str(eventMessage))
    eventMessage = dict(eventMessage)
    if 'event_name' in eventMessage:
        handleTargetHit(eventMessage)
    elif msg.payload == "timer_stopped":
        handleTimerEnd()
    else:
        print("No event name")

def handleTargetHit(eventMessage):
    if eventMessage.get('event_name') == 'target_hit':
            print("got a hit!!!!!!!!")
            targetId = eventMessage.get('target_id')
            score_keeper.addScore(1, targetId)
            print("Score for " + targetId + " =" + str(score_keeper.getScoreForTarget(targetId)))
    else:
        print("Not a target hit event")

def handleTimerEnd():
    target_1 = score_keeper.getScoreForTarget('target_1')
    print("Got timer end message")
    message = "Final Score is " + str(target_1) + "."
    data = {"say": message + message,
            "parms": "-s 140 -ven-us+f3"}
    
    req = urllib2.Request('http://' + serverIP + ':5000/say')
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(data))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(serverIP, 1883, 60)
#client.connect("192.168.1.112", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()