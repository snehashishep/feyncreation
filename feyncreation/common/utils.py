# common/utils.py

def parse_process(input_str):
    """Parses the process string to extract incoming, outgoing, and fused particles."""
    try:
        # Split the process into incoming and outgoing/fused parts
        incoming, outgoing_fused = input_str.split('>')
        incoming = incoming.strip().split()
        outgoing_fused = outgoing_fused.strip().split()
        
        # Handle three-body decay case: incoming == 1 and outgoing_fused == 3
        if len(incoming) == 1 and len(outgoing_fused) == 3:
            outgoing = outgoing_fused  # All 3 particles are outgoing
            fused = []  # No fused particles in three-body decay
        # Handle cases where incoming != 1 or where fused particles may exist (e.g., vbf1, twotwo)
        elif len(outgoing_fused) >= 2:
            outgoing = outgoing_fused[:2]  # First two are outgoing particles
            fused = outgoing_fused[2:]  # The rest are fused particles, if any
        else:
            print(f"Error: Unexpected number of outgoing particles in '{input_str}'")
            return None, None, None

        return incoming, outgoing, fused
    except ValueError:
        print("Invalid process format. Use 'in1 in2 > out1 out2 fused1 fused2' for general processes or 'in1 > out1 out2 out3' for three-body decay.")
        return None, None, None


