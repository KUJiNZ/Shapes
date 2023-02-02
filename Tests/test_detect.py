import ast
import os

import pytest as pytest

from Shapes.complex import Complex
from dotenv import load_dotenv
from Tests.log import Log

# LOGGER
LOG = Log("__haifaytest__ ", "test_haifa_log.log")
logger = LOG.logger


@pytest.fixture
def haifa():
    # ENV FILE
    load_dotenv('.env.test')
    kitchen_type = os.getenv('KITCHEN_TYPE_HAIFA')
    # HAIFA ClASS
    rooms = ast.literal_eval(os.getenv('ROOMS_HERZ'))
    return Complex


@pytest.mark.haifa_test_setter_kitchen
def test_setter_kitchen(haifa):
    """
    Name: Artiom
    Function Name: kitchen
    Description: Testing setter of kitchen in class AprtmHaifa
    """
    try:
        haifa._kitchen = os.getenv('KITCHEN_TYPE_HERZ')
        assert haifa._kitchen is os.getenv('KITCHEN_TYPE_HERZ')
        logger.info(
            f"{test_setter_kitchen.__doc__}\nActual: {haifa._kitchen} Expected: {os.getenv('KITCHEN_TYPE_HERZ')}\n")
    except Exception as e:
        logger.exception(f"{test_setter_kitchen.__doc__}{e}\n")
        raise