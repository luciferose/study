import turtle

def setup(pencile):
    pencile.color('blue')
    pencile.penup()
    pencile.goto(-200,100)
    pencile.pendown()

def koch(pencil,size,order):
    if order == 0:
        pencil.forward(size)
    else:
        for angle in [60,-120,60,0]:
            koch(pencil,size/3,order-1)
            pencil.left(angle)

def main():
    pencil = turtle.Turtle()
    setup(pencil)
    order=2
    size=400

    for i in range(3):
        koch(pencil,size,order)
        pencil.right(120)

if __name__ == '__main__':
    main()
    turtle.tracer(1000)
    turtle.mainloop()