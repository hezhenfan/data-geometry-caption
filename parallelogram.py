from manim import *
import math
import random
import sys
import argparse
import json
import os

# manim -ql --save_last_frame -o 1.png parallelogram.py -- --point --length --angle --ec_file 5.json


class ParallelogramWithDetails(Scene):

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

        self.shfit = round(random.uniform(-2, 2), 2)
        B_x = random.randint(-5, -4)
        B_y = random.randint(-3, -2)
        A_x = B_x + self.shfit
        A_y = random.randint(1, 3)
        C_x = random.randint(4, 5)
        C_y = B_y
        D_x = C_x + self.shfit
        D_y = A_y

        self.A = [A_x, A_y, 0]
        self.B = [B_x, B_y, 0]
        self.C = [C_x, C_y, 0]
        self.D = [D_x, D_y, 0]
        self.MathTex_A = "A(" + f"{self.A[0]}" + ", " + f"{self.A[1]}" + ")"
        self.MathTex_B = "B(" + f"{self.B[0]}" + ", " + f"{self.B[1]}" + ")"
        self.MathTex_C = "C(" + f"{self.C[0]}" + ", " + f"{self.C[1]}" + ")"
        self.MathTex_D = "D(" + f"{self.D[0]}" + ", " + f"{self.D[1]}" + ")"

        # 线段长度
        self.length_AB = self.calculate_distance(self.A, self.B)
        self.length_BC = self.calculate_distance(self.B, self.C)
        self.length_CD = self.calculate_distance(self.C, self.D)
        self.length_AD = self.calculate_distance(self.A, self.D)

    def calculate_distance(self, point1, point2):

        distance = round(math.sqrt(
            (point2[0] - point1[0])**2 +
            (point2[1] - point1[1])**2
        ), 2)

        formatted_distance = f"{distance:.2f}".rstrip('0').rstrip('.') if '.' in f"{distance:.2f}" else f"{int(distance)}"

        return formatted_distance

    def calculate_angle(self, A, B, C):
        # 计算向量 AB 和 AC
        AB = [B[i] - A[i] for i in range(len(A))]
        AC = [C[i] - A[i] for i in range(len(A))]
        
        # 计算点积
        dot_product = sum(AB[i] * AC[i] for i in range(len(A)))
        
        # 计算向量的模
        magnitude_AB = math.sqrt(sum(AB[i] ** 2 for i in range(len(A))))
        magnitude_AC = math.sqrt(sum(AC[i] ** 2 for i in range(len(A))))
        
        # 计算夹角的余弦值
        cos_theta = dot_product / (magnitude_AB * magnitude_AC)
        
        # 计算夹角，使用 acos 函数，并转换为角度
        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)

        formatted_angle = f"{angle_degrees:.2f}".rstrip('0').rstrip('.') if '.' in f"{angle_degrees:.2f}" else f"{int(angle_degrees)}"
        
        return formatted_angle, cos_theta

    def construct(self):

        # Create points
        point_A = Dot(self.A, color=BLUE, radius=0.01)
        point_B = Dot(self.B, color=BLUE, radius=0.01)
        point_C = Dot(self.C, color=BLUE, radius=0.01)
        point_D = Dot(self.D, color=BLUE, radius=0.01)

        # Create labels for points
        label_A = MathTex(self.MathTex_A).scale(0.5).next_to(point_A, UP)
        label_B = MathTex(self.MathTex_B).scale(0.5).next_to(point_B, DOWN)
        label_C = MathTex(self.MathTex_C).scale(0.5).next_to(point_C, DOWN)
        label_D = MathTex(self.MathTex_D).scale(0.5).next_to(point_D, UP)

        vertex_A = MathTex('A').scale(0.5).next_to(point_A, UP)
        vertex_B = MathTex('B').scale(0.5).next_to(point_B, DOWN)
        vertex_C = MathTex('C').scale(0.5).next_to(point_C, DOWN)
        vertex_D = MathTex('D').scale(0.5).next_to(point_D, UP)

        # Create lines between points
        line_AB = Line(self.A, self.B)
        line_BC = Line(self.B, self.C)
        line_CD = Line(self.C, self.D)
        line_AD = Line(self.A, self.D)

        # Create edge lengths
        length_AB = MathTex(f"{self.length_AB}").scale(0.5).next_to(line_AB, LEFT, buff=0.2)
        length_BC = MathTex(f"{self.length_BC}").scale(0.5).next_to(line_BC, DOWN, buff=0.2)
        length_CD = MathTex(f"{self.length_CD}").scale(0.5).next_to(line_CD, RIGHT, buff=0.2)
        length_AD = MathTex(f"{self.length_AD}").scale(0.5).next_to(line_AD, UP, buff=0.2)

        # length_AB.shift(RIGHT * 1)
        # length_AC.shift(LEFT * 1)

        # 标注角度
        angle_A_degrees, cos_theta_A = self.calculate_angle(self.A, self.B, self.D)
        angle_B_degrees, cos_theta_B = self.calculate_angle(self.B, self.C, self.A)
        angle_C_degrees, cos_theta_C = self.calculate_angle(self.C, self.D, self.B)
        angle_D_degrees, cos_theta_D = self.calculate_angle(self.D, self.A, self.C)
        angle_A = Angle(Line(self.A, self.B), Line(self.A, self.D), radius=0.5, other_angle=False)
        angle_B = Angle(Line(self.B, self.C), Line(self.B, self.A), other_angle=False)
        angle_C = Angle(Line(self.C, self.D), Line(self.C, self.B), radius=0.5, other_angle=False)
        angle_D = Angle(Line(self.D, self.A), Line(self.D, self.C), radius=0.5, other_angle=False)
        angle_label_A = MathTex(f"{angle_A_degrees}^{{\\circ}}").scale(0.4).next_to(angle_A, DOWN)
        angle_label_B = MathTex(f"{angle_B_degrees}^{{\\circ}}").scale(0.4).next_to(angle_B, UP)
        angle_label_C = MathTex(f"{angle_C_degrees}^{{\\circ}}").scale(0.4).next_to(angle_C, UP)
        angle_label_D = MathTex(f"{angle_D_degrees}^{{\\circ}}").scale(0.4).next_to(angle_D, DOWN)

        if self.shfit > 0:
            angle_label_A.shift(RIGHT * 0.5)
            angle_label_B.shift(RIGHT * 0.5)
            angle_label_C.shift(LEFT * 0.5)
            angle_label_D.shift(LEFT * 0.5)
        else:
            angle_label_A.shift(RIGHT * 0.5)
            angle_label_B.shift(RIGHT * 0.5)
            angle_label_C.shift(LEFT * 0.5)
            angle_label_D.shift(LEFT * 0.5)
        # Draw the parallelogram, labels, and edge lengths at once

        ecs = []

        self.add(point_A, point_B, point_C, point_D)
        if self.args.point:
            self.add(label_A, label_B, label_C, label_D)
        else:
            self.add(vertex_A, vertex_B, vertex_C, vertex_D)
        self.add(line_AB, line_BC, line_CD, line_AD)
        if self.args.length:
            self.add(length_AB, length_BC, length_CD, length_AD)
            ecs.append(f'AB={self.length_AB}')
            ecs.append(f'BC={self.length_BC}')
            ecs.append(f'CD={self.length_CD}')
            ecs.append(f'AD={self.length_AD}')
        if self.args.angle:
            self.add(angle_A, angle_B, angle_C, angle_D)
            self.add(angle_label_A, angle_label_B, angle_label_C, angle_label_D)
            ecs.append(f'∠A={angle_A_degrees}°')
            ecs.append(f'∠B={angle_B_degrees}°')
            ecs.append(f'∠C={angle_C_degrees}°')
            ecs.append(f'∠D={angle_D_degrees}°')

        ec_file = self.args.ec_file
        if ec_file:
            ec_path = os.path.join(os.getcwd(), 'ec', ec_file)
            print(ec_path)
            with open(ec_path, 'w', encoding='utf-8') as f:
                json.dump(ecs, f, ensure_ascii=False, indent=4)

        # Wait for a moment at the end to keep everything displayed
        self.wait(2)
