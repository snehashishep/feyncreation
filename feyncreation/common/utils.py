# common/utils.py

def parse_process(input_str):
    """Parses the process string to extract incoming, outgoing, and fused particles."""
    try:
        incoming, outgoing_fused = input_str.split('>')
        incoming = incoming.strip().split()
        outgoing_fused = outgoing_fused.strip().split()
        outgoing = outgoing_fused[:2]
        fused = outgoing_fused[2:]
        return incoming, outgoing, fused
    except ValueError:
        print("Invalid process format. Use 'in1 in2 > out1 out2 fused1 fused2'.")
        return None, None, None

