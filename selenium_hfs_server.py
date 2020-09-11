#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import json
import socket
import logging
import threading
import datetime
import os
from wifi_chrome import *
from hfs_http_server import *

# FRONT_END_SERVER_IP = "192.168.1.24"
FRONT_END_SERVER_IP = "192.168.0.100"
FRONT_END_SERVER_PORT = 9998

current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename='{}/wifi_network_server/log/selenium_server.log'.format(current_path),
                    filemode='a',  ##模式,有w和a,w就是写模式,每次都会重新写日志,覆盖之前的日志
                    # a是追加模式,默认如果不写的话,就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )


class FrontEndServer(object):
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def response(self):
        server = self.server
        server.bind((FRONT_END_SERVER_IP, FRONT_END_SERVER_PORT))
        server.listen(5)
        while True:
            conn, addr = server.accept()
            print("%s connected" % (conn))
            while True:
                try:
                    data = conn.recv(1024)
                    print(type(data), "\n", data)
                    dict_data = json.loads(data)
                    if not data:
                        # print "%s disconnected"%conn
                        break
                    elif dict_data.get("cmd") == "set_hfs_limit_50K":
                        set_hfs_limit(50)
                        conn.send("set_hfs_limit_50K success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_hfs_limit_1M":
                        set_hfs_limit(1000)
                        conn.send("set_hfs_limit_1M success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_hfs_limit_20M":
                        set_hfs_limit(20000)
                        conn.send("set_hfs_limit_20M success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_hfs_switch_off":
                        spend_time = set_hfs_switch_off()
                        send_data = {"spend-time": spend_time}
                        conn.send(json.dumps(send_data).encode("utf-8"))
                    elif dict_data.get("cmd") == "set_hfs_switch_on":
                        spend_time = set_hfs_switch_on()
                        send_data = {"spend-time": spend_time}
                        conn.send(json.dumps(send_data).encode("utf-8"))
                    elif dict_data.get("cmd") == "set_hfs_external_network":
                        set_hfs_external_network()
                        conn.send("set_hfs_external_network success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_parameter_wep":
                        set_wifi_parameter_wep()
                        conn.send("set_wifi_parameter_wep success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_parameter_wpa":
                        set_wifi_parameter_wpa()
                        conn.send("set_wifi_parameter_wpa success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_parameter_wpa2":
                        set_wifi_parameter_wpa2()
                        conn.send("set_wifi_parameter_wpa2 success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_parameter_wpa_wpa2":
                        set_wifi_parameter_wpa_wpa2()
                        conn.send("set_wifi_parameter_wpa_wpa2 success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_parameter_802_11n":
                        set_wifi_parameter_802_11n()
                        conn.send("set_wifi_parameter_802_11n success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_parameter_802_11b_g":
                        set_wifi_parameter_802_11b_g()
                        conn.send("set_wifi_parameter_802_11b_g success".encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_ap_on":
                        spend_time = set_wifi_ap_on()
                        send_data = {"spend-time": spend_time}
                        conn.send(json.dumps(send_data).encode("utf-8"))
                    elif dict_data.get("cmd") == "set_wifi_ap_off":
                        spend_time = set_wifi_ap_off()
                        send_data = {"spend-time": spend_time}
                        conn.send(json.dumps(send_data).encode("utf-8"))
                    else:
                        print(data)
                        print("unknown message")
                except:
                    break


if __name__ == '__main__':
    fes = FrontEndServer()
    t = threading.Thread(target=fes.response)
    t.setDaemon(True)
    t.start()
    try:
        print('Enter "Ctrl + C" to exit ')
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        print("program exited")
        sys.exit(0)
