from feyncreation.diagram_class import vbf1
from feyncreation.common.utils import parse_process

def handle_vbf1_card(input_data):
    """Handles vbf1 diagram based on input card."""
    process_str = input_data.get('process', '')
    io_arrows = input_data.get('io_arrows', '').split()
    vec_arrows = input_data.get('vec_arrows', '').split()
    
    incoming, outgoing, fused = parse_process(process_str)
    vec_bosons = input_data.get('vec_bosons', '').split()
    
    # Assuming 'fused' is a list but should only contain one particle for VBF1
    fused_particle = fused[0] if fused else None
    arrow_fused = fused_particle in io_arrows  # Check if fused particle needs an arrow
    
    output_filename = input_data.get('output_filename', 'vbf1_diagram')
    
    diagram = vbf1.VBF1()
    diagram.draw(
        incoming=incoming,
        outgoing=outgoing[:2],  # First two are outgoing particles
        vec_bosons=vec_bosons,  # Vector bosons input separately
        fused=fused_particle,   # Use only the first fused particle
        arrow_incoming1=incoming[0] in io_arrows,
        arrow_incoming2=incoming[1] in io_arrows,
        arrow_outgoing1=outgoing[0] in io_arrows,
        arrow_outgoing2=outgoing[1] in io_arrows,
        arrow_fused=arrow_fused,  # Pass the correct value for the fused particle arrow
        arrow_vec1=vec_bosons[0] in vec_arrows,  # Check if vec1 needs an arrow
        arrow_vec2=vec_bosons[1] in vec_arrows,  # Check if vec2 needs an arrow
        output_filename=output_filename
    )

def handle_vbf1_input():
    """Handles input for vbf1 diagrams."""
    process_str = input("Enter the process (e.g., 'mu+ mu- > vm vmbar h'): ").strip()
    incoming, outgoing, fused = parse_process(process_str)

    if incoming and outgoing and fused:
        vec_bosons = input("Enter vec1 and vec2 (e.g., 'z gamma'): ").strip().split()
        io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'mu+ mu- vm vmbar'): ").strip().split()
        vec_arrows = input("Which vector bosons do you want arrows? (e.g., 'vec1 vec2' or 'none'): ").strip().split()

        if "none" in vec_arrows:
            vec_arrows = []  # No arrows for vec1 and vec2 if 'none' is specified
        arrow_fused = fused[0] in io_arrows  # Check if fused particle needs an arrow
        output_filename = input("Enter the output filename (without extension): ").strip()

        diagram = vbf1.VBF1()
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
