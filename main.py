#!/usr/bin/python

import socket
import threading
import sys
import re
import requests
import urllib3

from Consts import FLORY_VEHICLE_PRODUCT_LINE_MESSAGE_PGN, SERVER_IP, SERVER_PORT, SPLUNK_AUTHORIZATION_KEY, \
    SPLUNK_ADDRESS
from Flory.FloryProprietaryB_65380 import FloryProprietaryB_65380
from FloryCanbusMessageFactory import FloryCanbusMessageFactory

urllib3.disable_warnings()


def splunkHec(data, source):
    url = SPLUNK_ADDRESS
    authHeader = {'Authorization': SPLUNK_AUTHORIZATION_KEY}
    payload = {"index": "flory", "sourcetype": "_json", "source": source, "event": data}
    return requests.post(url, headers=authHeader, json=payload, verify=False)


def on_new_client(client_socket, addr):
    bg_id = None
    model_id = None
    model_name = None

    while True:
        try:
            msg = client_socket.recv(2048).decode()
            if bg_id is None:
                result = re.compile(r".*?S2V6l000(.*?);", re.DOTALL).findall(msg)
                if result is not None and len(result) > 0:
                    bg_id = result[0]

            if bg_id is None:
                continue

            print(f"BG ID:{bg_id}")
            print(f"Message Received: {msg}")

            bg = re.compile(r".*?J1939 : J1939: (\d+)-(\d+)-(\d+)-(\d+)-(\d+) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}) ([0-9a-fA-F]{2}).*?", re.DOTALL).findall(msg)
            if bg is None or len(bg) == 0:
                continue

            for item in bg:
                pgn = item[0]
                data = item[5:]

                if model_id is None and pgn == FLORY_VEHICLE_PRODUCT_LINE_MESSAGE_PGN:
                    model_id = FloryProprietaryB_65380.get_model_id(data)
                    model_name = FloryProprietaryB_65380.get_model_name(model_id)

                if model_id is None:
                    continue

                message = FloryCanbusMessageFactory.create_message(pgn, data)
                if message is None:
                    continue

                message.load_dictionary(model_id)
                dictionary = message.get_dictionary()

                # if item[0] != "65411":
                #     continue

                dictionary["BgId"] = bg_id
                dictionary["RawData"] = list(data)
                dictionary["ModelId"] = model_id
                dictionary["ModelName"] = model_name
                print(splunkHec(dictionary, bg_id).content)

            #print(f'{addr} >> {msg}')
            #clientsocket.send(msg)

        except Exception as exp:
            print(exp)
            #client_socket.close()


s = socket.socket()    # Create a socket object
host = SERVER_IP       # socket.gethostname() # Get local machine name
port = SERVER_PORT     # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
    try:
        c, addr = s.accept()     # Establish connection with client.

        print(f"Got connection from {addr}")
        t = threading.Thread(target=on_new_client, args=(c, addr))  # construct the thread
        t.start()  # start the thread
    except KeyboardInterrupt as msg:
        s.close()
        sys.exit(0)

