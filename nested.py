from turtle import *

speed('fastest')
pencolor('red')

for i in range(6):
    fd(100)
    for i in range(6):
        fd(50)
        write(i)
        for i in range(6):
            fd(25)
            lt(60)
        lt(60)
    rt(60)
    write(i)


hideturtle()
mainloop()