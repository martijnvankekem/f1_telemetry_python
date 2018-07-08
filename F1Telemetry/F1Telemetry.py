#!/usr/bin/env python
# coding=utf-8

#
# F1 Telemetry - Main application
# Written in Python by Martijn van Kekem
# URL: https://www.vankekem.com/
#
# Receives F1 Telemetry data for the custom F1 steering wheel, designed by Martijn van Kekem
#
# This work was made possible thanks to the following sources:
# -- https://github.com/gmaslowski/f1game-telemetry/wiki/udp-packet-1237-structure
# -- http://forums.codemasters.com/discussion/53139/f1-2017-d-box-and-udp-output-specification
#
# This work is licensed under a "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License"
# License URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
#

import socket, math, sys # Import libraries
sys.path.append('ArrayStructure.py') # Include array structure
from ArrayStructure import * # Import everything from array structure
from struct import * # Import everything from struct

UDP_IP = "192.168.0.10" # UDP listen IP-address
UDP_PORT = 20777 # UDP listen port
PACKET_SIZE = 1289 # Amount of bytes in packet

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create UDP Socket
udp.bind((UDP_IP, UDP_PORT)) # Bind socket to IP and port
print ("F1 Telemetry ready") # Show we're ready
print ("Listening on " + UDP_IP + ":" + str(UDP_PORT)) # Show IP and port

# Get UDP value by it's name
def getValByName(name):
    global returnData # Access the global variable returnData
    for x in range(0, len(returnData)): # Do for every item in returnData
        if returnData[x][0] == name: # If this item matches the name
            return returnData[x][1] # Return the value of this item
    return -1 # Nothing found, return -1

# Run continuously
while True:
    index = 0; # Set starting index
    data, addr = udp.recvfrom(PACKET_SIZE) # Receive value from UDP socket
    for x in range(0, len(returnData)): # Do for every item in the received array
        size = 4 if returnData[x][2] == 'f' else 1 # Set size based on if it's a byte or float
        returnData[x][1] = unpack('<' + returnData[x][2], data[index:index+size])[0] # Add float to the array
        index += size # Increase starting index with the size

    # Usage: getValByName(tag)
    # Example: getValByName("m_speed")
    # Returns: Current car speed in meters per second
    # A full list of tags can be found in the 'ArrayStructure' file
