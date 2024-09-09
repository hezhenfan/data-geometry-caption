from manim import *
import math
import random
from manim.camera.camera import Camera
# manim -p -ql --save_last_frame -o 1.png triangle.py IsoscelesTriangleWithDetails


class ParallelogramWithDetails(Scene):
    def construct(self):
        # Define the vertices of the parallelogram
        A = [-3, -1, 0]  # Coordinates for A
        B = [1, -1, 0]   # Coordinates for B
        C = [3, 1, 0]    # Coordinates for C
        D = [-1, 1, 0]   # Coordinates for D

        # Create points
        point_A = Dot(A, color=BLUE)
        point_B = Dot(B, color=BLUE)
        point_C = Dot(C, color=BLUE)
        point_D = Dot(D, color=BLUE)

        # Create labels for points
        label_A = MathTex("A(-3, -1)").next_to(point_A, DOWN)
        label_B = MathTex("B(1, -1)").next_to(point_B, DOWN)
        label_C = MathTex("C(3, 1)").next_to(point_C, UP)
        label_D = MathTex("D(-1, 1)").next_to(point_D, UP)

        # Create lines between points
        line_AB = Line(A, B)
        line_BC = Line(B, C)
        line_CD = Line(C, D)
        line_DA = Line(D, A)

        # Create edge lengths
        length_AB = MathTex("4").next_to(line_AB, DOWN)
        length_BC = MathTex("2\\sqrt{5}").next_to(line_BC, RIGHT)
        length_CD = MathTex("4").next_to(line_CD, UP)
        length_DA = MathTex("2\\sqrt{5}").next_to(line_DA, LEFT)

        # Draw the parallelogram, labels, and edge lengths at once
        self.add(point_A, point_B, point_C, point_D)
        self.add(label_A, label_B, label_C, label_D)
        self.add(line_AB, line_BC, line_CD, line_DA)
        self.add(length_AB, length_BC, length_CD, length_DA)

        # Wait for a moment at the end to keep everything displayed
        self.wait(2)
