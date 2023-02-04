import ast
import os
import pytest

from Shapes.calc import Calc
from dotenv import load_dotenv

from Tests.log import Log

# LOGGER
LOG = Log("__calc__ ", "calc_log.log")
logger = LOG.logger


@pytest.fixture
def calc():
    # ENV FILE
    load_dotenv('.env.test')

    # DETECT ClASS
    return Calc()


@pytest.mark.test_rectangle_perimeter
def test_rectangle_perimeter(calc):
    """
    Name: Artiom
    Function Name: test_rectangle_perimeter
    Description: Testing counting rectangle perimeter
    """
    try:
        shape = ast.literal_eval(os.getenv('RECTANGLE'))
        x = calc.rectangle_perimeter(shape)
        assert x is sum(shape)
        logger.info(
            f"{test_rectangle_perimeter.__doc__}\nActual: {x} Expected: {sum(shape)}\n")
    except Exception as e:
        logger.exception(f"{test_rectangle_perimeter.__doc__}{e}\n")
        raise


@pytest.mark.test_rectangle_area
def test_rectangle_area(calc):
    """
    Name: Artiom
    Function Name: test_rectangle_area
    Description: Testing counting rectangle area
    """
    try:
        shape = ast.literal_eval(os.getenv('RECTANGLE'))
        x = calc.rectangle_area(shape)
        assert x is 12
        logger.info(
            f"{test_rectangle_area.__doc__}\nActual: {x} Expected: {12}\n")
    except Exception as e:
        logger.exception(f"{test_rectangle_area.__doc__}{e}\n")
        raise


@pytest.mark.test_triangle_perimeter
def test_triangle_perimeter(calc):
    """
    Name: Artiom
    Function Name: test_triangle_perimeter
    Description: Testing counting triangle perimeter
    """
    try:
        shape = ast.literal_eval(os.getenv('TRIANGLE'))
        x = calc.triangle_perimeter(shape)
        assert x is sum(shape)
        logger.info(
            f"{test_triangle_perimeter.__doc__}\nActual: {x} Expected: {sum(shape)}\n")
    except Exception as e:
        logger.exception(f"{test_triangle_perimeter.__doc__}{e}\n")
        raise


@pytest.mark.test_triangle_area
def test_triangle_area(calc):
    """
    Name: Artiom
    Function Name: test_triangle_area
    Description: Testing counting triangle area
    """
    try:
        shape = ast.literal_eval(os.getenv('TRIANGLE'))
        x = calc.triangle_area(shape)
        assert type(x) is float and x > 0
        logger.info(
            f"{test_triangle_area.__doc__}\nActual: {x} Expected: {float and x > 0}\n")
    except Exception as e:
        logger.exception(f"{test_triangle_area.__doc__}{e}\n")
        raise
