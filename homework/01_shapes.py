# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(width=1600, height=900)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код



def triangle(point, angle=0, length=200, width=3):
    for add_angle in range(0, 360, 120):
        vect = sd.get_vector(start_point=point, angle=angle+add_angle, length=length, width=width)
        point = vect.end_point
        vect.draw()

point = sd.get_point(200,100)
triangle(point)

def square(point, angle=0, length=200, width=3):
    for add_angle in range(0,360,90):
        vect = sd.get_vector(start_point=point, angle=angle+add_angle, length=length, width=width)
        point = vect.end_point
        vect.draw()

point_1 = sd.get_point(400,300)
square(point_1)

def pentagon(point, angle=0, length=200, width=3):
    for add_angle in range(0,360,72):
        vect = sd.get_vector(start_point=point, angle=angle+add_angle, length=length, width=width)
        point = vect.end_point
        vect.draw()

point_2 = sd.get_point(150,550)
pentagon(point_2)

def hexagon(point, angle=0, length=200, width=3):
    for add_angle in range(0,360,60):
        vect = sd.get_vector(start_point=point, angle=angle+add_angle, length=length, width=width)
        point = vect.end_point
        vect.draw()

point_3 = sd.get_point(800, 150)
hexagon(point_3)

def polygon(point, angle_number, angle=0, length=200, width=3):
    angles_sum = (angle_number - 2) * 180
    internal_angle = angles_sum / angle_number
    external_angle = 180 - internal_angle
    add_angle = 0
    while add_angle<360:
        vect = sd.get_vector(start_point=point, angle=angle+add_angle, length=length, width=width)
        point = vect.end_point
        add_angle+=external_angle
        vect.draw()

point_4 = sd.get_point(1250, 300)
polygon(point_4, 5, 30)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
