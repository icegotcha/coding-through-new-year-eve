#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 11:00:06 2016

@author: icegotcha
HAPPT NEW YEAR 2017
"""

import turtle as t
from time import sleep
import random



def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w

def draw_star(size, color, ray, angle):
    t.fillcolor(color)
    t.begin_fill()
    for side in range(ray):
        t.forward(size)
        t.right(angle)
        t.forward(size)
        t.right((360/ray)-angle)
    t.end_fill()


def draw_christmas_tree(height, start, posX, posY):
    # move
    t.penup()
    t.goto(posX, posY)
    t.pendown()
    # start draw tree
    for n in range(start, height+1):
        x = posX
        for col in range(2*n-1):
            item = weighted_choice([("leaf", 4),("ball",1), ("decor", 2)])
            if item == "leaf":
                t.color("green")
                t.write("+", font=("Arial", 16, "bold"))
            elif item == "decor":
                rc = random.choice(["red", "cyan", "magenta", "yellow", "white"])
                t.color(rc)
                t.write(random.choice(['@', '&', '*', chr(169), chr(174)]),
                        font=("Arial", 16, "bold"))
            else:
                c = random.choice(["red", "orange", "yellow", 
                                       "blue", "white","purple"])
                # color
                t.color(c)
                t.fillcolor(c)
                #circle
                t.begin_fill()
                t.circle(10)
                t.end_fill()
            x += 20
            t.penup()
            t.goto(x, posY)
            t.pendown()
        # end the row
        posX -= 20
        posY -= 20
        t.penup()
        t.goto(posX, posY)
        t.pendown()
        
def draw():
    t.penup()
    t.goto(0, 180)
    t.pendown()
    # star
    draw_star(20, "yellow", 6, 120)
    t.penup()
    # tree
    draw_christmas_tree(15, 1, -15,100) 
    #stem
    t.penup()
    t.forward(210)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.setheading(0)
    t.colormode(255)
    brown = (139,69,19)
    t.fillcolor(*brown)
    t.color(*brown)
    t.begin_fill()
    for side in range(2):
        t.forward(180)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    # type word
    t.penup()
    t.setheading(-90)
    t.forward(80)
    t.setheading(180)
    t.forward(80)
    t.setheading(0)
    t.pendown()
    t.color("orange")
    word = "HAPPY NEW YEAR 2017"
    for letter in word:
       t.pendown()
       t.write(letter, font=("Arial", 16, "bold"))
       t.penup()
       t.forward(20)
       
    

# example of stars
#draw_star(30, "yellow", 5, 144)
#draw_star(30, "yellow", 6, 120) 
"""
" DRAW START HERE
"""
def say_bye(x,y):
   t.bye()
   
win = t.Screen()
win.onclick(say_bye)
t.bgcolor("black")
while(True):
   t.tracer(0,0)
   t.speed("fastest")
   draw()
   t.update()
   sleep(2.0)
   t.reset()
   
