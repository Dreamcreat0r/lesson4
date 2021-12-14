# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

def polygon(point, angle_number, color, angle=0, length=200, width=3):
    angles_sum = (angle_number - 2) * 180
    internal_angle = angles_sum / angle_number
    external_angle = 180 - internal_angle
    add_angle = 0
    while add_angle<360:
        vect = sd.get_vector(start_point=point, angle=angle+add_angle, length=length, width=width)
        point = vect.end_point
        add_angle+=external_angle
        vect.draw(color=color)

color_list = ('COLOR_RED', 'COLOR_ORANGE', 'COLOR_YELLOW', 'COLOR_GREEN', 'COLOR_CYAN', 'COLOR_BLUE', 'COLOR_PURPLE')
color_dict = {'COLOR_RED':sd.COLOR_RED, 'COLOR_ORANGE':sd.COLOR_ORANGE, 'COLOR_YELLOW':sd.COLOR_YELLOW, 
              'COLOR_GREEN':sd.COLOR_GREEN, 'COLOR_CYAN':sd.COLOR_CYAN, 'COLOR_BLUE':sd.COLOR_BLUE, 
              'COLOR_PURPLE':sd.COLOR_PURPLE}
print('Дотупные цвета:')
for index, value in enumerate(color_list):
    print(index, ' : ', value)

angle_number = input('Please, choose the number of angles: ')
angle = input('Please, choose the incline angle: ')
length = input('Please, choose the face length: ')
width = input('Please, choose the face width: ')
color = input('Please, chooose color index: ')

angle_number = int(angle_number)
angle = int(angle)
length = int(length)
width = int(width)
color = color_list[int(color)]

color = color_dict[color]

point = sd.get_point(300,300)
polygon(point=point, angle_number=angle_number, angle=angle, length=length, width=width, color=color)

sd.pause()
