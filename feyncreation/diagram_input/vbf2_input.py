from feyncreation.diagram_class import vbf2
from feyncreation.common.utils import parse_process

def handle_vbf2_card(input_data):
    """Handles vbf2 diagram based on input card."""
    vbf2_type = input_data.get('vbf2_type', 'four-point')
    process_str = input_data.get('process', '')
    io_arrows = input_data.get('io_arrows', '').split()
    vec_arrows = input_data.get('vec_arrows', '').split()

    incoming, outgoing, fused = parse_process(process_str)
    vec_bosons = input_data.get('vec_bosons', '').split()
    arrow_fused1 = input_data.get('arrow_fused1', 'false') == 'true'
    arrow_fused2 = input_data.get('arrow_fused2', 'false') == 'true'
    
    mediator = None
    arrow_mediator = False
    if vbf2_type != 'four-point':
        mediator = input_data.get('mediator', '').strip()
        arrow_mediator = input_data.get('arrow_mediator', 'false') == 'true'
    
    output_filename = input_data.get('output_filename', 'vbf2_diagram')

    if vbf2_type == 'four-point':
        diagram = vbf2.VBF2FourPoint()
        diagram.draw(
            incoming=incoming,
            outgoing=outgoing,  # First two are outgoing particles
            fused=fused,        # Automatically read fused particles
            vec_bosons=vec_bosons,  # Vector bosons input separately
            arrow_incoming1=incoming[0] in io_arrows,
            arrow_incoming2=incoming[1] in io_arrows,
            arrow_outgoing1=outgoing[0] in io_arrows,
            arrow_outgoing2=outgoing[1] in io_arrows,
            arrow_vec1=vec_bosons[0] in vec_arrows,
            arrow_vec2=vec_bosons[1] in vec_arrows,
            arrow_fused1=arrow_fused1,
            arrow_fused2=arrow_fused2,
            output_filename=output_filename
        )
    else:
        diagram_class = vbf2.VBF2SChannel if vbf2_type == 's-channel' else vbf2.VBF2TChannel
        diagram = diagram_class()
        diagram.draw(
            incoming=incoming,
            outgoing=outgoing,  # First two are outgoing particles
            fused=fused,        # Automatically read fused particles
            vec_bosons=vec_bosons,
            mediator=mediator,
            arrow_incoming1=incoming[0] in io_arrows,
            arrow_incoming2=incoming[1] in io_arrows,
            arrow_outgoing1=outgoing[0] in io_arrows,
            arrow_outgoing2=outgoing[1] in io_arrows,
            arrow_vec1=vec_bosons[0] in vec_arrows,
            arrow_vec2=vec_bosons[1] in vec_arrows,
            arrow_fused1=arrow_fused1,
            arrow_fused2=arrow_fused2,
            arrow_mediator=arrow_mediator,
            output_filename=output_filename
        )

def handle_vbf2_input():
    """Handles input for vbf2 diagrams."""
    vbf2_type = input("Choose VBF2 type (four-point/s-channel/t-channel): ").lower()
    process_str = input("Enter the process (e.g., 'in1 in2 > out1 out2 fused1 fused2'): ").strip()
    incoming, outgoing, fused = parse_process(process_str)

    if incoming and outgoing and fused:
        vec_bosons = input("Enter vec1 and vec2 (e.g., 'z gamma'): ").strip().split()
        io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'in1 in2 out1 out2'): ").strip().split()
        vec_arrows = input("Which vector bosons do you want arrows? (e.g., 'vec1 vec2' or 'none'): ").strip().split()

        if "none" in vec_arrows:
            vec_arrows = []  # No arrows for vec1 and vec2 if 'none' is specified
        fused_arrows = input("Which fused particles do you want arrows? (e.g., 'fused1 fused2'): ").strip().split()
        arrow_fused1 = 'fused1' in fused_arrows
        arrow_fused2 = 'fused2' in fused_arrows

        # If not four-point, ask for the mediator
        if vbf2_type != 'four-point':
            mediator = input("Enter the mediator: ").strip().lower()
            arrow_mediator = input("Do you want an arrow on the mediator? (true/false): ").lower() == 'true'

        # Ask for output filename after mediator inputs
        output_filename = input("Enter the output filename (without extension): ").strip()

        if vbf2_type == 'four-point':
            diagram = vbf2.VBF2FourPoint()
            diagram.draw(
                incoming=incoming,
                outgoing=outgoing,  # First two are outgoing particles
                fused=fused,        # Automatically read fused particles
                vec_bosons=vec_bosons,  # Vector bosons input separately
                arrow_incoming1=incoming[0] in io_arrows,
                arrow_incoming2=incoming[1] in io_arrows,
                arrow_outgoing1=outgoing[0] in io_arrows,
                arrow_outgoing2=outgoing[1] in io_arrows,
                arrow_vec1=vec_bosons[0] in vec_arrows,
                arrow_vec2=vec_bosons[1] in vec_arrows,
                arrow_fused1=arrow_fused1,
                arrow_fused2=arrow_fused2,
                output_filename=output_filename
            )
        else:
            diagram_class = vbf2.VBF2SChannel if vbf2_type == 's-channel' else vbf2.VBF2TChannel
            diagram = diagram_class()
            diagram.draw(
                incoming=incoming,
                outgoing=outgoing,  # First two are outgoing particles
                fused=fused,        # Automatically read fused particles
                vec_bosons=vec_bosons,
                mediator=mediator,
                arrow_incoming1=incoming[0] in io_arrows,
                arrow_incoming2=incoming[1] in io_arrows,
                arrow_outgoing1=outgoing[0] in io_arrows,
                arrow_outgoing2=outgoing[1] in io_arrows,
                arrow_vec1=vec_bosons[0] in vec_arrows,
                arrow_vec2=vec_bosons[1] in vec_arrows,
                arrow_fused1=arrow_fused1,
                arrow_fused2=arrow_fused2,
                arrow_mediator=arrow_mediator,
                output_filename=output_filename
            )
