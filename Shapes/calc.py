from Shapes.detect import Detect
import math


class Calc(Detect):
    def __init__(self):
        super().__init__()

    def rectangle_perimeter(self, ls):
        """
        Name: Artiom
        Function Name: rectangle_perimeter
        Description: Function gets list of rectangle parameters and counting his perimeter
        :param ls: list of shape parameters
        :return: perimeter
        """
        if (self.is_rectangle(ls)):
            return sum(ls)
        if (self.is_square(ls)):
            return sum(ls)
        raise Exception("This is not a rectangle or square!")

    def rectangle_area(self, ls):
        """
        Name: Artiom
        Function Name: rectangle_area
        Description: Function gets list of rectangle parameters and counting his area
        :param ls: list of shape parameters
        :return: area
        """
        i = 1
        if (self.is_rectangle(ls)):
            for n in ls:
                if ls[i] != n and i <= len(ls) - 1:
                    return ls[i] * n
                i += 1
        if (self.is_square(ls)):
            return ls[0] * ls[1]
        raise Exception("This is not a rectangle or square!")

    def triangle_perimeter(self, ls):
        """
        Name: Artiom
        Function Name: triangle_perimeter
        Description: Function gets list of triangle parameters and counting his perimeter
        :param ls: list of shape parameters
        :return: perimeter
        """
        i = 1
        if (self.is_triangle(ls)):
            return sum(ls)
        raise Exception("This is not a triangle!")

    def triangle_area(self, ls):
        """
        Name: Artiom
        Function Name: triangle_area
        Description: Function gets list of triangle parameters and counting his area
        :param ls: list of shape parameters
        :return: area
        """
        if (self.is_triangle(ls)):
            semi = self.triangle_perimeter(ls) / 2
            return math.sqrt(semi * (semi - ls[0]) * (semi - ls[1]) * (semi - ls[2]))
        raise Exception("This is not a triangle!")
