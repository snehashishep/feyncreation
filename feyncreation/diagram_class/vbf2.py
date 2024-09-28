from feyncreation.common.diagram_base import LabeledVertex, should_have_arrow
from feynman import Diagram
import matplotlib.pyplot as plt
from feyncreation.common.particles import particle_dict, particle_styles

class VBF2FourPoint:
    """Four-point diagram for vbf2 process."""
    def draw(self, incoming, outgoing, fused, vec_bosons, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, arrow_fused1=False, arrow_fused2=False, arrow_vec1=False, arrow_vec2=False, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.4, .8), label='')
        v2 = LabeledVertex(xy=(.4, .2), label='')
        v3 = LabeledVertex(xy=(.6, .5), label='')
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.05)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.05)
        fused1_out = LabeledVertex(xy=(.9, .65), label=particle_dict.get(fused[0].lower(), fused[0]), xoffset=0.05)
        fused2_out = LabeledVertex(xy=(.9, .35), label=particle_dict.get(fused[1].lower(), fused[1]), xoffset=0.05)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        v2.draw(ax)
        v3.draw(ax)
        out1.draw(ax)
        out2.draw(ax)
        fused1_out.draw(ax)
        fused2_out.draw(ax)

        # Add styles for particles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])
        fused1_style = particle_styles.get(fused[0].lower(), dict(style='-', dashes=[5, 2]))
        fused2_style = particle_styles.get(fused[1].lower(), dict(style='-', dashes=[5, 2]))
        vec1_style = particle_styles.get(vec_bosons[0].lower(), particle_styles['w+'])
        vec2_style = particle_styles.get(vec_bosons[1].lower(), particle_styles['w+'])

        # Draw the lines between the vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v2, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)
        diagram.line(v1, v3, **vec1_style, arrow=arrow_vec1, lw=2)
        diagram.line(v2, v3, **vec2_style, arrow=arrow_vec2, lw=2)
        diagram.line(v3, fused1_out, **fused1_style, arrow=arrow_fused1, lw=2)
        diagram.line(v3, fused2_out, **fused2_style, arrow=arrow_fused2, lw=2)
        diagram.line(v1, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v2, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)


        # Add labels for vector bosons and fused particle
        vec1_label = particle_dict.get(vec_bosons[0].lower(), vec_bosons[0])
        vec2_label = particle_dict.get(vec_bosons[1].lower(), vec_bosons[1])
        

        diagram.text(v3.xy[0]+0.02, v3.xy[1] + 0.13, vec1_label, fontsize=15)
        diagram.text(v3.xy[0]+0.02, v3.xy[1] - 0.15, vec2_label, fontsize=15)

        # Plot the diagram
        diagram.plot()
        plt.tight_layout(pad=2.0)
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()

class VBF2SChannel:
    """S-channel diagram for vbf2 process."""
    def draw(self, incoming, outgoing, fused, vec_bosons, mediator, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, arrow_fused1=False, arrow_fused2=False, arrow_vec1=False, arrow_vec2=False, arrow_mediator=False, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.25, .8), label='')
        v2 = LabeledVertex(xy=(.25, .2), label='')
        v3 = LabeledVertex(xy=(.4, .5), label='')
        v4 = LabeledVertex(xy=(.7, .5), label='')
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.05)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.05)
        fused1_out = LabeledVertex(xy=(.9, .65), label=particle_dict.get(fused[0].lower(), fused[0]), xoffset=0.05)
        fused2_out = LabeledVertex(xy=(.9, .35), label=particle_dict.get(fused[1].lower(), fused[1]), xoffset=0.05)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        v2.draw(ax)
        v3.draw(ax)
        v4.draw(ax)
        out1.draw(ax)
        out2.draw(ax)
        fused1_out.draw(ax)
        fused2_out.draw(ax)

        # Add styles for particles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])
        fused1_style = particle_styles.get(fused[0].lower(), dict(style='-', dashes=[5, 2]))
        fused2_style = particle_styles.get(fused[1].lower(), dict(style='-', dashes=[5, 2]))
        vec1_style = particle_styles.get(vec_bosons[0].lower(), particle_styles['w+'])
        vec2_style = particle_styles.get(vec_bosons[1].lower(), particle_styles['w+'])
        mediator_style = particle_styles.get(mediator.lower(), particle_styles['w+'])

        # Draw the lines between the vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v2, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)
        diagram.line(v1, v3, **vec1_style, arrow=arrow_vec1, lw=2)
        diagram.line(v2, v3, **vec2_style, arrow=arrow_vec2, lw=2)
        diagram.line(v3, v4, **mediator_style, arrow=arrow_mediator, lw=2)
        diagram.line(v4, fused1_out, **fused1_style, arrow=arrow_fused1, lw=2)
        diagram.line(v4, fused2_out, **fused2_style, arrow=arrow_fused2, lw=2)
        diagram.line(v1, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v2, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)

        # Add labels for vector bosons and fused particle
        vec1_label = particle_dict.get(vec_bosons[0].lower(), vec_bosons[0])
        vec2_label = particle_dict.get(vec_bosons[1].lower(), vec_bosons[1])
        mediator_label = particle_dict.get(mediator.lower(), mediator)
        

        diagram.text(v3.xy[0]+0.01, v3.xy[1] + 0.13, vec1_label, fontsize=15)
        diagram.text(v3.xy[0]+0.01, v3.xy[1] - 0.15, vec2_label, fontsize=15)
        diagram.text(v3.xy[0]+0.13, v3.xy[1] +0.07, mediator_label, fontsize=15)

        # Plot the diagram
        diagram.plot()
        plt.tight_layout(pad=2.0)
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()


class VBF2TChannel:
    """T-channel diagram for vbf2 process."""
    def draw(self, incoming, outgoing, fused, vec_bosons, mediator, arrow_incoming1=True, arrow_incoming2=True, arrow_outgoing1=True, arrow_outgoing2=True, arrow_fused1=False, arrow_fused2=False, arrow_vec1=False, arrow_vec2=False, arrow_mediator=False, output_filename="output"):
        plt.close('all')
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)

        diagram = Diagram(ax)

        # Create labeled vertices with small offsets
        in1 = LabeledVertex(xy=(.1, .8), label=particle_dict.get(incoming[0].lower(), incoming[0]), xoffset=-0.05)
        in2 = LabeledVertex(xy=(.1, .2), label=particle_dict.get(incoming[1].lower(), incoming[1]), xoffset=-0.05)
        v1 = LabeledVertex(xy=(.3, .8), label='')
        v2 = LabeledVertex(xy=(.3, .2), label='')
        v3 = LabeledVertex(xy=(.5, .6), label='')
        v4 = LabeledVertex(xy=(.5, .4), label='')
        out1 = LabeledVertex(xy=(.9, .8), label=particle_dict.get(outgoing[0].lower(), outgoing[0]), xoffset=0.05)
        out2 = LabeledVertex(xy=(.9, .2), label=particle_dict.get(outgoing[1].lower(), outgoing[1]), xoffset=0.05)
        fused1_out = LabeledVertex(xy=(.9, .65), label=particle_dict.get(fused[0].lower(), fused[0]), xoffset=0.05)
        fused2_out = LabeledVertex(xy=(.9, .35), label=particle_dict.get(fused[1].lower(), fused[1]), xoffset=0.05)

        # Draw the vertices and labels
        in1.draw(ax)
        in2.draw(ax)
        v1.draw(ax)
        v2.draw(ax)
        v3.draw(ax)
        v4.draw(ax)
        out1.draw(ax)
        out2.draw(ax)
        fused1_out.draw(ax)
        fused2_out.draw(ax)

        # Add styles for particles
        in1_style = particle_styles.get(incoming[0].lower(), particle_styles['fermion'])
        in2_style = particle_styles.get(incoming[1].lower(), particle_styles['fermion'])
        out1_style = particle_styles.get(outgoing[0].lower(), particle_styles['fermion'])
        out2_style = particle_styles.get(outgoing[1].lower(), particle_styles['fermion'])
        fused1_style = particle_styles.get(fused[0].lower(), dict(style='-', dashes=[5, 2]))
        fused2_style = particle_styles.get(fused[1].lower(), dict(style='-', dashes=[5, 2]))
        vec1_style = particle_styles.get(vec_bosons[0].lower(), particle_styles['w+'])
        vec2_style = particle_styles.get(vec_bosons[1].lower(), particle_styles['w+'])
        mediator_style = particle_styles.get(mediator.lower(), particle_styles['w+'])

        # Draw the lines between the vertices
        diagram.line(in1, v1, **in1_style, arrow=should_have_arrow(incoming[0].lower(), arrow_incoming1), lw=2)
        diagram.line(in2, v2, **in2_style, arrow=should_have_arrow(incoming[1].lower(), arrow_incoming2), lw=2)
        diagram.line(v1, v3, **vec1_style, arrow=arrow_vec1, lw=2)
        diagram.line(v2, v4, **vec2_style, arrow=arrow_vec2, lw=2)
        diagram.line(v3, v4, **mediator_style, arrow=arrow_mediator, lw=2)
        diagram.line(v3, fused1_out, **fused1_style, arrow=arrow_fused1, lw=2)
        diagram.line(v4, fused2_out, **fused2_style, arrow=arrow_fused2, lw=2)
        diagram.line(v1, out1, **out1_style, arrow=should_have_arrow(outgoing[0].lower(), arrow_outgoing1), lw=2)
        diagram.line(v2, out2, **out2_style, arrow=should_have_arrow(outgoing[1].lower(), arrow_outgoing2), lw=2)

        # Add labels for vector bosons and fused particle
        vec1_label = particle_dict.get(vec_bosons[0].lower(), vec_bosons[0])
        vec2_label = particle_dict.get(vec_bosons[1].lower(), vec_bosons[1])
        mediator_label = particle_dict.get(mediator.lower(), mediator)
        

        diagram.text(v3.xy[0], v3.xy[1] + 0.1, vec1_label, fontsize=15)
        diagram.text(v4.xy[0]+0.02, v4.xy[1] - 0.12, vec2_label, fontsize=15)
        diagram.text(v3.xy[0]+0.1, v3.xy[1] - 0.1, mediator_label, fontsize=15)

        # Plot the diagram
        diagram.plot()
        plt.tight_layout(pad=2.0)
        plt.savefig(f"{output_filename}.png", dpi=300)
        plt.show()
