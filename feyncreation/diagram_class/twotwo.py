from feyncreation.common.diagram_base import LabeledVertex, should_have_arrow
from feynman import Diagram
import matplotlib.pyplot as plt
from feyncreation.common.particles import particle_dict, particle_styles

class SChannel:
    """S-channel diagram for twotwo process."""
    def draw(self, incoming, outgoing, mediator, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, arrow_mediator=False, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.3, .5))  # No label for internal vertices
        v2 = LabeledVertex(xy=(.7, .5))
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.08)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.08)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        v2.draw(ax)
        out1.draw(ax)
        out2.draw(ax)

        # Ensure case-insensitive matching and default styles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])  # Default to fermion style
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])

        # Add lines between vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v1, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)

        # Mediator line (horizontal)
        diagram.line(v1, v2, **particle_styles.get(mediator.lower(), particle_styles['g']), arrow=arrow_mediator, lw=2)

        # Outgoing lines
        diagram.line(v2, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v2, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)

        # Mediator label
        mediator_label = particle_dict.get(mediator.lower(), mediator)
        ax.text(v1.xy[0] + 0.2, v1.xy[1] + 0.11, mediator_label, fontsize=15)

        # Set manual axis limits to ensure space for labels
        ax.set_xlim(0, 1.1)  # Extend the axis a bit to give space for labels
        ax.set_ylim(0, 1.1)

        # Plot the diagram
        diagram.plot()

        # Use tight_layout with padding
        plt.tight_layout(pad=2.0)

        # Save the diagram as a PNG file with dpi=300
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()


class TChannel:
    """T-channel diagram for twotwo process."""
    def draw(self, incoming, outgoing, mediator, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, arrow_mediator=False, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.5, .8))  # No label for internal vertices
        v2 = LabeledVertex(xy=(.5, .2))
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.08)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.08)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        v2.draw(ax)
        out1.draw(ax)
        out2.draw(ax)

        # Ensure case-insensitive matching and default styles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])  # Default to fermion style
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])

        # Add lines between vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v2, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)

        # Mediator line (vertical)
        diagram.line(v1, v2, **particle_styles.get(mediator.lower(), particle_styles['g']), arrow=arrow_mediator, lw=2)

        # Outgoing lines
        diagram.line(v1, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v2, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)

        # Mediator label
        mediator_label = particle_dict.get(mediator.lower(), mediator)
        ax.text(v1.xy[0] + 0.1, v1.xy[1] - 0.3, mediator_label, fontsize=15)

        # Set manual axis limits to ensure space for labels
        ax.set_xlim(0, 1.1)  # Extend the axis a bit to give space for labels
        ax.set_ylim(0, 1.1)

        # Plot the diagram
        diagram.plot()

        # Use tight_layout with padding
        plt.tight_layout(pad=2.0)

        # Save the diagram as a PNG file with dpi=300
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()

class FourPoint:
    """Four-particle vertex (4-point) diagram for twotwo process without a mediator."""
    def draw(self, incoming, outgoing, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.5, .5))  # Central vertex for 4-particle interaction
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.08)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.08)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        out1.draw(ax)
        out2.draw(ax)

        # Ensure case-insensitive matching and default styles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])  # Default to fermion style
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])

        # Add lines between vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v1, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)

        # Outgoing lines
        diagram.line(v1, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v1, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)

        # Set manual axis limits to ensure space for labels
        ax.set_xlim(0, 1.1)  # Extend the axis a bit to give space for labels
        ax.set_ylim(0, 1.1)

        # Plot the diagram
        diagram.plot()

        # Use tight_layout with padding
        plt.tight_layout(pad=2.0)

        # Save the diagram as a PNG file with dpi=300
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()