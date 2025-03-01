from capture import capture_packets
from analyze import save_to_csv
from threat_detection import detect_port_scan, detect_ddos
from visualize import visualize_traffic
from send_email import send_email

def main():
    print("🚀 Starting Network Traffic Analyzer...\n")
    
    # Step 1: Capture Packets
    packets = capture_packets(count=100)
    save_to_csv(packets)

    # Step 2: Run Threat Detection
    detect_port_scan()
    detect_ddos()

    # Step 3: Visualize Traffic
    visualize_traffic()

    # Step 4: Send Alert if Threats Detected
    if packets:
        send_email("🚨 Network Threat Detected!", "Suspicious activity found in network logs.","apurwa1909@gmail.com")

if __name__ == "__main__":
    main()
