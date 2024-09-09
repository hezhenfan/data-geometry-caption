from manim import *
# manim -p -ql test.py ParallelogramWithDetails

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


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



# class ParallelogramWithDetailsAndAngles(Scene):
#     def construct(self):
#         # Define the vertices of the parallelogram
#         A = [-3, -1, 0]  # Coordinates for A
#         B = [1, -1, 0]   # Coordinates for B
#         C = [3, 1, 0]    # Coordinates for C
#         D = [-1, 1, 0]   # Coordinates for D

#         # Create points
#         point_A = Dot(A, color=BLUE)
#         point_B = Dot(B, color=BLUE)
#         point_C = Dot(C, color=BLUE)
#         point_D = Dot(D, color=BLUE)

#         # Create labels for points
#         label_A = MathTex("A(-3, -1)").next_to(point_A, DOWN)
#         label_B = MathTex("B(1, -1)").next_to(point_B, DOWN)
#         label_C = MathTex("C(3, 1)").next_to(point_C, UP)
#         label_D = MathTex("D(-1, 1)").next_to(point_D, UP)

#         # Create lines between points
#         line_AB = Line(A, B)
#         line_BC = Line(B, C)
#         line_CD = Line(C, D)
#         line_DA = Line(D, A)

#         # Create edge lengths
#         length_AB = MathTex("4").next_to(line_AB, DOWN)
#         length_BC = MathTex("2\\sqrt{5}").next_to(line_BC, RIGHT)
#         length_CD = MathTex("4").next_to(line_CD, UP)
#         length_DA = MathTex("2\\sqrt{5}").next_to(line_DA, LEFT)

#         # Calculate and display angles (approximated for simplicity)
#         angle_A = MathTex("120^\\circ").next_to(A , np.array((1.0, 1.0, 0)))
#         angle_B = MathTex("60^\\circ").next_to(B , np.array((-1.0, 1.0, 0)))
#         angle_C = MathTex("120^\\circ").next_to(C , np.array((-1.0, -1.0, 0)))
#         angle_D = MathTex("60^\\circ").next_to(D , np.array((1.0, -1.0, 0)))
#         self.add(angle_A, angle_B, angle_C, angle_D)
#         # self.add(angle_A)
#         # Draw the parallelogram, labels, edge lengths, and angles at once
#         self.add(point_A, point_B, point_C, point_D)
#         self.add(label_A, label_B, label_C, label_D)
#         self.add(line_AB, line_BC, line_CD, line_DA)
#         self.add(length_AB, length_BC, length_CD, length_DA)


#         # Wait for a moment at the end to keep everything displayed
#         self.wait(2)

class ParallelogramWithDetailsAndAngles(Scene):
    def __init__(self, vertices, angles, edge_lengths, **kwargs):
        super().__init__(**kwargs)
        self.vertices = vertices
        self.angles = angles
        self.edge_lengths = edge_lengths

    def construct(self):
        A, B, C, D = self.vertices  # Unpack the vertex coordinates

        # Create points
        point_A = Dot(A, color=BLUE)
        point_B = Dot(B, color=BLUE)
        point_C = Dot(C, color=BLUE)
        point_D = Dot(D, color=BLUE)

        # Create labels for points
        label_A = MathTex(f"A({A[0]}, {A[1]})").next_to(point_A, DOWN)
        label_B = MathTex(f"B({B[0]}, {B[1]})").next_to(point_B, DOWN)
        label_C = MathTex(f"C({C[0]}, {C[1]})").next_to(point_C, UP)
        label_D = MathTex(f"D({D[0]}, {D[1]})").next_to(point_D, UP)

        # Create lines between points
        line_AB = Line(A, B)
        line_BC = Line(B, C)
        line_CD = Line(C, D)
        line_DA = Line(D, A)

        # Create edge lengths (values are passed as parameters)
        length_AB = MathTex(f"{self.edge_lengths[0]}").next_to(line_AB, DOWN)
        
        length_BC = MathTex(f"{self.edge_lengths[1]}").next_to(line_BC, RIGHT)
        length_CD = MathTex(f"{self.edge_lengths[2]}").next_to(line_CD, UP)
        length_DA = MathTex(f"{self.edge_lengths[3]}").next_to(line_DA, LEFT)

        # Create angles (values are passed as parameters)
        angle_A = MathTex(f"{self.angles[0]}^\\circ").next_to(A, np.array((1.0, 1.0, 0)))
        angle_B = MathTex(f"{self.angles[1]}^\\circ").next_to(B, np.array((-1.0, 1.0, 0)))
        angle_C = MathTex(f"{self.angles[2]}^\\circ").next_to(C, np.array((-1.0, -1.0, 0)))
        angle_D = MathTex(f"{self.angles[3]}^\\circ").next_to(D, np.array((1.0, -1.0, 0)))

        # Draw everything at once
        self.add(point_A, point_B, point_C, point_D)
        self.add(label_A, label_B, label_C, label_D)
        self.add(line_AB, line_BC, line_CD, line_DA)
        self.add(length_AB, length_BC, length_CD, length_DA)
        self.add(angle_A, angle_B, angle_C, angle_D)

        # Wait for a moment at the end to keep everything displayed
        self.wait(2)
