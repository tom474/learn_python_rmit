# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Manh Cuong (s3974735)
# Created date: 09/11/2022
# Last modified date: 10/11/2022

import turtle
win = turtle.Screen()
win.bgcolor("red")  # Change the background color into red


def build_leaves(aspect, distance):
    # This function creates leaves (upper green part) for the Christmas tree
    leaves = turtle.Turtle()  # This turtle's name is "leaves"
    leaves.color("blue", "green")  # Leaves' color is green
    # The next 5 lines navigate where the start point of each green part is
    leaves.up()
    leaves.right(aspect)
    leaves.forward(distance)
    leaves.left(aspect)
    leaves.down()
    # The next 5 lines create green triangle
    leaves.begin_fill()
    for i in range(3):
        leaves.forward(200)
        leaves.left(120)
    leaves.end_fill()
    leaves.ht()  # Hide turtle's last stamp


def build_wood():
    # This function creates wood (lower brown part) for the Christmas tree
    wood = turtle.Turtle()  # This turtle's name is "wood"
    wood.color("brown", "brown")  # Wood's color is brown
    # The next 6 lines navigate where the start point of the brown part is
    wood.up()
    wood.right(90)
    wood.forward(200)
    wood.left(90)
    wood.forward(75)
    wood.down()
    # The next 10 lines create wood
    wood.begin_fill()
    wood.right(90)
    wood.forward(100)
    wood.left(90)
    wood.forward(50)
    wood.left(90)
    wood.forward(100)
    wood.left(90)
    wood.forward(50)
    wood.end_fill()
    wood.ht()  # Hide turtle's last stamp


def build_tree():
    # This function completes the Christmas tree
    build_leaves(0, 0)
    build_leaves(90, 100)
    build_leaves(90, 200)
    build_wood()


def tree_star():
    # This function creates a star on the top of the tree
    star = turtle.Turtle()  # This turtle's name is star
    star.color("yellow", "yellow")  # Star's color is yellow
    # The next 6 lines navigate where the start point of the star is
    star.up()
    star.left(90)
    star.forward(192)
    star.right(90)
    star.forward(75)
    star.down()
    # The next 5 lines create yellow star
    star.begin_fill()
    for i in range(5):
        star.forward(50)
        star.right(144)
    star.end_fill()
    star.ht()  # Hide turtle's last stamp


def make_ornaments(distance1, distance2, aspect):
    # This function creates ornaments to decorate the Christmas tree
    # Firstly, it creates a string to hold ornament
    string = turtle.Turtle()  # This turtle's name is string
    # The next 5 lines navigate where the start point of the string is
    string.up()
    string.forward(distance1)
    string.right(aspect)
    string.forward(distance2)
    string.down()
    string.forward(20)  # Create string
    string.ht()  # Hide turtle's last stamp

    # Secondly, it creates an ornament
    ornament = turtle.Turtle()  # This turtle's name is ornament
    # The next 6 lines navigate where the start point of the ornament is
    ornament.up()
    ornament.forward(distance1)
    ornament.right(aspect)
    ornament.forward(distance2 + 20)
    ornament.right(90)
    ornament.down()
    # The next 4 lines create ornament
    ornament.color("yellow", "yellow")
    ornament.begin_fill()
    ornament.circle(10)
    ornament.end_fill()
    ornament.ht()  # Hide turtle's last stamp


def accessories():
    # This function decorates the Christmas tree with a star and 6 ornaments
    tree_star()
    make_ornaments(0, 0, 90)
    make_ornaments(200, 0, 90)
    make_ornaments(0, 100, 90)
    make_ornaments(200, 100, 90)
    make_ornaments(0, 200, 90)
    make_ornaments(200, 200, 90)
    # These parameters are used to navigate the start point of each string and ornament


def make_gifts():
    # This function creates gift boxes under the tree
    gift = turtle.Turtle()  # This turtle's name is gift
    # The next 5 lines navigate where the start point of the gifts is
    gift.up()
    gift.right(90)
    gift.forward(300)
    gift.left(90)
    gift.down()
    # A nested for loop to create 4 boxes with 4 different colors
    for k in ["green", "blue", "yellow", "purple"]:
        gift.color(k, k)
        if k == "green":
            gift.up()
            gift.forward(0)
            gift.down()
        else:
            gift.up()
            gift.forward(50)
            gift.down()
        gift.begin_fill()
        for a in range(4):
            gift.forward(30)
            gift.left(90)
        gift.end_fill()
        gift.ht()  # Hide turtle's last stamp


def main():
    # This is the main function
    build_tree()
    accessories()
    make_gifts()


main()
win.delay(10)
win.exitonclick()
