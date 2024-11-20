from turtle import * #This line imports turtle, which is a graphics library. After importing turtle, one can draw designs and customize their screen to display different shapes and patterns using the colour and pensize function. In addition, one can move the turtle, which is the focal point of the screen, forward, backwards, right and left. 

from freegames import square, vector #This line imports a square and vector function from freegames, which is a Python module. This module contains simple games and functions that allows one to create a simple game of their own. The square function creates a square in which the user plays the game. The vector function controls the position and movement of vectors within the game. In this case, the vector would control the snake and the food, for example.

from random import randrange

food = vector(0, 0) #This line creates a vector at the coordinates (0,0). "Food" represents a position in the game that the snake must pass in order to eat it and grow.
snake = [vector(10, 0)] #This line creates a list called snake with the vector at the coordinates (10,0). The list "snake" exists as a list so that more items can be added as the snake consumes the "food" on the screen.
aim = vector(0, -10) #This line creates a vector at the coordinates (0,10). The variable aim contains the direction in which the snake moves. The coordinates (0,-10) implies that the snake moves down ten units as the game is started.


def change(x, y): #This function changes the direction that the snake moves in. It moves in respect to the x and y axes. When this function is called, the position of the snake, in (x,y) coordinates, is updated in the game.
    """Change snake direction."""
    aim.x = x #This changes the snakes x-direction. If the snake moves 15 units right, the overall change in the function would be (15,0).
    aim.y = y #This changes the snakes y-direction. If the snake moves 15 units up, the overall change in the function would be (0,15).


def inside(head): #This function determines if the head of the snake is within the boundaries (x and y coordinates below) of the game.
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190 #This function checks if the head of the snake is between the x coordinates (-200,190) and y coordinates (-200,190).
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