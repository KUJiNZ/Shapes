from Shapes.detect import Detect
import math
class Calc(Detect):
    def __init__(self):
        super().__init__()


    def rectangle_perimeter(self, ls):
        if(self.is_rectangle(ls)):
            return sum(ls)
        raise Exception("This is not a rectangle!")


    def rectangle_area(self, ls):
        if(self.is_rectangle(ls)):
            return ls[0]*ls[1]
        raise Exception("This is not a rectangle!")



    def triangle_perimeter(self, ls):
        if(self.is_triangle(ls)):
            return sum(ls)
        raise Exception("This is not a triangle!")



    def triangle_area(self, ls):
        if(self.is_triangle(ls)):
            semi = self.triangle_perimeter(ls)/2
            return math.sqrt(semi * (semi - ls[0]) * (semi - ls[1]) * (semi - ls[2]))
        raise Exception("This is not a triangle!")