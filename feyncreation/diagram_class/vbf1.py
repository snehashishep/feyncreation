# vbf1.py
from feyncreation.common.diagram_base import LabeledVertex, should_have_arrow
from feynman import Diagram
import matplotlib.pyplot as plt
from feyncreation.common.particles import particle_dict, particle_styles

class VBF1:
    """VBF1 diagram for vector boson fusion process."""
    def draw(self, incoming, outgoing, vec_bosons, fused, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, arrow_fused=False, arrow_vec1=False, arrow_vec2=False, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.4, .8), label='')
        v2 = LabeledVertex(xy=(.4, .2), label='')
        v3 = LabeledVertex(xy=(.6, .5), label='')  # Intermediate vertex
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.05)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.05)
        midout1 = LabeledVertex(xy=(.9, .5), label=particle_dict.get(fused.lower(), fused), xoffset=0.05)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        v2.draw(ax)
        v3.draw(ax)
        out1.draw(ax)
        out2.draw(ax)
        midout1.draw(ax)

        # Ensure case-insensitive matching and default styles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])  # Default to fermion style
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])
        vec1_style = particle_styles.get(vec_bosons[0].lower(), particle_styles['w+'])
        vec2_style = particle_styles.get(vec_bosons[1].lower(), particle_styles['w+'])
        fused_style = particle_styles.get(fused.lower(), dict(style='-', dashes=[5, 2]))  # Default fused particle style

        # Add lines between vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v2, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)

        # Vector bosons (wiggly lines)
        diagram.line(v1, v3, **vec1_style, lw=2)
        diagram.line(v2, v3, **vec2_style, lw=2)

        # Fused particle from boson fusion (dashed line)
        # Draw vec1, vec2, and fused lines
        diagram.line(v1, v3, **vec1_style, arrow=arrow_vec1, lw=2)
        diagram.line(v2, v3, **vec2_style, arrow=arrow_vec2, lw=2)
        diagram.line(v3, midout1, **fused_style, arrow=arrow_fused, lw=2)

        # Outgoing particles
        diagram.line(v1, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v2, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)

        # Add labels for vector bosons and fused particle
        vec1_label = particle_dict.get(vec_bosons[0].lower(), vec_bosons[0])
        vec2_label = particle_dict.get(vec_bosons[1].lower(), vec_bosons[1])
        fused_label = particle_dict.get(fused.lower(), fused)

        ax.text(v3.xy[0], v3.xy[1] + 0.13, vec1_label, fontsize=15)
        ax.text(v3.xy[0], v3.xy[1] - 0.15, vec2_label, fontsize=15)

        # Plot the diagram
        diagram.plot()

        # Use tight_layout with padding
        plt.tight_layout(pad=2.0)

        # Save the diagram as a PNG file with dpi=300
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()






