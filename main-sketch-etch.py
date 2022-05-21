from turtle import Turtle, Screen

tur = Turtle()
win_screen = Screen()
tur.pensize(7)


def m_forward():
    tur.forward(10)
def m_left():
    tur.left(10)
def m_right():
    tur.right(10)
def m_down():
    tur.backward(10)

def clear_window_screen():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()



win_screen.listen()
win_screen.onkey(key="w", fun=m_forward)
win_screen.onkey(key="a", fun=m_left)
win_screen.onkey(key="d", fun=m_right)
win_screen.onkey(key="s", fun=m_down)
win_screen.onkey(clear_window_screen, "c")






win_screen.exitonclick()