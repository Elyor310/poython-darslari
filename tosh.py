import turtle
a=0

def funk1():
    tosh.forward(50)
    global a
    a=0

def funk2():
    global a
    if a==0:
        tosh.left(90)
        a=1
    else:
        tosh.forward(50)
        

def funk3():
    tosh.right(45)
    a=0

def funk4():
    wn.bye()

def main():
    global tosh
    global wn
    wn=turtle.Screen()
    wn.title("Toshbaqa")
    wn.bgcolor('green')
    tosh=turtle.Turtle()

    wn.onkey(funk1, "Up")
    wn.onkey(funk2, "Left")
    wn.onkey(funk3, "Right")
    wn.onkey(funk4, "q")

    wn.listen()


    wn.mainloop()
main()