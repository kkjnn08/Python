import turtle as t
import random



def tree(length, pen_size):
    angle = random.randint(15, 30)
    branch = random.uniform(0.6, 0.9)
    r_color = random.choice(color_list)

    # 잎 그리기
    if length < 35:
        t.color(r_color)
        t.stamp()
        t.color("#283618")

    # 가지 그리기
    if length > 12:
        t.pensize(pen_size)
        pen_size *= 0.7
        t.forward(length)
        t.left(angle)
        tree(length*branch, pen_size)
        t.right(angle*2)
        tree(length*branch, pen_size)
        t.left(angle)
        t.backward(length)

color_list = ['#ECCB99', '#CB5C1E', '#984F26', '#4C0813', '#D3434D', '#7B111B', "#AE2130"]

t.bgcolor("#F7EAD6")

t.setheading(90)
t.speed(0)
t.up()
t.goto(0, -300)
t.down()

t.color("#283618")

tree(100, 10)
