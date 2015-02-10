# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # This is a heading
# 
# ## this is a subheading
# 
# * a bulleted
# * list
# * of things
# 
# 1. enumerated
# 2. lists
# 
# I like **bold** and *italic*

# <codecell>

print "hello world"

# <codecell>

5*100

# <codecell>

5.6/2.3

# <markdowncell>

# remember - exponents use the double asterisk

# <codecell>

3**4

# <codecell>

a=5
b=6

# <codecell>

sqrt(a**2+b**2)

# <codecell>

3**100

# <codecell>

%gui tk
from turtle import *

# <codecell>

reset()

# <codecell>

forward(50)

# <codecell>

forward(10)

# <codecell>

reset()

forward(50)
right(45)
forward(50)

# <codecell>

reset()

length_of_a_side=150

forward(length_of_a_side)
right(90)

forward(length_of_a_side)
right(90)

forward(length_of_a_side)
right(90)

forward(length_of_a_side)
right(90)

# <codecell>

reset()

length_of_a_side=150

print "start here"
for i in range(4):
    forward(length_of_a_side)
    right(90)
    print "in the loop ",i
    
print "end here"

# <codecell>

length_of_a_side

# <codecell>

def draw_square(length_of_a_side):
    forward(length_of_a_side)
    right(90)

    forward(length_of_a_side)
    right(90)

    forward(length_of_a_side)
    right(90)

    forward(length_of_a_side)
    right(90)

# <codecell>

reset()
draw_square(30)
forward(30)

draw_square(30)
forward(30)

draw_square(30)
forward(30)

# <codecell>

def draw_row():
  for i in range(6):
    draw_square(30)
    forward(30)
  
def back_over():
    backward(6*30)
    right(90)
    forward(30)
    left(90)

# <codecell>

reset()
for i in range(6):
    draw_row()
    back_over()

# <codecell>

reset()
draw_row()

back_over()

draw_row()

# <codecell>


