import docker
import os

# docker run -d --name manim -v "D:\\math\\geometry-caption\\:/manim" manimcommunity/manim tail -f /dev/null


def gen_geometry(output, geometry, labels_arg):

    command = f'manim -ql --save_last_frame -o {output} {geometry}.py -- {labels_arg}'
    print(command)

    client = docker.from_env()
    container = client.containers.get('manim')
    exec_result = container.exec_run(command)
    print(exec_result.exit_code)


def batch_gen(total, geometry, labels):

    labels_name = '_'.join(labels)
    labels_arg = '--' + ' --'.join(labels)

    for i in range(1, total + 1):
        output = f'{geometry}_{labels_name}_{i}.png'
        gen_geometry(output, geometry, labels_arg + f' --ec_file {geometry}_{labels_name}_{i}.json')


if __name__ == "__main__":

    # labels = ['point', 'length', 'angle']  组合标记

    # 修改 total 和 扩展 geometrys，以生成更丰富的图形
    total = 1
    geometrys = ['isosceles_triangle', 'parallelogram', 'rectangle', 'square']
    for geometry in geometrys:
        batch_gen(total, geometry, ['point'])
        batch_gen(total, geometry, ['length'])
        batch_gen(total, geometry, ['angle'])
        batch_gen(total, geometry, ['point', 'length'])
        batch_gen(total, geometry, ['length', 'angle'])
        batch_gen(total, geometry, ['point', 'angle'])
        batch_gen(total, geometry, ['point', 'length', 'angle'])




