"""
sierpinski_triangle.py

A program that draws the Sierpiński triangle.

Author: Trevor DePew
"""

import turtle
import math


def draw_sierpinski_triangle(x1, y1, x2, y2, t):
    pass


def main():
    print("Drawing triangles!")
    t = turtle.Turtle()
    t.hideturtle()

    try:
        draw_sierpinski_triangle(-100, 0, 100, 0, t)
        draw_sierpinski_triangle(0, -173.2, -100, 0, t)
        draw_sierpinski_triangle(100, 0, 0, -173.2, t)
    except:
        print("Exception, exiting.")
        exit(0)


if __name__ == '__main__':
    main()
