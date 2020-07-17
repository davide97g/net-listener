import sys
import subprocess
import os
from time import sleep

from spotify import play, pause

IP_DEVICE = "192.168.1.67"

connected = False

sleepTime = int(input("sleep time: "))


def status(connected):
    print("Connection status: ", "OK" if connected else "KO")


def ping(IP_DEVICE, connected):

    print("ping ", IP_DEVICE)

    proc = subprocess.Popen(["ping", IP_DEVICE], stdout=subprocess.PIPE)

    found = False

    while True:
        line = proc.stdout.readline()
        if not line:
            break
        line = line.decode("utf-8")
        # condizione bruttissima ma per ora è l'unica idea che ho avuto
        if line.find("Tempo") != -1:
            found = True
            if not connected:
                connected = True
                status(connected)
                play()
            break

    if not found:
        connected = False
        status(connected)
        pause()

    return connected


while True:
    sleep(sleepTime)
    connected = ping(IP_DEVICE, connected)
