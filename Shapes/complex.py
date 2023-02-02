from Shapes.detect import Detect
from Shapes.calc import Calc

class Complex(Calc):
    def __init__(self):
        super().__init__()
        self.shape([])


    def shape(self,lss):
        # triangles = [{"triangles":[{"sides":[],"area": 0}]
        result= [
            {"triangles":
            [
            {
             "sides": [3, 4, 5],
             "area": 6,
             "perimeter": 12
            }
            ]
            },


        {"rectangles": [
                {
                    "sides": [2, 3, 2, 3],
                    "area": 6,
                    "perimeter": 10
                }
            ]
        },
            {"squares": [
                {
                    "sides": [2, 2, 2, 2],
                    "area": 4,
                    "perimeter": 8
                }
            ]
            }
        ]
        print(result[0]['triangles'])
        # for shape in lss:
        #     if(len(shape))==4:
        #         if(self.is_square(shape)):
        #             print(result[0])

