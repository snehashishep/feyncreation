# diagram_base.py
from feynman import Vertex
import matplotlib.pyplot as plt

# class LabeledVertex(Vertex):  # Inherit from feynman.Vertex
#     def __init__(self, xy, label='', xoffset=0, yoffset=0, marker='', markersize=6, color='black'):
#         super().__init__(xy)  # Call parent constructor
#         self.label = label
#         self.xoffset = xoffset
#         self.yoffset = yoffset
#         self.marker = marker
#         self.markersize = markersize
#         self.color = color

#     def draw(self, ax):
#         super().draw(ax)  # Draw the base vertex
        
#         # Add text label at the vertex location with custom offset
#         if self.label:
#             ax.text(self.xy[0] + self.xoffset, self.xy[1] + self.yoffset, self.label, fontsize=15, ha='center', va='center')

class LabeledVertex(Vertex):
    def __init__(self, xy, label='', xoffset=0, yoffset=0, marker='', markersize=6, color='black'):
        super().__init__(xy=xy, marker=marker, markersize=markersize, color=color)
        self.label = label
        self.xoffset = xoffset
        self.yoffset = yoffset

    def draw(self, ax):
        super().draw(ax)
        if self.label:
            ax.text(self.xy[0] + self.xoffset, self.xy[1] + self.yoffset, self.label, fontsize=15, ha='center', va='center')



def should_have_arrow(particle, arrow_choice):
    from .particles import arrow_particles
    if particle in arrow_particles:
        return arrow_choice
    return False