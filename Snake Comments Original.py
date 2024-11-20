from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
#Kennice

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake)) #Daniella 
        food.x = randrange(-15, 15) * 10 #RH: Set a new random x-coordinate for food in the range of (-15,15). This will pick a random integer is the range, multiplying it by 10 so it aligns with the snakes grid
        food.y = randrange(-15, 15) * 10 #RH: set anew random y coordinate for the food (same thing as line above, line ensures the food is somehwere on teh game grid)
    else:
        snake.pop(0) #RH: remove the tail segment (first element in the snake list) if the food is not eaten (else condition)

    clear() #RH: Clear the screen for drawing allows for no overlap of past drawings by erasing everything on the screen so the game can update the snake and food position 
#RH: for loop that loops through every segment in the snake list) to draw each segment of the snake
    for body in snake:
        square(body.x, body.y, 9, 'black') #RH: Draw the snake as a black square by assigning the x and y coordinates with 9 

    square(food.x, food.y, 9, 'green')#RH: draw the food as a green square 
    update() #RH: update display to show the new positions 
    ontimer(move, 100) #RH: schedule the next move after 100millisseconds
#Rileigh 
#Victoria 
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()