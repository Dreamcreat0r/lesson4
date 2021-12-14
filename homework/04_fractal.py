# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
# Сделать так, чтобы нижние ветки были толстыми, а верхние - тоньше. Порог работы функции - по толщине веток
# Тонкие ветки сделать другого цвета

# Пригодятся функции
# sd.random_number()

# TODO здесь ваш код

def draw_branches(start_point, middle_angle, length, width):
    if width>1:
        width-=1
    if width>2:
        color = sd.COLOR_DARK_ORANGE
    else:
        color = sd.COLOR_GREEN
    rand_angle1 = sd.random_number(0, 20)
    angle1 = middle_angle + 20 + rand_angle1
    vect1 = sd.get_vector(start_point=start_point, angle=angle1, length=length, width=width)
    vect1.draw(color=color)
    end_point1 = vect1.end_point
    if length > 3:
        length1 = length * .75
        draw_branches(start_point=end_point1, middle_angle=angle1, length=length1, width=width)
    else:
        return
    rand_angle2 = sd.random_number(0, 20)
    angle2 = middle_angle-40+rand_angle2
    vect2 = sd.get_vector(start_point=start_point, angle=angle2, length=length, width=width)
    vect2.draw(color=color)
    end_point2 = vect2.end_point
    if length > 3:
        length2 = length * .75
        draw_branches(start_point=end_point2, middle_angle=angle2, length=length2, width=width)
    else:
        return

root_point = sd.get_point(300,5)
stem_width = 10
stem = sd.get_vector(start_point=root_point, angle = 90, length = 100, width=stem_width)
stem.draw(color = sd.COLOR_DARK_ORANGE)
length = 85
stem_end = stem.end_point

draw_branches(start_point=stem_end, middle_angle=90, length=length, width=stem_width)

sd.pause()


