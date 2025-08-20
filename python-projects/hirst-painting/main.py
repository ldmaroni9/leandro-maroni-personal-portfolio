#This script creates a 10x10 frame with spots that are 20 in size and 50 paces apart
from turtle import Turtle, Screen
from random import randint
import colorgram

colors = colorgram.extract('dystopia.jpg', 20)
print(colors)
color_list = []
all_colors = []

for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    new_color = (r, g, b)
    all_colors.append(new_color)

print(all_colors)

t = Turtle()

t.shape("arrow")
t.pensize(20)

screen = Screen()
screen.colormode(255)


dystopia_colors = [(82, 90, 96), (39, 43, 45), (141, 154, 163), (32, 36, 34), (31, 30, 28), (78, 85, 84), (204, 215, 221), (150, 160, 157), (102, 90, 75), (217, 227, 224), (59, 63, 70), (31, 28, 30), (58, 65, 68), (57, 67, 66), (239, 240, 232), (117, 131, 136), (114, 128, 144), (158, 156, 147), (119, 132, 129), (178, 191, 208)]
peace_sells_colors = [(122, 68, 84), (147, 75, 64), (44, 28, 24), (187, 97, 81), (59, 34, 44), (90, 49, 64), (211, 143, 87), (10, 14, 12), (94, 50, 44), (176, 94, 100), (23, 25, 29), (82, 78, 102), (188, 124, 58), (172, 131, 143), (243, 192, 96), (74, 80, 78), (88, 62, 34), (65, 57, 81), (225, 177, 165), (233, 191, 169)]
rust_in_peace_colors = [(32, 45, 131), (51, 75, 166), (31, 27, 68), (82, 109, 193), (39, 22, 40), (216, 150, 88), (239, 227, 85), (122, 147, 209), (146, 93, 58), (118, 73, 109), (241, 235, 181), (202, 220, 247), (31, 22, 15), (192, 131, 167), (84, 47, 85), (151, 160, 62), (89, 166, 65), (161, 181, 238), (135, 165, 131), (196, 104, 72)]
horizontal_steps = 0
vertical_steps = 0

t.penup()
t.back(350)
t.right(90)
t.forward(320)
t.left(90)
t.pendown()
t.speed(100)


def horizontal_motion():
    random_color_index = randint(0, len(peace_sells_colors)-1)
    random_color = peace_sells_colors[random_color_index]
    t.pencolor(random_color)
    t.down()
    t.circle(10)
    t.up()
    t.forward(70)


while vertical_steps < 10:
    while horizontal_steps < 10:
        horizontal_steps += 1
        horizontal_motion()
    t.backward(700)
    t.left(90)
    t.forward(70)
    t.right(90)
    vertical_steps += 1
    horizontal_steps -= 10


screen.exitonclick()
