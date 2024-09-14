from feyncreation.diagram_class.twotwo import SChannel, TChannel
from feyncreation.common import config
import os

# Define input 
incoming = ['q', 'qbar']
outgoing = ['t', 'tbar']
mediator = 'g'
io_arrows = ['q', 'qbar', 't', 'tbar']

# Create the S-channel diagram
diagram = SChannel() #TChannel()
diagram.draw(
    incoming=incoming,
    outgoing=outgoing,
    mediator=mediator,
    arrow_incoming1=incoming[0] in io_arrows,
    arrow_incoming2=incoming[1] in io_arrows,
    arrow_outgoing1=outgoing[0] in io_arrows,
    arrow_outgoing2=outgoing[1] in io_arrows,
    output_filename="twotwo_diagram"
)
