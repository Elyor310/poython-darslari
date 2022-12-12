import turtle
global a
a=0
def funk1():
    tosh.forward(50)
    a=0
def funk2():
    if a==0:
        tosh.left(90)
        a=1
    elif a==1:
        tosh.forward(50)
def funk3():
    tosh.right(45)
#def funk4():
 #   tosh.back(50)

def main():
    global wn, tosh
    wn=turtle.Screen()
    
    wn.title('toshbaqa')
    wn.bgcolor('green')

    tosh=turtle.Turtle()
    
    wn.onkey(funk1, 'Up')
    wn.onkey(funk2, 'Left')
    wn.onkey(funk3, 'Right')
  #  wn.onkey(funk4, 'Back' )

    wn.listen()
    wn.mainloop()

main()
    