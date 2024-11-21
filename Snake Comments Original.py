from turtle import * #KP: This line imports turtle, which is a graphics library. After importing turtle, one can draw designs and customize their screen to display different shapes and patterns using the colour and pensize function. In addition, one can move the turtle, which is the focal point of the screen, forward, backwards, right and left. 

from freegames import square, vector #KP: This line imports a square and vector function from freegames, which is a Python module. This module contains simple games and functions that allows one to create a simple game of their own. The square function creates a square in which the user plays the game. The vector function controls the position and movement of vectors within the game. In this case, the vector would control the snake and the food, for example.

from random import randrange

food = vector(0, 0) #KP: This line creates a vector at the coordinates (0,0). "Food" represents a position in the game that the snake must pass in order to eat it and grow.
snake = [vector(10, 0)] #KP: This line creates a list called snake with the vector at the coordinates (10,0). The list "snake" exists as a list so that more items can be added as the snake consumes the "food" on the screen.
aim = vector(0, -10) #KP: This line creates a vector at the coordinates (0,10). The variable aim contains the direction in which the snake moves. The coordinates (0,-10) implies that the snake moves down ten units as the game is started.


def change(x, y): #KP: This function changes the direction that the snake moves in. It moves in respect to the x and y axes. When this function is called, the position of the snake, in (x,y) coordinates, is updated in the game.
    """Change snake direction."""
    aim.x = x #KP: This changes the snakes x-direction. If the snake moves 15 units right, the overall change in the function would be (15,0).
    aim.y = y #KP: This changes the snakes y-direction. If the snake moves 15 units up, the overall change in the function would be (0,15).


def inside(head): #KP: This function determines if the head of the snake is within the boundaries (x and y coordinates below) of the game.
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190 #KP: This function checks if the head of the snake is between the x coordinates (-200,190) and y coordinates (-200,190).

def move(): #DR: defining move function (creating new function object "move"), which doesn't take any arguments
    """Move snake forward one segment."""
    head = snake[-1].copy() #DR: creating a copy of the last vector stored in the "snake" list using the built-in list copy() method, and assigning it to the variable "head"
    head.move(aim) #DR: changing the head's position by adding the aim vector using the  move() method of the freegames module vector class

    if not inside(head) or head in snake: #DR: if the head leaves the boundaries or touches the body (i.e. if inside(head) returns False or the head vector is in snake), the code in the indented block is executed
        square(head.x, head.y, 9, 'red') #DR: creates a red square of size 9 at the head's position using the freegames module square() function
        update() #DR: updates display (to show the square)
        return #DR: terminates function (and game)

    snake.append(head) #DR: if neither of the two if statement conditions are true, head is added to snake using the built-in list append() method

    if head == food: #DR: if the head vector is the same as the food vector, the code in the indented block is executed
        print('Snake:', len(snake)) #DR: printing the length of the snake to the console 
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
 
setup(420, 420, 370, 0) #VH: The parameters are such: setup(width, height, startx, starty), and this configures the game window. The first two values, 420 and 420, set the window width and height to 420 pixels. The third and fourth numbers, 370 and 0, position the window at coordinates (370,0) on the user's screen. 
hideturtle() #VH: This hides the default Turtle cursor, which by default appears as an arrow in the window. It does this because the cursor is not needed in this game. We are only using Turtle graphics to drap the snake, food, and background so hiding the cursor provides a cleaner interface.
tracer(False) #VH: This disables the automatic screen updates that happen with each drawing command in Turtle. tracer(n), by default, has an integer parameter 'n' which determines how frequently Turtle updates the screen: tracer(false) is the same as tracer(0) which completely disables automatic updates. With this, it prevents flickering and the snake's movements appear smoother. 
listen() #VH: This function makes the Turtle window responsive to keyboard inputs. This is used because it enables the window to detect key pressed, which allows the player to control the snake using the arrow keys on one's keyboard. Without this function, the game would not respond to keyboard inputs.  
# VH: onkey() binds specific keys to specific actions. Each call to onkey() assiciates a key (Right, Left, Up, Down) with a function that will execute when the key is pressed.
# VH: Here, lambda is a small directional inline function. It provides a way to create temporary functions so that we don't need to define four seperate functions. These inline functions call the change() functions with specific arguments when specific keys are pressed. Each individual function changes the movement of the snake by modifying aim.x and aim.y which are the x and y vectors (horizontal and vertical components of direction).
onkey(lambda: change(10, 0), 'Right') # VH: When the Right arrow key is pressed, the snake moves right by 10 pixels per frame and has no vertical movement. 
onkey(lambda: change(-10, 0), 'Left') # VH: When the Left arrow key is pressed, the snake moves left by 10 pixels per frame and has no vertical movement. 
onkey(lambda: change(0, 10), 'Up') # VH: When the Up arrow key is pressed, the snake moves up by 10 pixels per frame and has no horizontal movement. 
onkey(lambda: change(0, -10), 'Down') # VH: When the Down arrow key is pressed, the snake moves down by 10 pixels per frame and has no horizontal movement. 
#VH: for the previous four functions, it does this because it allows the players to control the direction of the snake by pressing the arrow keys.
move() #VH: This function is the main loop of the game as it handles moving the snake, checking for collisions, updating the game state, and redrawing the screen. This loop makes the game itself responsive to player input and maintains gameplay until a the snake collides either with a wall or irself. 
done() #VH: This function keeps the game window open after the program has finished running. In this function, the game stops automatically if the snake collides with a wall or itself. Calling done() after move() ensures that the window remains open even after the game ends.
