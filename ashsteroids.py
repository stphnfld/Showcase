import turtle
import math
import random

# Set up screen
wn = turtle.Screen()
wn.bgcolor('black')

# Draw border
mypen = turtle.Turtle()
mypen.color('white')
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()

# Create multiple asteroids
max_asteroids = 5
asteroids = []

for count in range(max_asteroids):
    asteroids.append(turtle.Turtle())
    asteroids[count].color('red')
    asteroids[count].shape('circle')
    asteroids[count].penup()
    asteroids[count].speed(0)
    asteroids[count].setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set player speed
playerspeed = 1

# Create player's bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(player.heading())
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = 'ready'

# Move player
def move_left():
    player.left(30)

def move_right():
    player.right(30)

def fire_bullet():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        bullet.setposition(player.xcor(), player.ycor())
        bullet.setheading(player.heading())

# Collision checking
def is_collision(t1, t2):
    return math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2)) < 20

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')

while True:
    for asteroid in asteroids:
        asteroid.forward(2)

        # Boundary checking for asteroid
        if asteroid.xcor() > 290 or asteroid.xcor() < -290:
            asteroid.right(180)
        if asteroid.ycor() > 290 or asteroid.ycor() < -290:
            asteroid.right(180)

        # Collision checking between bullet and asteroid
        if is_collision(bullet, asteroid):
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(-400, -400)
            asteroid.setposition(random.randint(-290, 290), random.randint(-290, 290))

        # Collision checking between player and asteroid
        if is_collision(player, asteroid):
            player.hideturtle()
            asteroid.hideturtle()
            print('Game Over')
            break

    # Move the bullet
    if bulletstate == 'fire':
        bullet.fd(bulletspeed)

    # Boundary checking for bullet
    if bullet.xcor() > 290 or bullet.xcor() < -290 or bullet.ycor() > 290 or bullet.ycor() < -290:
        bullet.hideturtle()
        bulletstate = 'ready'
