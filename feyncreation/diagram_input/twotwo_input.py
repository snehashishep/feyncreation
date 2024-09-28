from feyncreation.diagram_class import twotwo
from feyncreation.common.utils import parse_process

def handle_twotwo_card(input_data):
    """Handles twotwo diagram based on input card."""
    channel_type = input_data.get('channel_type', 's-channel')
    process_str = input_data.get('process', '')
    io_arrows = input_data.get('io_arrows', '').split()
    
    incoming, outgoing, _ = parse_process(process_str)
    
    mediator = None
    med_arrow = False
    if channel_type != 'four-point':
        mediator = input_data.get('mediator', '').strip()
        med_arrow = input_data.get('med_arrow', 'false') == 'true'
    
    output_filename = input_data.get('output_filename', 'twotwo_diagram')
    
    diagram = twotwo.SChannel() if channel_type == 's-channel' else twotwo.TChannel() if channel_type == 't-channel' else twotwo.FourPoint()
    if channel_type == 'four-point':
        diagram.draw(
            incoming=incoming,
            outgoing=outgoing,
            arrow_incoming1=incoming[0] in io_arrows,
            arrow_incoming2=incoming[1] in io_arrows,
            arrow_outgoing1=outgoing[0] in io_arrows,
            arrow_outgoing2=outgoing[1] in io_arrows,
            output_filename=output_filename
        )
    else:
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

def handle_twotwo_input():
    """Handles input for twotwo diagrams."""
    channel_type = input("Choose channel type (s-channel/t-channel/four-point): ").lower()
    process_str = input("Enter the process (e.g., 'q qbar > t tbar'): ").strip()
    incoming, outgoing, _ = parse_process(process_str)

    if incoming and outgoing:
        io_arrows = input("Which incoming/outgoing particles do you want arrows? (e.g., 'q qbar'): ").strip().split()
        mediator = None
        if channel_type != 'four-point':
            mediator = input("Enter the mediator: ").strip().lower()
        med_arrow = input("Do you want a mediator arrow? (true/false): ").lower() == 'true' if mediator else False
        output_filename = input("Enter the output filename (without extension): ").strip()

        diagram = twotwo.SChannel() if channel_type == 's-channel' else twotwo.TChannel() if channel_type == 't-channel' else twotwo.FourPoint()
        if channel_type == 'four-point':
            diagram.draw(
                incoming=incoming,
                outgoing=outgoing,
                arrow_incoming1=incoming[0] in io_arrows,
                arrow_incoming2=incoming[1] in io_arrows,
                arrow_outgoing1=outgoing[0] in io_arrows,
                arrow_outgoing2=outgoing[1] in io_arrows,
                output_filename=output_filename
            )
        else:
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
