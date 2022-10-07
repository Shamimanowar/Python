import turtle
import time


t = turtle.Turtle()


def write_r():
    t.speed(4)
    t.penup()
    t.goto(-30, 50)  # centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.right(90)
    t.forward(150)
    t.goto(-30, 50)
    t.speed(4)
    t.right(-90)
    t.circle(-50, 180, 100)
    t.penup()
    t.goto(0, -40)
    t.left(135)
    t.pendown()
    t.forward(70)


def write_o():
    # t.goto(30, 50)
    # t = turtle.Turtle()
    # t.penup()
    # t.goto(-30, 50)  # centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.circle(78, None, 100)
    t.penup()


def write_t():
    t.penup()
    # t.goto(-30, 50)  # centering in the screen
    t.goto(190, -80)
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.forward(100)
    t.goto(20, 50)
    t.right(90)
    t.forward(100)
    time.sleep(5)


if __name__ == "__main__":
    write_r()
    t.penup()
    t.goto(90, -80)
    write_o()
    # t.penup()
    # t.goto(190, -80)
    write_t()
