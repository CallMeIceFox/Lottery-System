import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Juego de la Suerte")

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(25)
pen.penup()
pen.goto(-300,-300)
pen.pendown()
for i in range(6):
    pen.setheading(0)
    pen.forward(600)
    pen.setheading(90)
    pen.forward(50)
    pen.setheading(180)
    pen.forward(600)
    pen.setheading(90)
    pen.forward(50)
pen.setheading(0)
pen.forward(600)


# Function to draw a number
def draw_number(x, y, number, color="black"):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(number, align="center", font=("Arial", 24, "normal"))

# Get user's 6 number guesses
user_numbers_input = screen.textinput("6 Numeros", "Escribe 6 numeros separados por un espacio de 1-99.")
if user_numbers_input is not None:
    try:
        user_numbers = list(map(int, user_numbers_input.split()))
        if len(user_numbers) == 6 and all(1 <= num <= 99 for num in user_numbers):
            # Generate random numbers
            random_numbers = random.sample(range(1, 99), 8)
            print("Random Numbers:", random_numbers)

            # Draw random numbers on the screen
            for i, num in enumerate(random_numbers):
                draw_number(-200 + i * 50, 0, num)

            # Compare numbers
            matches = [num for num in user_numbers if num in random_numbers]
            num_matches = len(matches)
            draw_number(0, 150, f"Adivinaste {num_matches} numeros", color="green")

            # Draw matches on the screen
            for i, num in enumerate(user_numbers):
                if num in matches:
                    draw_number(-200 + i * 50, -50, num, color="green")
        else:
            draw_number(0, 150, "Invalido", color="red")
    except ValueError:
        draw_number(0, 150, "Invalido", color="red")
else:
    draw_number(0, 150, "Zero Numeros Escritos", color="red")

pen.color("gold")
pen.pensize(10)
pen.penup()
pen.goto(-62,-250)
pen.pendown()
pen.begin_fill()
pen.forward(125)
pen.setheading(90)
pen.forward(125)
pen.setheading(180)
pen.forward(125)
pen.setheading(270)
pen.forward(125)
pen.end_fill()
pen.penup()
pen.goto(0,-225)
pen.color("blue")
pen.pendown()
pen.setheading(90)
pen.forward(75)
pen.setheading(270)
pen.forward(15)
pen.setheading(0)
pen.forward(25)
pen.setheading(180)
pen.forward(50)
pen.setheading(270)
pen.forward(25)
pen.setheading(0)
pen.forward(50)
pen.setheading(270)
pen.forward(25)
pen.setheading(180)
pen.forward(50)

def restart():
    pen.color("lightblue")
    pen.penup()
    pen.goto(-300,-300)
    for i in range(600):
        pen.setheading(0)
        pen.forward(600)
        pen.setheading(90)
        pen.forward(1)
        pen.setheading(180)
        pen.forward(600)
        pen.setheading(90)
        pen.forward(1)



listen()
onkey(restart, "Space")

screen.mainloop()