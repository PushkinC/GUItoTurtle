import turtle


# Начало
def start(self):

    if self.isTurtle.checkState() == 2:
        turtle.shape('turtle')
    else:
        turtle.shape('circle')
        turtle.shapesize(0.01, 0.01, 0)

    if self.isAnim.checkState() == 2:
        turtle.speed(6)
    else:
        turtle.speed('fastest')



    for i in range(self.listWidget.count()):
        a = self.listWidget.item(i).text()
        match a[0]:
            case 'f':
                turtle.fd(int(a[1:]))
            case 'r':
                turtle.rt(int(a[1:]))
            case 'l':
                turtle.lt(int(a[1:]))
            case 'u':
                turtle.penup()
            case 'd':
                turtle.pendown()
            case _:
                print('что то не то')



    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True