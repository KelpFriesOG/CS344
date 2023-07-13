import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed of the turtle
my_turtle.speed(10)

# Set the color of the pen
my_turtle.pencolor("black")

# Set the fill color of the circle
my_turtle.fillcolor("red")

# Begin filling the Pokéball shape
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()

# Move to the center of the red region
my_turtle.penup()
my_turtle.goto(0, -50)
my_turtle.pendown()

# Set the fill color of the white region
my_turtle.fillcolor("white")

# Begin filling the white region
my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

# Move to the center of the red region
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

# Set the fill color of the black region
my_turtle.fillcolor("black")

# Begin filling the black region
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open until it is closed manually
turtle.done()
