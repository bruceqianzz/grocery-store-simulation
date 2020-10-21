"""CSC148 Assignment 1: Tests for GroceryStore

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the GroceryStore class.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Jacqueline Smith
"""
from io import StringIO
from store import GroceryStore, RegularLine, ExpressLine, SelfServeLine, Customer, Item

# TODO: write your test functions for GroceryStore here
# Note - your tests should use StringIO to simulate opening a configuration file
# rather than requiring separate files.
# See the Assignment 0 sample test for an example of using StringIO in testing.

CONFIG_FILE = '''{
  "regular_count": 2,
  "express_count": 1,
  "self_serve_count": 1,
  "line_capacity": 2
}
'''


def test_enter_line() -> None:
    """check if people can enter line correctly"""
    store1 = GroceryStore(StringIO(CONFIG_FILE))
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    customer4 = Customer("a", [])
    customer5 = Customer("b", [])
    customer6 = Customer("c", [])
    customer7 = Customer("d", [])
    customer8 = Customer("e", [])
    customer9 = Customer("f", [])
    assert store1.enter_line(customer1) == 0
    assert store1.enter_line(customer2) == 1
    assert store1.enter_line(customer3) == 2
    assert store1.enter_line(customer4) == 3
    assert store1.enter_line(customer5) == 0
    assert store1.enter_line(customer6) == 1
    assert store1.enter_line(customer7) == 2
    assert store1.enter_line(customer8) == 3
    assert store1.enter_line(customer9) == -1


def test_enter_line1() -> None:
    """check if people can enter line correctly."""
    store = GroceryStore(StringIO(CONFIG_FILE))
    customer1 = Customer('bruce', [])
    customer2 = Customer('jerry', [])
    customer3 = Customer('tom', [Item('banana', 1), Item('banana', 1), Item('banana', 1),
                                 Item('banana', 1), Item('banana', 1), Item('banana', 1),
                                 Item('banana', 1), Item('banana', 1)])
    customer4 = Customer('mary', [])
    assert store.enter_line(customer1) == 0
    assert store.enter_line(customer2) == 1
    assert store.enter_line(customer3) == 3
    assert store.enter_line(customer4) == 2


CONFIG_FILE2 = '''{
      "regular_count": 1,
      "express_count": 1,
      "self_serve_count": 0,
      "line_capacity": 1
    }
    '''


def test_enter_line2() -> None:
    """check if people can enter line correctly."""
    store = GroceryStore(StringIO(CONFIG_FILE2))
    customer1 = Customer('bruce', [])
    customer2 = Customer('tom', [Item('banana', 1), Item('banana', 1), Item('banana', 1),
                                 Item('banana', 1), Item('banana', 1), Item('banana', 1),
                                 Item('banana', 1), Item('banana', 1)])
    customer3 = Customer('jerry', [])
    customer4 = Customer('mary', [])
    assert store.enter_line(customer1) == 0
    assert store.enter_line(customer2) == -1
    assert store.enter_line(customer3) == 1
    assert store.enter_line(customer4) == -1


def test_cannot_enter_line() -> None:
    """test for when the line capacity is full"""
    store1 = GroceryStore(StringIO(CONFIG_FILE2))
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    assert store1.enter_line(customer1) == 0
    assert store1.enter_line(customer2) == 1
    assert store1.enter_line(customer3) == -1
    assert customer3.arrival_time == -1


def test_line_is_ready() -> None:
    """check the method of line is ready"""
    store1 = GroceryStore(StringIO(CONFIG_FILE2))
    customer1 = Customer("bruce", [])
    assert store1.line_is_ready(0) is False
    assert store1.line_is_ready(1) is False
    assert store1.enter_line(customer1) == 0
    assert store1.line_is_ready(0) is True
    assert store1.line_is_ready(1) is False


def test_start_checkout_normal_line() -> None:
    """check the checkout for normal line"""
    store1 = GroceryStore(StringIO(CONFIG_FILE2))
    item1 = Item("banana", 10)
    item2 = Item("apple", 2)
    item3 = Item("orange", 9)
    customer1 = Customer("bruce", [item1, item2, item3])
    customer2 = Customer("tom", [item1, item2, item3])
    assert store1.enter_line(customer1) == 0
    assert store1.start_checkout(0) == 21
    assert store1.enter_line(customer2) == 1
    assert store1.start_checkout(1) == 21


CONFIG_FILE3 = '''{
          "regular_count": 0,
          "express_count": 0,
          "self_serve_count": 3,
          "line_capacity": 1
        }
        '''


def test_start_checkout_self_serve_line() -> None:
    """check for the checkout method for self serve line"""
    store1 = GroceryStore(StringIO(CONFIG_FILE3))
    item1 = Item("banana", 10)
    item2 = Item("apple", 2)
    item3 = Item("orange", 9)
    customer1 = Customer("bruce", [item1, item2, item3])
    assert store1.enter_line(customer1) == 0
    assert store1.start_checkout(0) == 42


CONFIG_FILE4 = '''{
          "regular_count": 1,
          "express_count": 1,
          "self_serve_count": 0,
          "line_capacity": 4
        }
        '''


def test_complete_checkout_with_customer_behind() -> None:
    """check complete with customers behind"""
    store1 = GroceryStore(StringIO(CONFIG_FILE4))
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    customer4 = Customer("jams", [])
    customer5 = Customer("jerry", [])
    assert store1.enter_line(customer1) == 0
    assert store1.enter_line(customer2) == 1
    assert store1.enter_line(customer3) == 0
    assert store1.enter_line(customer4) == 1
    assert store1.enter_line(customer5) == 0
    assert store1.complete_checkout(0) == 2
    assert store1.complete_checkout(1) == 1


def test_complete_checkout_no_customer_behind() -> None:
    """check for the checkout method with no customer behind"""
    store1 = GroceryStore(StringIO(CONFIG_FILE4))
    customer1 = Customer("bruce", [])
    assert store1.enter_line(customer1) == 0
    assert store1.complete_checkout(0) == 0


def test_close_line_people_in_line() -> None:
    """check close line with people in line"""
    store1 = GroceryStore(StringIO(CONFIG_FILE4))
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    assert store1.enter_line(customer1) == 0
    assert store1.enter_line(customer2) == 1
    assert store1.enter_line(customer3) == 0
    assert store1.close_line(0) == [customer3]
    assert store1.close_line(1) == []


def test_close_line_no_people_in_line() -> None:
    """check close line with no people in line"""
    store1 = GroceryStore(StringIO(CONFIG_FILE4))
    assert store1.close_line(0) == []


def test_get_first_in_line() -> None:
    """check get first method"""
    store1 = GroceryStore(StringIO(CONFIG_FILE4))
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    assert store1.enter_line(customer1) == 0
    assert store1.enter_line(customer2) == 1
    assert store1.enter_line(customer3) == 0
    assert store1.get_first_in_line(0) == customer1
    assert store1.get_first_in_line(1) == customer2


def test_get_first_in_line_no_one_in_line() -> None:
    """che get first method with no person in line"""
    store1 = GroceryStore(StringIO(CONFIG_FILE4))
    assert store1.get_first_in_line(0) is None


CONFIG_FILE5 = '''{
          "regular_count": 0,
          "express_count": 0,
          "self_serve_count": 0,
          "line_capacity": 2
        }
        '''


def test_no_line_is_open() -> None:
    """check when there is no line open"""
    store1 = GroceryStore(StringIO(CONFIG_FILE5))
    customer1 = Customer("bruce", [])
    assert store1.enter_line(customer1) == -1


if __name__ == '__main__':
    import pytest
    pytest.main(['test_grocerystore.py'])
