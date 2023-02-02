from Shapes.detect import Detect
from Shapes.complex import Complex
import math
from Shapes.calc import Calc
if __name__ == '__main__':
    # c = Calc()
    # ls=[3,4,5]
    # # print(c.triangle_area(ls))
    # p = c.triangle_perimeter(ls)
    # print(p)
    # print(p*(p-3)*(p-4)*(p-5)**0.5)
    com = Complex()
    # com.shape([])
    # print(com.generate_shape_format([2,3,4]))
    lss = [[2, 6, 2, 6],[6, 2, 6, 2],[4,4,4,4],[4,4,4,4]]

    # print(com.shape(lss))
    print(com.clean_duplicates(lss))
