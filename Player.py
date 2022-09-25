import turtle


def start(self):
    items = []

    for i in range(self.listWidget.count() - 1):
        a = self.listWidget.item(i).text()
        print(a)
        match a[0]:
            case 'f':
                turtle.fd(int(a[1:]))
            case 'r':
                turtle.rt(int(a[1:]))
            case 'l':
                turtle.lt(int(a[1:]))
            case _:
                print('что то не то')
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True