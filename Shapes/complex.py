from Shapes.calc import Calc


class Complex(Calc):
    def __init__(self):
        super().__init__()

    def shape(self, shapes):
        """
        Name: Artiom
        Function Name: shape
        Description: Function gets list of lists shapes,checking what exactly shape is.
        :param shapes: list of list shapes
        :return: dictionary with all kinds of shapes
        """
        try:
            proper_shapes=self.clean_duplicates(shapes)
            # format for dict to return
            result = [{"triangles": []}, {"rectangles": []}, {"squares": []}]
            # checking what kind of shape is
            for shape in proper_shapes:
                # if is triangle?
                if (len(shape)) == 3:
                    if (self.is_rectangle(shape)):
                        result[0]["triangles"].append(self.generate_triangle_format(shape))
                # if is rectangle or square?
                if (len(shape)) == 4:
                    if (self.is_rectangle(shape)):
                        result[1]["rectangles"].append(self.generate_rectangle_format(shape))

                    if (self.is_square(shape)):
                        result[2]["squares"].append(self.generate_rectangle_format(shape))

            return result

        except Exception as e:
            raise e

    def generate_triangle_format(self, triangle):
        """
        Name: Artiom
        Function Name: generate_triangle_format
        Description: Function gets triangle of lists of shapes and creating formatted list to insert in dictionary.
        :param triangle: list of shape
        :return: list of formatted shape
        """
        try:
            # format to insert in dictionary
            format_of_shape = {
                "sides": [],
                "area": 0,
                "perimeter": 0
            }

            for n in triangle:
                format_of_shape["sides"].append(n)
            format_of_shape["area"] = self.triangle_area(triangle)
            format_of_shape["perimeter"] = self.triangle_perimeter(triangle)
            return format_of_shape
        except Exception as e:
            raise e

    def generate_rectangle_format(self, rectangle):
        """
          Name: Artiom
          Function Name: generate_rectangle_format
          Description: Function gets rectangle of lists of shapes and creating formatted list to insert in dictionary.
          :param rectangle: list of shape
          :return: list of formatted shape
          """
        try:
            # format to insert in dictionary
            format_of_shape = {
                "sides": [],
                "area": 0,
                "perimeter": 0
            }
            for n in rectangle:
                format_of_shape["sides"].append(n)
            format_of_shape["area"] = self.rectangle_area(rectangle)
            format_of_shape["perimeter"] = self.rectangle_perimeter(rectangle)
            return format_of_shape
        except Exception as e:
            raise e

    def clean_duplicates(self, shapes):
        """
          Name: Artiom
          Function Name: clean_duplicates
          Description: Function gets lists of shapes and removing duplicate.
          :param shapes: lists of improper shapes
          :return: lists of proper shapes
          """
        try:
            # for each shape in shapes comparing if next is duplicate
            for i in range(len(shapes) - 1):
                for j in range(len(shapes) - 1):
                    j = i + 1
                    # if shapes in list are the same size and sum need to check them if are duplicates
                    if j < len(shapes) and sum(shapes[i]) == sum(shapes[j]) and len(shapes[i]) == len(shapes[j]):
                        length = len(shapes[i])
                        count = 0
                        # checking for duplicates each value of both shapes
                        for v in shapes[i]:
                            if shapes[i].count(v) == shapes[j].count(v):
                                count += 1
                                #if number of values appearing in both shapes the same times that means they are the same
                                if count == length:
                                    shapes.remove(shapes[j])
            return shapes
        except Exception as e:
            raise e
