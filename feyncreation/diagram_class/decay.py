from feyncreation.common.diagram_base import LabeledVertex, should_have_arrow
from feynman import Diagram
import matplotlib.pyplot as plt
from feyncreation.common.particles import particle_dict, particle_styles

class DecayTwoBody:
    """Class for 2-body decay diagrams."""
    def draw(self, incoming, outgoing, arrow_incoming, arrow_outgoing1, arrow_outgoing2, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Define vertices
        in1 = LabeledVertex(xy=(.1, .5), label=particle_dict.get(incoming.lower(), incoming), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.5, .5), label='')
        out1 = LabeledVertex(xy=(.8, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.07)
        out2 = LabeledVertex(xy=(.8, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.07)

        diagram.vertices = [in1, v1, out1, out2]

        # Get styles based on particles
        in1_style = particle_styles.get(incoming.lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])

        # Draw lines with arrows if needed
        diagram.line(in1, v1, lw=2, **in1_style, arrow=arrow_incoming)
        diagram.line(v1, out1, lw=2, **out1_style, arrow=arrow_outgoing1)
        diagram.line(v1, out2, lw=2, **out2_style, arrow=arrow_outgoing2)

        diagram.plot()
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()

class DecayThreeBody:
    """Class for 3-body decay diagrams."""
    def draw(self, incoming, outgoing, offshell, offshell_label, arrow_incoming, arrow_outgoing1, arrow_outgoing2, arrow_outgoing3, arrow_offshell, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Define vertices
        in1 = LabeledVertex(xy=(.1, .5), label=particle_dict.get(incoming.lower(), incoming), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.4, .5), label='')
        v2 = LabeledVertex(xy=(.6, .3), label='')
        out1 = LabeledVertex(xy=(.8, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.05)
        out2 = LabeledVertex(xy=(.8, .45), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.05)
        out3 = LabeledVertex(xy=(.8, .15), label=particle_dict.get(outgoing[2].lower(), outgoing[2]), xoffset=0.05)

        diagram.vertices = [in1, v1, v2, out1, out2, out3]

        # Get styles based on particles
        in1_style = particle_styles.get(incoming.lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])
        out3_style = particle_styles.get(outgoing[2].lower(), particle_styles['fermion'])
        offshell_style = particle_styles.get(offshell.lower(), particle_styles['w+'])

        # Draw lines with arrows if needed
        diagram.line(in1, v1, lw=2, **in1_style, arrow=arrow_incoming)
        diagram.line(v1, v2, lw=2, **offshell_style, arrow=arrow_offshell)
        diagram.line(v1, out1, lw=2, **out1_style, arrow=arrow_outgoing1)
        diagram.line(v2, out2, lw=2, **out2_style, arrow=arrow_outgoing2)
        diagram.line(v2, out3, lw=2, **out3_style, arrow=arrow_outgoing3)

        diagram.text(v1.xy[0], v1.xy[1] - 0.15, offshell_label, fontsize=15)

        diagram.plot()
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()

class DecayTriangle:
    """Class for triangle diagrams."""
    def draw(self, incoming, outgoing, triangle_arms, arrow_incoming, arrow_outgoing1, arrow_outgoing2, arrow_t1, arrow_t2, arrow_t3, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Define vertices
        in1 = LabeledVertex(xy=(.1, .5), label=particle_dict.get(incoming.lower(), incoming), xoffset=-0.05)
        t1 = LabeledVertex(xy=(.3, .5), label='')
        t2 = LabeledVertex(xy=(.6, .75), label='')
        t3 = LabeledVertex(xy=(.6, .25), label='')
        out1 = LabeledVertex(xy=(.9, .75), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.05)
        out2 = LabeledVertex(xy=(.9, .25), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.05)

        diagram.vertices = [in1, t1, t2, t3, out1, out2]

        # Get styles based on particles
        in1_style = particle_styles.get(incoming.lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['w+'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['w+'])
        t1_style = particle_styles.get(triangle_arms[0].lower(), particle_styles['fermion'])
        t2_style = particle_styles.get(triangle_arms[1].lower(), particle_styles['fermion'])
        t3_style = particle_styles.get(triangle_arms[2].lower(), particle_styles['fermion'])

        # Draw lines with arrows if needed
        diagram.line(in1, t1, lw=2, **in1_style, arrow=arrow_incoming)
        diagram.line(t1, t2, lw=2, **t1_style, arrow=arrow_t1)
        diagram.line(t2, t3, lw=2, **t2_style, arrow=arrow_t2)
        diagram.line(t3, t1, lw=2, **t3_style, arrow=arrow_t3)
        diagram.line(t2, out1, lw=2, **out1_style, arrow=arrow_outgoing1)
        diagram.line(t3, out2, lw=2, **out2_style, arrow=arrow_outgoing2)

        diagram.text(0.4, 0.7, particle_dict.get(triangle_arms[0].lower(), triangle_arms[0]), fontsize=15)
        diagram.text(0.7, 0.52, particle_dict.get(triangle_arms[1].lower(), triangle_arms[1]), fontsize=15)
        diagram.text(0.4, 0.3, particle_dict.get(triangle_arms[2].lower(), triangle_arms[2]), fontsize=15)

        diagram.plot()
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()
