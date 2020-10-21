"""CSC148 Assignment 1: Tests for Customer

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the Customer class.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Jacqueline Smith
"""
from store import Customer, Item

# TODO: write your test functions for Customer here


def test_customer_no_item() -> None:
    """test for customer with no item"""
    customer1 = Customer("bruce", [])
    assert customer1.name == "bruce"
    assert customer1.arrival_time == -1
    assert customer1._items == []


def test_customer_one_item() -> None:
    """check for customer with one item"""
    item1 = Item("banana",10)
    customer1 = Customer("bruce", [item1])
    assert customer1.name == "bruce"
    assert customer1.arrival_time == -1
    assert customer1._items == [item1]


def test_customer_multi_item() -> None:
    """check for customer with several items"""
    item1 = Item("banana", 10)
    item2 = Item("apple", 2)
    item3 = Item("orange", 9)
    customer1 = Customer("bruce", [item1, item2, item3])
    assert customer1.name == "bruce"
    assert customer1.arrival_time == -1
    assert customer1._items == [item1, item2, item3]


def test_customer_num_items_with_no_item() -> None:
    """check num item method with no item"""
    customer1 = Customer("bruce", [])
    assert customer1.arrival_time == -1
    assert customer1.num_items() == 0


def test_customer_num_items_with_one_item() -> None:
    """check num item method with one item"""
    item1 = Item("banana", 10)
    customer1 = Customer("bruce", [item1])
    assert customer1.num_items() == 1


def test_customer_num_items_with_multi_item() -> None:
    """check num item method with several items"""
    item1 = Item("banana", 10)
    item2 = Item("apple", 2)
    item3 = Item("orange", 9)
    customer1 = Customer("bruce", [item1, item2, item3])
    assert customer1.num_items() == 3


def test_get_item_time_with_no_item() -> None:
    """check get item time method with no item"""
    customer1 = Customer("bruce", [])
    assert customer1.get_item_time() == 0


def test_get_item_time_with_one_item() -> None:
    """check get item time method with one item"""
    item1 = Item("banana", 10)
    customer1 = Customer("bruce", [item1])
    assert customer1.get_item_time() == 10


def test_get_item_time_with_multi_item() -> None:
    """check get item time method with several items"""
    item1 = Item("banana", 10)
    item2 = Item("apple", 2)
    item3 = Item("orange", 9)
    customer1 = Customer("bruce", [item1, item2, item3])
    assert customer1.get_item_time() == 21


if __name__ == '__main__':
    import pytest
    pytest.main(['test_customer.py'])
