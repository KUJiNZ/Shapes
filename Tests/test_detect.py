import ast
import os
import pytest

from Shapes.detect import Detect
from dotenv import load_dotenv

from Tests.log import Log

# LOGGER
LOG = Log("__detect__ ", "detect_log.log")
logger = LOG.logger


@pytest.fixture
def detect():
    # ENV FILE
    load_dotenv('.env.test')

    # DETECT ClASS
    return Detect()


@pytest.mark.test_is_rectangle
def test_is_rectangle(detect):
    """
    Name: Artiom
    Function Name: is_rectangle
    Description: Testing if shape is_rectangle
    """
    try:
        shape = ast.literal_eval(os.getenv('RECTANGLE'))
        x = detect.is_rectangle(shape)
        assert x is True
        logger.info(
            f"{test_is_rectangle.__doc__}\nActual: {x} Expected: {True}\n")
    except Exception as e:
        logger.exception(f"{test_is_rectangle.__doc__}{e}\n")
        raise


@pytest.mark.test_is_square
def test_is_square(detect):
    """
    Name: Artiom
    Function Name: is_rectangle
    Description: Testing if shape is_square
    """
    try:
        shape = ast.literal_eval(os.getenv('SQUARE'))
        x = detect.is_square(shape)
        assert x is True
        logger.info(
            f"{test_is_square.__doc__}\nActual: {x} Expected: {True}\n")
    except Exception as e:
        logger.exception(f"{test_is_square.__doc__}{e}\n")
        raise

@pytest.mark.test_is_triangle
def test_is_triangle(detect):
    """
    Name: Artiom
    Function Name: is_triangle
    Description: Testing if shape is_square
    """
    try:
        shape = ast.literal_eval(os.getenv('TRIANGLE'))
        x = detect.is_triangle(shape)
        assert x is True
        logger.info(
            f"{test_is_triangle.__doc__}\nActual: {x} Expected: {True}\n")
    except Exception as e:
        logger.exception(f"{test_is_triangle.__doc__}{e}\n")
        raise