from turtle import Turtle
POSITIONS = [(-380,20),(-380,0),(-380,-20)]
# POSITIONS = [(0,20),(0,0),(0,-20)]

MOVE_DISTANCE = 20
class FirstPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.SEGMENTS = []
        
        self.create_paddle()
        self.head = self.SEGMENTS[0]
        self.mid = self.SEGMENTS[1]
        self.tail =self.SEGMENTS[2]

    def create_paddle(self):
        for i in POSITIONS:

            self.add_segment(i)
        
    def add_segment(self,i):
            paddle_parts = Turtle("square")
            paddle_parts.hideturtle()
            paddle_parts.speed("fastest")
            paddle_parts.color("white")
            paddle_parts.penup()
            paddle_parts.setheading(90)
            paddle_parts.goto(i)
            paddle_parts.showturtle()
            self.SEGMENTS.append(paddle_parts)


    def first_up(self):
        if self.head.ycor() >=  280:
             pass
        else:
             self.up()
    def up(self):    
        for seg in range(2,0,-1):
              
              xcors = self.SEGMENTS[seg-1].xcor()
              ycors = self.SEGMENTS[seg-1].ycor()
              self.SEGMENTS[seg].goto(xcors,ycors)

        self.head.forward(MOVE_DISTANCE)

    def first_down(self):
        if self.head.ycor() <=  -240:
             pass
        else:
             self.down()

    def down(self):   
        for seg in range(0,2,1):
              
              xcors = self.SEGMENTS[seg+1].xcor()
              ycors = self.SEGMENTS[seg+1].ycor()
              self.SEGMENTS[seg].goto(xcors,ycors)

        self.tail.backward(MOVE_DISTANCE)    


         
                 
