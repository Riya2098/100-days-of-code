def turn_right():
    turn_left()
    turn_left()
    turn_left()
  

while(at_goal()!=True):
    while(front_is_clear()):
        move()
    if(right_is_clear()):
        turn_right()
    elif(front_is_clear()):
        move()
    else:
        turn_left()


link to problem: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
