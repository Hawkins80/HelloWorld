# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(15)

# list of colors
colors = ["pink", "blue", "purple", "green", "orange", "red", "aqua", "gray", "gold", "magenta"]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


# draw octagon
def octagon(size):
    color_tina()
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)


# repeating octagons
def octagons(size, num):
    for x in range(1, num):
        octagon(size * x)


# draw a series of circles
def super_circles(size):
    for x in range(1, 15):
        color_tina()
        tina.circle(size * x)


# call my fancy new functions
super_circles(5)
octagons(5, 15)

# making star
tina = turtle.Turtle()

for i in range(20):
    tina.forward(i * 10)
    tina.right(144)
    tina.speed(2500)

tina.done()

# At the end of my app, I will use a conditional
# A conditional is another word for an if statement
answer = input("What next?")
print("You just said: " + answer)

if answer == "octagon":
    print("Oh, I know that one!")
    octagon(20)
elif answer == "super circles":
    print("Oh, I can do that!")
    super_circles(5)
elif answer == "justin bieber":
    print("My commander said I cannot do that...")


