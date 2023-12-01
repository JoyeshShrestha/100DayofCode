from turtle import Turtle, Screen

johnny = Turtle()
screen = Screen()


def move_forwards():
    johnny.forward(10)

def backward():
    johnny.backward(10)


def left():
        johnny.left(10)

def right():
        johnny.right(10)        
def gone():
      johnny.hideturtle()
      johnny.penup()
      johnny.home()

      johnny.showturtle()  
      johnny.pendown()      
      
def clearScreen():
      johnny.clear()
      gone()

def upen():
      johnny.penup()

def dpen():
      johnny.pendown()      
screen.listen()
screen.onkey(key="w", fun= move_forwards)
screen.onkey(key="s",fun=backward)
screen.onkey(key="a",fun=left)
screen.onkey(key="d",fun=right)
screen.onkey(key = "c", fun = clearScreen)
screen.onkey(key="p",fun=upen)
screen.onkey(key="o",fun=dpen)



screen.exitonclick()