# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Timed Programming Lab Test 1 - Question 3
# Author: Tran Manh Cuong (s3974735)
# Created date: 19/11/2022
# Last modified date: 19/11/2022
import turtle
win = turtle.Screen()
win.bgcolor("white")  # Background is white


def flag_bg():
    # This function draws the flag's background
    background = turtle.Turtle()
    background.color("blue", "red")  # pen color is blue and the fillcolor is red
    background.pensize(5)  # The background's pensize is 5 point
    background.penup()
    background.backward(200)
    background.left(90)
    background.forward(100)
    background.right(90)
    background.pendown()
    background.begin_fill()
    for i in range(2):  # draw a rectangle
        background.forward(400)
        background.right(90)
        background.forward(200)
        background.right(90)
    background.end_fill()
    background.ht()


def draw_star():
    # This function draws a star in the middle of the flag
    star = turtle.Turtle()
    star.color("white", "white")  # color is white
    star.penup()
    star.backward(20)
    star.pendown()
    star.begin_fill()
    star.left(120)
    star.forward(30)
    star.right(120)
    star.forward(30)
    for i in range(5):  # a for loop to draw 6 pointed shape
        star.left(60)
        star.forward(30)
        star.right(120)
        star.forward(30)
    star.end_fill()
    star.ht()


def main():
    # Main program
    flag_bg()
    draw_star()


main()
win.delay(10)
win.exitonclick()
