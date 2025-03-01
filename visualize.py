import pandas as pd
import matplotlib.pyplot as plt

def visualize_traffic(filename="traffic_log.csv"):
    """
    Generates a bar chart of network traffic by protocol.
    :param filename: Path to the packet log CSV file
    """
    df = pd.read_csv(filename)
    protocol_count = df["protocol"].value_counts()

    plt.figure(figsize=(10, 5))
    protocol_count.plot(kind='bar', color='skyblue')
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.title("Network Traffic by Protocol")
    plt.show()

if __name__ == "__main__":
    visualize_traffic()
