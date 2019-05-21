import turtle,random

turtles = list()

def setup():
    global turtles
    startlin = -620
    screen = turtle.Screen()
    screen.setup(1290,720)

    turtle_ycor = [-60, -30, 0 , 30 ,60]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green']

    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startlin,turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

def race():
    global turtles
    winner = False
    finshline=590

    while not winner:
        for current_tutrle in turtles:
            move = random.randint(0,2)
            current_tutrle.forward(move)
            xcor = current_tutrle.xcor()
            if (xcor >= finshline):
                winner = True
                winner_color = current_tutrle.color()
                print(winner_color)
                print('winner is: ',winner_color[0])

setup()
race()
turtle.mainloop()