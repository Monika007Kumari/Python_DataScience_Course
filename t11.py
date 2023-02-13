from turtle import *

speed('slowest')

side=20
size=50

# create a hexagon
for i in range(20):
    forward(size)
    left(360/side)
    write(i)

hideturtle() #hide turle
mainloop()  #keep window open