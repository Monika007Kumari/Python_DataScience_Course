from turtle import *

speed('fastest')
pencolor('red')

gap=3
angle=32

for i in range(100):
    fd(i*gap) #11
    #print(i*3+5)
    lt(angle)

mainloop()