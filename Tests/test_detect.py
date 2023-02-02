import ast
import os
import pytest as pytest

from Shapes.detect import Detect
from dotenv import load_dotenv

from Tests.log import Log

# LOGGER
LOG = Log("__haifaytest__ ", "test_haifa_log.log")
logger = LOG.logger

@pytest.fixture
def detect():


    # ENV FILE
    load_dotenv('.env.test')

    # DETECT ClASS
    return Detect()


@pytest.mark.is_rectangle
def is_rectangle(detect):
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
            f"{is_rectangle.__doc__}\nActual: {x} Expected: {True}\n")
    except Exception as e:
        logger.exception(f"{is_rectangle.__doc__}{e}\n")
        raise
