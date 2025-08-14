#!/usr/bin/env python3
import os
import socket
import requests
import psutil
import ping3
from tabulate import tabulate

# ASCII network icon
ascii_icon = r"""
      ___      ___
     (o o)    (o o)
ooO--(_)--Ooo--(_)--Ooo
"""

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text.strip()
    except:
        return "N/A"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "N/A"

def get_gateway():
    try:
        gws = psutil.net_if_addrs()
        return psutil.net_if_stats()
    except:
        return "N/A"

def get_dns_servers():
    try:
        with open("/etc/resolv.conf") as f:
            return [line.split()[1] for line in f if line.startswith("nameserver")]
    except:
        return ["N/A"]

def get_ping_latency(host="8.8.8.8"):
    try:
        latency = ping3.ping(host, unit="ms")
        return f"{latency:.2f} ms" if latency else "N/A"
    except:
        return "N/A"

def get_bandwidth_usage():
    try:
        net1 = psutil.net_io_counters()
        os.sleep(1)
        net2 = psutil.net_io_counters()
        sent = (net2.bytes_sent - net1.bytes_sent) / 1024
        recv = (net2.bytes_recv - net1.bytes_recv) / 1024
        return f"↑ {sent:.2f} KB/s, ↓ {recv:.2f} KB/s"
    except:
        return "N/A"

if __name__ == "__main__":
    print(ascii_icon)
    data = [
        ["Public IP", get_public_ip()],
        ["Local IP", get_local_ip()],
        ["Gateway", "N/A"],  # Could be improved with netifaces
        ["DNS Servers", ", ".join(get_dns_servers())],
        ["Ping Latency", get_ping_latency()],
        ["Bandwidth", get_bandwidth_usage()]
    ]
    print(tabulate(data, headers=["Metric", "Value"]))
