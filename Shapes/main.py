from Shapes.detect import Detect
from Shapes.complex import Complex
import math
from Shapes.calc import Calc
if __name__ == '__main__':
    c = Calc()
    ls=[3,4,5]
    print(c.triangle_area(ls))
    p = c.triangle_perimeter(ls)
    # print(p)
    # print(p*(p-3)*(p-4)*(p-5)**0.5)
    com = Complex()
    com.shape([])