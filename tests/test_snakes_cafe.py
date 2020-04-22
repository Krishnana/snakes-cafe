from snakes_cafe import __version__
from snakes_cafe.snakes_cafe import welcome_customer
from snakes_cafe.snakes_cafe import menu
from snakes_cafe.snakes_cafe import get_order
from textwrap import dedent
from unittest.mock import patch
import builtins

def test_version():
    assert __version__ == '0.1.0'

def test_invalid_order():
    expected_welcome_message = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    assert welcome_customer() == dedent(expected_welcome_message)

def test_menu():
    expected_menu = """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tear
    """
    assert menu() == dedent(expected_menu)

def test_get_same_orders():
    expected_orders =  {
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,
    "Ice Cream":0,
    "Cake":0,
    "Pie":0,
    "Coffee": 2,
    "Tea":0,
    "Unicorn Tear":0
    }
    with patch.object(builtins, 'input', side_effect=['coffee','coffee','quit']):
        result = get_order()
        assert result == expected_orders

def test_get_different_orders():
    expected_orders =  {
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,
    "Ice Cream":0,
    "Cake":1,
    "Pie":0,
    "Coffee": 3,
    "Tea":0,
    "Unicorn Tear":0
    }
    with patch.object(builtins, 'input', side_effect=['Coffee','caKe','quit']):
        result = get_order()
        assert result == expected_orders

def test_get_orders_case_sensitivity():
    expected_orders =  {
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,
    "Ice Cream":0,
    "Cake":1,
    "Pie":0,
    "Coffee": 3,
    "Tea":1,
    "Unicorn Tear":0
    }
    with patch.object(builtins, 'input', side_effect=['tEA','notinList','quit']):
        result = get_order()
        assert result == expected_orders         