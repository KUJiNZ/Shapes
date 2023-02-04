import os
import pytest

from Tests import test_complex
from Tests.test_complex import *



if __name__ == '__main__':
    pytest.main(['test_complex.py','test_calc.py','test_detect.py'])
