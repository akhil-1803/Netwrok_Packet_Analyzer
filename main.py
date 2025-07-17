from sniffer import start_sniffing

def main():
    print("==== Network Packet Analyzer ====")
    print("NOTE: You must have root/administrator permissions to capture packets.")
    try:
        interface = input("Enter interface (leave blank for default): ").strip()
        if not interface:
            interface = None
        start_sniffing(interface=interface)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
