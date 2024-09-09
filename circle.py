from manim import *
import math
import random
import sys
import argparse
import json
import os

# manim -ql --save_last_frame -o 1.png circle.py -- --point --length --angle --ec_file 4.json


class CircleWithDetails(Scene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 通过命令行参数来控制添加的元素
        parser = argparse.ArgumentParser()
        parser.add_argument("--point", action="store_true", help="Show points")
        parser.add_argument("--length", action="store_true", help="Show lengths")
        parser.add_argument("--angle", action="store_true", help="Show angles")
        parser.add_argument("--ec_file", type=str)
        self.args = parser.parse_args(sys.argv[7:])

        # 生成坐标点 [-7, 7] 宽，[-4, 4] 高

        O_x = random.randint(-1, 1)
        O_y = random.randint(-1, 1)

        self.radius = random.choice([i * 0.5 for i in range(3, 6)])

        self.O = [O_x, O_y, 0]
        self.MathTex_O = "O(" + f"{self.O[0]}" + ", " + f"{self.O[1]}" + ")"

        # 线段长度
        # self.length_AB = self.calculate_distance(self.A, self.B)
        # self.length_BC = self.calculate_distance(self.B, self.C)
        # self.length_CD = self.calculate_distance(self.C, self.D)
        # self.length_AD = self.calculate_distance(self.A, self.D)

    def calculate_distance(self, point1, point2):

        distance = round(math.sqrt(
            (point2[0] - point1[0])**2 +
            (point2[1] - point1[1])**2
        ), 2)

        formatted_distance = f"{distance:.2f}".rstrip('0').rstrip('.') if '.' in f"{distance:.2f}" else f"{int(distance)}"

        return formatted_distance

    def construct(self):

        # Create points
        point_O = Dot(self.O, color=BLUE, radius=0.05)

        # Create labels for points
        label_O = MathTex(self.MathTex_O).scale(0.5).next_to(point_O, UP)
        # label_B = MathTex(self.MathTex_B).scale(0.5).next_to(point_B, DOWN)
        # label_C = MathTex(self.MathTex_C).scale(0.5).next_to(point_C, DOWN)
        # label_D = MathTex(self.MathTex_D).scale(0.5).next_to(point_D, UP)

        vertex_O = MathTex('O').scale(0.5).next_to(point_O, UP)

        circle_O = Circle(radius=self.radius, color=WHITE)
        circle_O.move_to(self.O)

        # Create lines between points
        # line_AB = Line(self.A, self.B)
        # line_BC = Line(self.B, self.C)
        # line_CD = Line(self.C, self.D)
        # line_AD = Line(self.A, self.D)

        # Create edge lengths
        # length_AB = MathTex(f"{self.length_AB}").scale(0.5).next_to(line_AB, LEFT, buff=0.2)
        # length_BC = MathTex(f"{self.length_BC}").scale(0.5).next_to(line_BC, DOWN, buff=0.2)
        # length_CD = MathTex(f"{self.length_CD}").scale(0.5).next_to(line_CD, RIGHT, buff=0.2)
        # length_AD = MathTex(f"{self.length_AD}").scale(0.5).next_to(line_AD, UP, buff=0.2)

        # length_AB.shift(RIGHT * 1)
        # length_AC.shift(LEFT * 1)

        # 标注角度
        # right_angle = RightAngle(Line(self.B, self.A), Line(self.B, self.C), length=0.4, quadrant=(1, 1))

        # 添加90度的标注
        # angle_label = MathTex("90^{\\circ}").next_to(right_angle, UR, buff=0.1).scale(0.7)

        # Draw the parallelogram, labels, and edge lengths at once
        ecs = []

        ecs.append(f'r={self.radius}')

        self.add(point_O)
        self.add(circle_O)
        if self.args.point:
            self.add(label_O)
        else:
            self.add(vertex_O)
        # if self.args.length:
        #     self.add(length_AB, length_BC, length_CD, length_AD)
        #     ecs.append(f'AB={self.length_AB}')
        #     ecs.append(f'BC={self.length_BC}')
        #     ecs.append(f'CD={self.length_CD}')
        #     ecs.append(f'AD={self.length_AD}')
        # if self.args.angle:
        #     self.add(right_angle)
        #     ecs.append(f'∠A={90}°')
        #     ecs.append(f'∠B={90}°')
        #     ecs.append(f'∠C={90}°')
        #     ecs.append(f'∠D={90}°')

        ec_file = self.args.ec_file
        if ec_file:
            ec_path = os.path.join(os.getcwd(), 'ec', ec_file)
            print(ec_path)
            with open(ec_path, 'w', encoding='utf-8') as f:
                json.dump(ecs, f, ensure_ascii=False, indent=4)

        # Wait for a moment at the end to keep everything displayed
        self.wait(2)
