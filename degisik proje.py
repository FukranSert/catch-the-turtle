import time
import turtle
import random
gameover=False
#drawing_board
drawing_board=turtle.Screen()
drawing_board.bgcolor("blue")
drawing_board.title("MY_TURTLE")
turtle.setup(1200,700)
turtle.setworldcoordinates(-100,-100,100,100)
turtle1=turtle.Turtle()
turtle1.hideturtle()

#screen deatails
style=("Courier",30,"italic")
k=0
#scorebegging
turtle2=turtle.Turtle()

drawing_board.delay(0)
turtle2.color("black")
turtle2.penup()
turtle2.goto(0,90)
turtle2.pendown()
turtle2.write(f"SCORE:{k}",font=style,align="right",move=False)
turtle2.hideturtle()



#time board

def countdown(time):

    turtle1.clear()
    turtle1.color("red")
    turtle1.penup()
    turtle1.goto(0, 70)
    turtle1.pendown()


    if time > 0:
        turtle1.clear()

        turtle1.write(f"TIME:{time}", align='right', font=style)

        drawing_board.ontimer(lambda :countdown(time-1), 1000)
        turtle1.hideturtle()
    else:
        global gameover
        turtle2.hideturtle()
        turtle3.hideturtle()
        gameover=True
        turtle1.write(f"Gameover! Your score:{k}", align='right', font=style)
#oyun turtle ı
turtle3=turtle.Turtle()

turtle3.color("green")
turtle3.shape("turtle")
turtle3.shapesize(2.5,2,5)
x=list(range(-95,95))
y=list(range(-95,65))
def positionchanger():
    if gameover==False:
        turtle3.penup()
        turtle3.setpos(random.choice(x), random.choice(y))
        turtle.pendown()
        drawing_board.ontimer(positionchanger,750)


#score board

def scoree(x,y):
    global k
    k=k+1
    turtle2.clear()
    turtle2.color("black")
    turtle2.penup()
    turtle2.goto(0, 90)
    turtle2.pendown()
    turtle2.write(f"SCORE:{k}", font=style, align="right", move=False)
    turtle2.hideturtle()


countdown(10)
turtle3.onclick(scoree)
positionchanger()

turtle.mainloop()




