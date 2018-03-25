#!/usr/bin/python
# -*- coding: utf-8 -*-

# Installation
# pip install websocket-client
import websocket

def on_message(ws, message):
    print(message)

ws = websocket.WebSocketApp("wss://api.kkcoin.com/ws/KK_ETH@ticker", 
                            on_message = on_message)
ws.run_forever()
