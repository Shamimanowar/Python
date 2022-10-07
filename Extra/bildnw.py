# import package
import turtle
import time

# write text
# styling font
# turtle.speed(9)
# turtle.write("GeeksForGeeks", font=("Verdana", 15, "normal"))

t=turtle.Turtle()
def write_b():
    t.penup()
    t.goto(-30, 50)  # centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.right(90)
    t.forward(200)
    t.penup()
    t.goto(-30, 50)  # centering in the screen
    # draw first curve
    t.pendown()
    t.right(-90)
    t.circle(-50, 180)

    t.penup()
    t.goto(-30, -50)  # centering in the screen
    # draw second curve
    t.pendown()
    t.right(180)
    t.circle(-50, 180)
    time.sleep(2)


def write_build():
    turtle.color('purple')
    turtle.speed(0)
    style = ('Courier', 90, 'normal')
    turtle.write('IldNw', font=style, align='center')
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    write_b()
    t.penup()
    t.goto(50, -50)
    write_build()
