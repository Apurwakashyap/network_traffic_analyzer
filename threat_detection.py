import pandas as pd
from collections import Counter

def detect_port_scan(filename="traffic_log.csv", threshold=10):
    """
    Detects port scanning by checking if an IP sends packets to many destinations.
    :param filename: Path to the packet log CSV file
    :param threshold: Number of connections to flag as a scan
    """
    df = pd.read_csv(filename)
    src_count = Counter(df["src_ip"])

    for ip, count in src_count.items():
        if count > threshold:
            print(f"[ALERT] Port Scanning Detected from {ip}")

def detect_ddos(filename="traffic_log.csv", threshold=100):
    """
    Detects DDoS attacks by analyzing high packet volumes.
    :param filename: Path to the packet log CSV file
    :param threshold: Number of requests to trigger a DDoS alert
    """
    df = pd.read_csv(filename)
    ip_count = Counter(df["src_ip"])

    for ip, count in ip_count.items():
        if count > threshold:
            print(f"[ALERT] Possible DDoS attack from {ip}")

if __name__ == "__main__":
    detect_port_scan()
    detect_ddos()
