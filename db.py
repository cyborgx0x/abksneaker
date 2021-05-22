class Line:
    def __init__(self,points):
        self.points = points
    def drawline(self):
        for [*index] in self.points:
            print(index)
   

line1 = Line([{"x":10,"y":10},{"x":5,"y":10}])
line1.drawline()