from turtle import Turtle, Screen
# def move():
#     timmy.forward(100)
#     timmy.right(90)
timmy = Turtle()
timmy.shape("turtle")
# move()
# move()
# move()
# move()

# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
color_list = ['red','green','blue','yellow','purple','black','golden','beige','brown','green','blue','yellow','purple']
for i in range(4,10):
    for j in range(0,i):
        timmy.forward(100)
        timmy.right(360/i)
    timmy.color(color_list[i-4])



screen = Screen()
screen.exitonclick()