class Detect(object):
    def __init__(self):
        pass

    def is_rectangle(self,ls):
        if len(ls) == 4 and ls[0] == ls[2] and ls[1]==ls[4]:
            return True
        return False

    def is_square(self, ls):
        if len(ls) == 4:
            for n in ls:
                if ls[0]!=n:
                    return False
                else:
                    return True
        return False

    def is_triangle(self, ls):
        if len(ls) == 3:
            for n in ls:
                if not ((sum(ls)-n) > n):
                    return False
        return True

