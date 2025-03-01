import pyshark

INTERFACE = r"\Device\NPF_{27EF43B5-8DF3-45E3-BE3E-950B2C5958F6}"  # Wi-Fi
# If using Ethernet, change to:
# INTERFACE = r"\Device\NPF_{36617D44-D705-4564-A0A7-D172265DF1F7}"

def capture_packets(interface=INTERFACE, count=50):
    cap = pyshark.LiveCapture(interface=interface)
    packets = []

    for packet in cap.sniff_continuously(packet_count=count):
        try:
            packets.append({
                "timestamp": packet.sniff_time,
                "src_ip": packet.ip.src if hasattr(packet, 'ip') else None,
                "dst_ip": packet.ip.dst if hasattr(packet, 'ip') else None,
                "protocol": packet.highest_layer,
                "length": packet.length
            })
        except AttributeError:
            continue

    return packets

if __name__ == "__main__":
    packets = capture_packets()
    for pkt in packets:
        print(pkt)
