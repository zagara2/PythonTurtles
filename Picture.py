'''
Created on Feb 7, 2016

@author: Mickey
'''
import turtle              # allows us to use the turtles library                                         
wn = turtle.Screen()        # creates a graphics window                                                    
                                                                                                                           
def Strawberry(turt): #draws a strawberry towards the middle-right of the screen
    #sets speed and makes sure the turtle moves to the right location
    turt.speed(10)
    turt.penup()
    turt.home()
    turt.pendown()
    
    #main shape of the berry
    turt.fillcolor("red")
    turt.pencolor("red")
    turt.begin_fill()
    turt.left(90)
    for x in range(180):
        turt.forward(1)
        turt.right(1)
    turt.right(90)
    turt.forward(115)
    turt.left(118) 
    turt.forward (75)
    turt.left (30)
    turt.forward(40)
    turt.left (75)
    turt.forward(40)
    turt.left(30)
    turt.forward(63)
    turt.end_fill()

    #back to middle of top to draw leaves
    turt.penup()
    turt.home()
    turt.left(90)
    for x in range(90):
        turt.forward(1)
        turt.right(1)
    
    #drawing leaves
    turt.pendown()
    turt.pencolor("green")
    turt.pensize(8)
    turt.left(45)
    turt.forward(30)
    turt.right(180)
    turt.forward(30)
    turt.right(90)
    turt.forward(30)
    turt.right(180)
    turt.forward(30)
    turt.right(225)
    turt.forward(30)
    turt.penup()
    
    #draws black dots on the strawberry
    turt.goto(40, -30)
    turt.pendown()
    turt.dot(10, "black")
    turt.penup()
    turt.goto(60, -20)
    turt.dot(10, "black")
    turt.goto(40, -10)
    turt.dot(10, "black")
    turt.goto(80, -20)
    turt.dot(10, "black")
    turt.goto(20, -10)
    turt.dot(10, "black")
    turt.goto(80, 10)
    turt.dot(10, "black")
    turt.goto(80, 30)
    turt.dot(10, "black")
    turt.goto(70, 10)
    turt.dot(10, "black")
    turt.goto(60, -70)
    turt.dot(10, "black")
    turt.goto(70, -60)
    turt.dot(10, "black")
    turt.goto(20, 30)
    turt.dot(10, "black")
    turt.goto(20, 20)
    turt.dot(10, "black")
    turt.goto(40, 25)
    turt.dot(10, "black")
    turt.goto(30, 19)
    turt.dot(10, "black")
    
    #moving turtle location on screen after it draws the strawberry
    turt.penup()
    turt.home()
    turt.right(90)
    turt.forward(200)
    turt.pendown()
def writewords(turt): #writes "hooray for food!" on the screen 
   
    turt.pencolor("black")
    foodstring = "hooray for food!"
    turt.write(foodstring,font=("Arial", 25, "normal"))
    
    #moving turtle location on screen
    turt.penup()
    turt.home()
    turt.right(45)
    turt.forward(400)

def orangeslice(turt):#draws an orange slice
    
    #main shape of orange slice
    turt.pendown()
    turt.pencolor("yellow")
    turt.pensize(10)
    turt.fillcolor("orange")
    turt.begin_fill()
    turt.right(90)
    for x in range(180):
        turt.forward(1)
        turt.left(1)
    turt.left(90)
    turt.forward(118)
    turt.end_fill()
    
    #drawing lines inside
    turt.pensize(5)
    turt.right(180)
    turt.forward(59)
    turt.right(155)
    turt.forward(50)
    turt.right(180)
    turt.forward(50)
    turt.right(125)
    turt.forward(50)
    turt.right(180)
    turt.forward(50)
    turt.right(135)
    turt.forward(50)
    turt.right(180)
    turt.forward(50)
    turt.right(155)
    turt.forward(50)
    turt.right(180)
    turt.forward(50)
    turt.left(80)
    turt.forward(50)
    
    #moving turtle location
    turt.penup()
    turt.home()
    turt.right(180)
    turt.forward(200)
def donut(turt):#draws a donut decorated with pink frosting
    
    #big brown circle
    turt.pendown()
    turt.fillcolor("brown")
    turt.speed(10)
    turt.pencolor("brown")
    turt.begin_fill()
    turt.circle(100)
    turt.end_fill()
     
    #spiral frosting design
    turt.left(90)
    turt.forward(100)
    turt.width(5)
    for size in range(5, 40, 1):    
        turt.dot(15, "pink")
        turt.penup()                
        turt.forward(size)          
        turt.right(24) 
    
    #white hole in the middle
    turt.pencolor("black")
    turt.fillcolor("white")
    turt.begin_fill()
    turt.right(90)
    turt.forward(60)
    turt.right(90)
    turt.pendown()
    turt.circle(40)
    turt.end_fill()
    
    #move turtle location
    turt.penup()
    turt.home()
    turt.right(300)
    turt.forward(270)
def drink(turt): #draws a drink with a festive umbrella in it 
    #moving turtle to desired location
    turt.penup()
    turt.backward(235)
    turt.left(90)
    turt.forward(250)
    turt.right(60)
    
    #the glass
    turt.pendown()
    turt.pensize(8)
    turt.forward(150)
    turt.right(90)
    turt.forward(75)
    turt.right(90)
    turt.backward(-150)
    turt.right(90)
    turt.forward(75)
    turt.right(90)
    turt.penup()
    turt.forward(75)
    turt.right(90)
    
    #the liquid inside
    turt.pencolor("light blue")
    turt.fillcolor("light blue")
    turt.penup()
    turt.forward(7)
    turt.pendown()
    turt.begin_fill()
    turt.forward(61)
    turt.right(90)
    turt.forward(70)
    turt.right(90)
    turt.forward(61)
    turt.right(90)
    turt.forward(70)
    turt.end_fill()
    
    #the umbrella
    turt.penup()
    turt.right(90)
    turt.forward(30)
    turt.left(80)
    turt.pensize(2)
    turt.pencolor("black")
    turt.fillcolor("hot pink")
    turt.pendown()
    turt.forward(100)
    turt.right(90)
    turt.begin_fill()
    turt.forward(30)
    turt.left(135)
    turt.forward(40)
    turt.dot(8, "black")
    turt.left(90)
    turt.forward(40)
    turt.left(135)
    turt.forward(30)
    turt.end_fill()
    
    #the bubbles
    turt.penup()
    turt.right(90)
    turt.forward(150)
    turt.dot(12, "white")
    turt.left(190)
    turt.forward(30)
    turt.dot(12, "white")
    turt.right(120)
    turt.forward(25)
    turt.dot(12, "white")

def grapes(turt): #draws grapes 
    #hiding turtle, moving turtle to desired location
    turt.hideturtle()        
    turt.penup()
    turt.home()
    turt.forward(310)
    turt.left(90)
    turt.forward(275)
    
    #leaves
    turt.width("8")
    turt.left(90)
    turt.pendown()
    turt.pencolor("green")
    turt.fillcolor("green")
    turt.stamp()
    turt.right(45)
    turt.stamp()
    turt.right(-45)
    
    #stem
    turt.pencolor("brown")
    turt.forward(50)
    turt.right(180)
    turt.forward(25)
    turt.right(90)
    turt.forward(160)
    turt.right(180)
    turt.forward(130)
    turt.left(90)
    turt.forward(20)
    turt.penup()
    
    #purple grapes
    turt.dot(40, "purple")
    turt.forward(30)
    turt.dot(40, "purple")
    turt.forward(-30)
    turt.dot(40, "purple")
    turt.forward(-40)
    turt.dot(40, "purple")
    turt.forward(-30)
    turt.dot(40, "purple")
    turt.forward(30)
    turt.left(90)
    turt.forward(30)
    turt.dot(40, "purple")
    turt.right(90)
    turt.forward(40)
    turt.dot(40, "purple")
    turt.forward(25)
    turt.dot(30, "purple")
    turt.right(250)
    turt.forward(30)
    turt.dot(30, "purple")
    turt.left(45)
    turt.forward(30)
    turt.dot(40, "purple")
    turt.forward(30)
    turt.dot(30, "purple")
    turt.left(270)
    turt.forward(30)
    turt.dot(30, "purple")
    turt.forward(-60)
    turt.dot(30, "purple")
    turt.backward(30)
    turt.dot(35, "purple")
    turt.right(20)
    turt.forward(95)
    turt.dot(30, "purple")
    turt.left(200)
    turt.forward(60)
    turt.dot(25, "purple")
    turt.right(160)
    turt.forward(80)
    turt.dot(25, "purple")

        
def draw(): 
#creates a turtle and draws a picture of a strawberry, 2 orange slices, 
#2 donuts, a drink, grapes, and the words "hooray for food!"
    alex = turtle.Turtle()
    Strawberry(alex)
    writewords(alex)
    orangeslice(alex)
    orangeslice(alex)
    donut(alex)
    donut(alex)
    drink(alex)
    grapes(alex)

 
 
if __name__ == '__main__': 
    draw() 

    wn.exitonclick()   # must be last line in file