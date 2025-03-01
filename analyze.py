import pandas as pd
from network_monitoring_system.backened.capture import capture_packets

def save_to_csv(packets, filename="traffic_log.csv"):
    """
    Saves captured packet data into a CSV file.
    :param packets: List of packet dictionaries
    :param filename: Output CSV filename
    """
    df = pd.DataFrame(packets)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    packets = capture_packets()
    save_to_csv(packets)
