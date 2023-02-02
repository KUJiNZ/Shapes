class Detect(object):
    def __init__(self):
        pass

    def is_rectangle(self,ls):
        """
        Name: Artiom
        Function Name: is_rectangle
        Description: Function gets list checking if he is kind of rectangle shape
        :param ls: list of shape parameters
        :return: True or False
        """
        if len(ls) == 4:
            for n in ls:
                if ls.count(n) != 2:
                    return False
            return True
        return False

    def is_square(self, ls):
        """
        Name: Artiom
        Function Name: is_square
        Description: Function gets list checking if he is kind of square shape
        :param ls: list of shape parameters
        :return: True or False
        """
        if len(ls) == 4:
            for n in ls:
                if ls[1]!=n:
                    return False
            return True
        return False

    def is_triangle(self, ls):
        """
        Name: Artiom
        Function Name: is_triangle
        Description: Function gets list checking if he is kind of triangle shape
        :param ls: list of shape parameters
        :return: True or False
        """
        if len(ls) == 3:
            for n in ls:
                #if sum of two sides of tringle less that one side it is not triagle
                if not ((sum(ls)-n) > n):
                    return False
        return True

