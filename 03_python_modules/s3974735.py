# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2022C
# Assignment: 1
# Author: Tran Manh Cuong (s3974735)
# Created date: 09/11/2022
# Last modified date: 10/11/2022

import turtle

win = turtle.Screen()
win.bgcolor("red")  # Change the background color to red


def build_leaves(aspect, distance):
    """This function creates leaves (upper green part) for the Christmas tree."""
    leaves = turtle.Turtle()
    leaves.color("blue", "green")  # Green leaves
    leaves.up()
    leaves.right(aspect)
    leaves.forward(distance)
    leaves.left(aspect)
    leaves.down()
    leaves.begin_fill()
    for _ in range(3):  # Draw green triangle
        leaves.forward(200)
        leaves.left(120)
    leaves.end_fill()
    leaves.hideturtle()


def build_wood():
    """This function creates wood (lower brown part) for the Christmas tree."""
    wood = turtle.Turtle()
    wood.color("brown", "brown")  # Brown wood
    wood.up()
    wood.right(90)
    wood.forward(200)
    wood.left(90)
    wood.forward(75)
    wood.down()
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
    wood.hideturtle()


def build_tree():
    """This function completes the Christmas tree."""
    build_leaves(0, 0)
    build_leaves(90, 100)
    build_leaves(90, 200)
    build_wood()


def tree_star():
    """This function creates a star on the top of the tree."""
    star = turtle.Turtle()
    star.color("yellow", "yellow")  # Yellow star
    star.up()
    star.left(90)
    star.forward(192)
    star.right(90)
    star.forward(75)
    star.down()
    star.begin_fill()
    for _ in range(5):  # Draw a star
        star.forward(50)
        star.right(144)
    star.end_fill()
    star.hideturtle()


def make_ornaments(distance1, distance2, aspect):
    """This function creates ornaments to decorate the Christmas tree."""
    string = turtle.Turtle()
    string.up()
    string.forward(distance1)
    string.right(aspect)
    string.forward(distance2)
    string.down()
    string.forward(20)  # Create string
    string.hideturtle()

    ornament = turtle.Turtle()
    ornament.up()
    ornament.forward(distance1)
    ornament.right(aspect)
    ornament.forward(distance2 + 20)
    ornament.right(90)
    ornament.down()
    ornament.color("yellow", "yellow")
    ornament.begin_fill()
    ornament.circle(10)  # Draw ornament
    ornament.end_fill()
    ornament.hideturtle()


def accessories():
    """This function decorates the Christmas tree with a star and 6 ornaments."""
    tree_star()
    for distance1 in [0, 200]:
        for distance2 in [0, 100, 200]:
            make_ornaments(distance1, distance2, 90)


def make_gifts():
    """This function creates gift boxes under the tree."""
    gift = turtle.Turtle()
    gift.up()
    gift.right(90)
    gift.forward(300)
    gift.left(90)
    gift.down()
    # Create 4 different colored boxes
    for color in ["green", "blue", "yellow", "purple"]:
        gift.color(color, color)
        if color != "green":
            gift.up()
            gift.forward(50)
            gift.down()
        gift.begin_fill()
        for _ in range(4):
            gift.forward(30)
            gift.left(90)
        gift.end_fill()
    gift.hideturtle()


def main():
    """Main function to build and decorate the tree."""
    build_tree()
    accessories()
    make_gifts()


main()
win.delay(10)
win.exitonclick()
