from manim import *
import math
import random
import sys
import argparse
import json
import os

# manim -ql --save_last_frame -o 1.png sector.py -- --point --length --angle --ec_file 7.json


class SectorWithDetails(Scene):

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

        self.radius = random.choice([i * 0.5 for i in range(5, 7)])
        self.start_angle = PI/random.choice([2, 3, 4, 5, 6])
        self.angle = PI/random.choice([1, 2, 3, 4, 5, 6])

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

        vertex_O = MathTex('O').scale(0.5).next_to(point_O, UP)

        sector_O = Sector(
            outer_radius=self.radius,          # 半径
            start_angle=self.start_angle,  # 起始角度为 45 度
            angle=self.angle,        # 扇形角度为
            fill_opacity=0,
            stroke_width=4,  # 边界线宽度
            stroke_color=BLUE  # 边界线颜色
        )
        sector_O.move_to(self.O)

        # 创建表示角度的弧线
        angle_arc = Arc(
            radius=self.radius * 0.1,         # 弧线的半径
            start_angle=self.start_angle,   # 弧线的起始角度
            angle=self.angle,         # 弧线的角度
        )
        angle_arc.move_to(self.O)

        # 标注角度值
        angle_label = MathTex(f"{self.angle * 180 / PI}^\\circ").scale(0.5).next_to(angle_arc, RIGHT)

        # Draw the parallelogram, labels, and edge lengths at once
        ecs = []

        ecs.append(f'r={self.radius}')

        self.add(point_O)
        self.add(sector_O)
        self.add(angle_arc)
        if self.args.point:
            self.add(label_O)
        else:
            self.add(vertex_O)

        if self.args.angle:
            self.add(angle_label)

        ec_file = self.args.ec_file
        if ec_file:
            ec_path = os.path.join(os.getcwd(), 'ec', ec_file)
            print(ec_path)
            with open(ec_path, 'w', encoding='utf-8') as f:
                json.dump(ecs, f, ensure_ascii=False, indent=4)

        # Wait for a moment at the end to keep everything displayed
        self.wait(2)
