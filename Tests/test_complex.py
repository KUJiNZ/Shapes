import ast
import os
import pytest

from Shapes.complex import Complex
from dotenv import load_dotenv

from Tests.log import Log

# LOGGER
LOG = Log("__complex__ ", "complex_log.log")
logger = LOG.logger


@pytest.fixture
def complex():
    # ENV FILE
    load_dotenv('.env.test')

    # COMPLEX ClASS
    return Complex()


@pytest.mark.test_shape
def test_shape(complex):
    """
    Name: Artiom
    Function Name: test_shape
    Description: Testing if function gets list of dictionary of shapes and returning proper shapes dictionary
    """
    try:
        shapes = ast.literal_eval(os.getenv('SHAPES'))
        x = complex.shape(shapes)
        assert type(x) is list and x is not None
        logger.info(
            f"{test_shape.__doc__}\nActual: {x} Expected: is list of and x is not None\n")
    except Exception as e:
        logger.exception(f"{test_shape.__doc__}{e}\n")
        raise


@pytest.mark.test_clean_duplicates
def test_clean_duplicates(complex):
    """
    Name: Artiom
    Function Name: test_clean_duplicates
    Description: Testing if function gets list of dictionary of shapes and cleans dups
    """
    try:
        shapes = ast.literal_eval(os.getenv('SHAPES'))
        expected = ast.literal_eval(os.getenv('NO_DUPS_SHAPES'))
        x = complex.clean_duplicates(shapes)
        assert x == expected
        logger.info(
            f"{test_clean_duplicates.__doc__}\nActual: {x} Expected: {expected} \n")
    except Exception as e:
        logger.exception(f"{test_clean_duplicates.__doc__}{e}\n")
        raise
