from feyncreation.diagram_class.vbf1 import VBF1
from feyncreation.common import config
import os

# Define input for VBF1 diagram
incoming = ['mu+', 'mu-']
outgoing = ['vm', 'vmbar', 'h']
vec_bosons = ['w+', 'w-']
io_arrows = ['mu+', 'mu-']
vec_arrows = []  # No arrows for vector bosons

# Create the VBF1 diagram
diagram = VBF1()
diagram.draw(
    incoming=incoming,
    outgoing=outgoing[:2],
    vec_bosons=vec_bosons,
    fused='h',
    arrow_incoming1=incoming[0] in io_arrows,
    arrow_incoming2=incoming[1] in io_arrows,
    arrow_outgoing1=outgoing[0] in io_arrows,
    arrow_outgoing2=outgoing[1] in io_arrows,
    arrow_fused='h' in io_arrows,
    arrow_vec1=vec_bosons[0] in vec_arrows,
    arrow_vec2=vec_bosons[1] in vec_arrows,
    output_filename="vbf_diagram"
)
