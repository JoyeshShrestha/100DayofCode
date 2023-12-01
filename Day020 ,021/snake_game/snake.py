from turtle import Screen, Turtle
STARTING_POSTITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
RIGHT = 0
LEFT=180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):    
        for position in STARTING_POSTITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
            snake_block = Turtle("square")
            snake_block.color("white")
            snake_block.speed("slow")
            snake_block.penup()
            snake_block.goto(position)
            
            self.segments.append(snake_block)
    def extend(self):
         self.add_segment(self.segments[-1].position())
         

    def move(self):
        for seg_num in range(len(self.segments)-1 , 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()

            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)         

    def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP) 
    def down(self):
            if self.head.heading() != UP:
            
                self.head.setheading(DOWN) 
   
    def left(self):
            if self.head.heading() != RIGHT:
            
                self.head.setheading(LEFT) 

    def right(self):
            if self.head.heading() != LEFT:
            
             self.head.setheading(RIGHT) 
                       