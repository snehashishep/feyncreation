from feyncreation.common import config
import os
from feyncreation.diagram_class import twotwo, vbf1
from feyncreation.common.particles import particle_styles, particle_dict  # Import styles for different particles

# Diagram class registry
diagram_registry = {
    'twotwo': {
        's-channel': twotwo.SChannel,
        't-channel': twotwo.TChannel
    },
    'vbf1': vbf1.VBF1
}

# List of standard vector bosons
standard_vector_bosons = ['z', 'w+', 'w-', 'gamma']

def parse_process(input_str):
    """Parses the process string to extract incoming and outgoing particles."""
    try:
        incoming, outgoing = input_str.split('>')
        incoming = incoming.strip().split()
        outgoing = outgoing.strip().split()
        return incoming, outgoing
    except ValueError:
        print("Invalid process format. Use 'incoming1 incoming2 > outgoing1 outgoing2 fused'.")
        return None, None

def parse_input_card(card_path):
    """Parses an input card and returns a dictionary of input values."""
    input_data = {}
    with open(card_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=', 1)
                input_data[key.strip()] = value.strip().lower()
    return input_data

def get_user_input_from_card(card_path):
    """Generates a diagram based on the input card."""
    input_data = parse_input_card(card_path)
    diagram_class = input_data.get('diagram_class', 'twotwo')
    process_str = input_data.get('process', '')
    io_arrows = input_data.get('io_arrows', '').split()  # Get incoming/outgoing particles with arrows
    vec_arrows = input_data.get('vec_arrows', '').split()  # Get vector bosons with arrows (allow 'none')

    if "none" in vec_arrows:
        vec_arrows = []  # No arrows for vec1 and vec2 if 'none' is specified

    incoming, outgoing = parse_process(process_str)

    if diagram_class in diagram_registry:
        if diagram_class == "twotwo":
            channel_type = input_data.get('channel_type', 's-channel')
            if channel_type in diagram_registry[diagram_class]:
                diagram = diagram_registry[diagram_class][channel_type]()
                mediator = input_data.get('mediator', '').strip()
                med_arrow = input_data.get('med_arrow', 'false') == 'true'  # Parse mediator arrow as true/false

                diagram.draw(
                    incoming=incoming,
                    outgoing=outgoing,
                    mediator=mediator,
                    arrow_incoming1=incoming[0] in io_arrows,
                    arrow_incoming2=incoming[1] in io_arrows,
                    arrow_outgoing1=outgoing[0] in io_arrows,
                    arrow_outgoing2=outgoing[1] in io_arrows,
                    arrow_mediator=med_arrow,
                    output_filename=input_data.get('output_filename', 'output')
                )
            else:
                print(f"Channel type '{channel_type}' not recognized.")
        
        elif diagram_class == "vbf1":
            vec_bosons = input_data.get('vec_bosons', '').strip().split()
            fused = outgoing[2]  # Fused particle is the last one

            # Check if the fused particle needs an arrow
            arrow_fused = fused in io_arrows

            diagram = diagram_registry[diagram_class]()
            diagram.draw(
                incoming=incoming,
                outgoing=outgoing[:2],  # First two are the outgoing particles
                vec_bosons=vec_bosons,
                fused=fused,
                arrow_incoming1=incoming[0] in io_arrows,
                arrow_incoming2=incoming[1] in io_arrows,
                arrow_outgoing1=outgoing[0] in io_arrows,
                arrow_outgoing2=outgoing[1] in io_arrows,
                arrow_fused=arrow_fused,  # Pass the correct arrow setting for the fused particle
                arrow_vec1=vec_bosons[0] in vec_arrows,  # Check if vec1 needs an arrow
                arrow_vec2=vec_bosons[1] in vec_arrows,  # Check if vec2 needs an arrow
                output_filename=input_data.get('output_filename', 'output')
            )
        else:
            print(f"Diagram class '{diagram_class}' not recognized.")
    else:
        print(f"Diagram class '{diagram_class}' not recognized.")

def get_user_input():
    # Print available particles
    print("Available particles:")
    print(", ".join(particle_dict.keys()))
    use_card = input("Do you want to use an input card? (yes/no): ").lower()
    if use_card == 'yes':
        card_path = input("Enter the path to the input card: ").strip()
        if os.path.exists(card_path):
            get_user_input_from_card(card_path)
        else:
            print(f"Input card '{card_path}' not found.")
    else:
        diagram_class = input("Enter the class of diagram (e.g., 'twotwo', 'vbf1'): ").lower()

        if diagram_class in diagram_registry:
            if diagram_class == 'twotwo':
                channel_type = input("Choose channel type (s-channel/t-channel): ").lower()
                process_str = input("Enter the process (e.g., 'q qbar > t tbar'): ").strip()
                incoming, outgoing = parse_process(process_str)

                if incoming and outgoing:
                    mediator = input("Enter the mediator: ").strip().lower()
                    med_arrow = input("Do you want a mediator arrow? (true/false): ").lower() == 'true'
                    io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'q qbar'): ").strip().split()
                    output_filename = input("Enter the output filename (without extension): ").strip()

                    diagram = diagram_registry[diagram_class][channel_type]()
                    diagram.draw(
                        incoming=incoming,
                        outgoing=outgoing,
                        mediator=mediator,
                        arrow_incoming1=incoming[0] in io_arrows,
                        arrow_incoming2=incoming[1] in io_arrows,
                        arrow_outgoing1=outgoing[0] in io_arrows,
                        arrow_outgoing2=outgoing[1] in io_arrows,
                        arrow_mediator=med_arrow,
                        output_filename=output_filename
                    )

            elif diagram_class == 'vbf1':
                process_str = input("Enter the process (e.g., 'mu+ mu- > vm vmbar h'): ").strip()
                incoming, outgoing = parse_process(process_str)

                if incoming and outgoing:
                    fused = outgoing[2]  # The fused particle (last one)
                    vec_bosons = input("Enter vec1 and vec2 (e.g., 'z gamma'): ").strip().split()

                    io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'mu+ mu- vm vmbar'): ").strip().split()
                    vec_arrows = input("Which vector bosons do you want arrows? (e.g., 'q qbar' or 'none'): ").strip().split()
                    if "none" in vec_arrows:
                        vec_arrows = []  # No arrows for vec1 and vec2 if 'none' is specified
                    arrow_fused = fused in io_arrows  # Check if fused particle needs an arrow
                    output_filename = input("Enter the output filename (without extension): ").strip()

                    diagram = diagram_registry[diagram_class]()
                    diagram.draw(
                        incoming=incoming,
                        outgoing=outgoing[:2],  # First two are outgoing particles
                        vec_bosons=vec_bosons,  # Vector bosons input separately
                        fused=fused,            # Fused particle
                        arrow_incoming1=incoming[0] in io_arrows,
                        arrow_incoming2=incoming[1] in io_arrows,
                        arrow_outgoing1=outgoing[0] in io_arrows,
                        arrow_outgoing2=outgoing[1] in io_arrows,
                        arrow_fused=arrow_fused,  # Pass the correct value for the fused particle arrow
                        arrow_vec1=vec_bosons[0] in vec_arrows,  # Check if vec1 needs an arrow
                        arrow_vec2=vec_bosons[1] in vec_arrows,  # Check if vec2 needs an arrow
                        output_filename=output_filename
                    )
        else:
            print(f"Diagram class '{diagram_class}' not recognized.")

if __name__ == "__main__":
    get_user_input()
