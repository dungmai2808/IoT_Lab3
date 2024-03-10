import sys
from Adafruit_IO import MQTTClient
import time
import random
from uart import *

AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "dungmai2808"
AIO_KEY = "aio_blaG72ZFediI1heOIvD8fxW3KFv1"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", Feed id:" + feed_id)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData(1)
        else:
            writeData(2)
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData(3)
        else:
            writeData(4)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    readSerial(client)
    time.sleep(1)