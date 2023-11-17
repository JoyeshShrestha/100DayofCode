def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()

count = 0    
while at_goal() is False:
    if right_is_clear() is True:
        turn_right()
        move()
        count+=1
        if count > 4:
            move()
    elif front_is_clear() is True:
        move()
        count=0

    else:
        count=0
        turn_left()
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
