def protocol_name(proto_num):
    # Common protocol numbers
    proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    return proto_map.get(proto_num, f"Unknown ({proto_num})")

def format_payload(payload_bytes, max_len=64):
    # Safe readable payload preview
    payload_str = ''.join(
        chr(b) if 32 <= b < 127 else '.' for b in payload_bytes[:max_len]
    )
    if len(payload_bytes) > max_len:
        payload_str += "..."
    return payload_str
