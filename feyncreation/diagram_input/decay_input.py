from feyncreation.diagram_class import decay
from feyncreation.common.utils import parse_process
from feyncreation.common.particles import particle_dict, particle_styles

def handle_decay_two_body_input():
    """Handles input for 2-body decay diagrams."""
    # Input for the process
    process_str = input("Enter the process (e.g., 'h > b bbar'): ").strip()
    incoming, outgoing, _ = parse_process(process_str)

    # Ask for arrow input
    io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'h b bbar'): ").strip().split()

    # Ask for output filename
    output_filename = input("Enter the output filename (without extension): ").strip()

    # Draw the 2-body decay diagram
    diagram = decay.DecayTwoBody()
    diagram.draw(
        incoming=incoming[0],  # Single incoming particle
        outgoing=outgoing,     # Two outgoing particles
        arrow_incoming=incoming[0] in io_arrows,
        arrow_outgoing1=outgoing[0] in io_arrows,
        arrow_outgoing2=outgoing[1] in io_arrows,
        output_filename=output_filename
    )

def handle_decay_three_body_input():
    """Handles input for 3-body decay diagrams."""
    process_str = input("Enter the process (e.g., 'n+ > n0 e+ ve'): ").strip()
    incoming, outgoing, _ = parse_process(process_str)

    offshell = input("Enter the offshell particle (e.g., 'w+'): ").strip()

    # Get the label from the particle dictionary for LaTeX rendering
    offshell_label = particle_dict.get(offshell.lower(), offshell)

    # Ask if the user wants a star (*) in the offshell particle label
    add_star = input("Do you want a star (*) in the label for the offshell particle? (yes/no): ").lower()
    if add_star == 'yes':
        # Append the star inside the LaTeX string
        offshell_label = offshell_label[:-1] + r'*$'

    # Use the original offshell particle for lookups, but use the modified label for display
    io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'n+ e+'): ").strip().split()
    arrow_offshell = input("Do you want an arrow on the offshell particle? (true/false): ").lower() == 'true'

    output_filename = input("Enter the output filename (without extension): ").strip()

    diagram = decay.DecayThreeBody()
    diagram.draw(
        incoming=incoming[0],  # Single incoming particle
        outgoing=outgoing,     # Three outgoing particles
        offshell=offshell,     # Use original offshell particle for internal logic
        offshell_label=offshell_label,  # Use modified label for LaTeX display
        arrow_incoming=incoming[0] in io_arrows,
        arrow_outgoing1=outgoing[0] in io_arrows,
        arrow_outgoing2=outgoing[1] in io_arrows,
        arrow_outgoing3=outgoing[2] in io_arrows,
        arrow_offshell=arrow_offshell,
        output_filename=output_filename
    )


def handle_decay_triangle_input():
    """Handles input for triangle decay diagrams."""
    # Input for the process
    process_str = input("Enter the process (e.g., 'h > gamma gamma'): ").strip()
    incoming, outgoing, _ = parse_process(process_str)

    # Ask for the triangle arms
    triangle_arms = input("Enter the triangle arms (e.g., 't t t'): ").strip().split()

    # Ask for arrow input
    io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'h gamma gamma'): ").strip().split()
    triangle_arrows = input("Which triangle particles do you want arrows? (e.g., 't t t'): ").strip().split()

    # Ask for output filename
    output_filename = input("Enter the output filename (without extension): ").strip()

    # Draw the triangle decay diagram
    diagram = decay.DecayTriangle()
    diagram.draw(
        incoming=incoming[0],  # Single incoming particle
        outgoing=outgoing,     # Two outgoing particles
        triangle_arms=triangle_arms,  # Three arms of the triangle
        arrow_incoming=incoming[0] in io_arrows,
        arrow_outgoing1=outgoing[0] in io_arrows,
        arrow_outgoing2=outgoing[1] in io_arrows,
        arrow_t1=triangle_arms[0] in triangle_arrows,
        arrow_t2=triangle_arms[1] in triangle_arrows,
        arrow_t3=triangle_arms[2] in triangle_arrows,
        output_filename=output_filename
    )
