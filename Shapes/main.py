import ast
import os
from Shapes.complex import Complex
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv('.env.development')
    com = Complex()

    lss = ast.literal_eval(os.getenv('SHAPES'))

    print(com.shape(lss))
    print(com.clean_duplicates(lss))
