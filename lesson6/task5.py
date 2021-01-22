
class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print(f'запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'запуск отрисовки Pen')


class Pencill(Stationery):
    def draw(self):
        print(f'запуск отрисовки Pencill')


class Handle(Stationery):
    def draw(self):
        print(f'запуск отрисовки Handle')


st = Stationery('Stationery')
pn = Pen('Pen')
pc = Pencill('Pencill')
hl = Handle('Handle')

for i in [st, pn, pc, hl]:
    i.draw()