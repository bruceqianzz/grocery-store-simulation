"""CSC148 Assignment 1: Tests for checkout classes

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the checkout classes.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jacqueline Smith

All of the files in this directory and all subdirectories are:
Copyright (c) 2019 Jacqueline Smith
"""
from store import RegularLine, ExpressLine, SelfServeLine, Customer, Item

# TODO: write your test functions for the checkout classes here


def test_checkout_basic() -> None:
    """check for basic value of attribute"""
    line1 = RegularLine(3)
    assert line1.capacity == 3
    assert line1.is_open is True
    assert line1.queue == []
    line2 = SelfServeLine(3)
    assert line2.capacity == 3
    assert line2.is_open is True
    assert line2.queue == []
    line3 = ExpressLine(3)
    assert line3.capacity == 3
    assert line3.is_open is True
    assert line3.queue == []


def test_checkout_can_accept_basic() -> None:
    """check for can accept"""
    customer1 = Customer("bruce", [])
    line1 = RegularLine(3)
    assert line1.can_accept(customer1) is True
    line2 = ExpressLine(3)
    assert line2.can_accept(customer1) is True
    line3 = SelfServeLine(3)
    assert line3.can_accept(customer1) is True


def test_checkout_cannot_accept_when_line_is_closed() -> None:
    """check if a customer can enter a line if line is closed"""
    customer1 = Customer("bruce", [])
    line1 = RegularLine(3)
    line1.is_open = False
    assert line1.can_accept(customer1) is False
    line2 = SelfServeLine(3)
    line2.is_open = False
    assert line2.can_accept(customer1) is False
    line3 = ExpressLine(3)
    line3.is_open = False
    assert line3.can_accept(customer1) is False


def test_checkout_cannot_accept_line_capacity_full() -> None:
    """check if a customer can enter a line if the line is full"""
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    line1 = RegularLine(2)
    assert line1.accept(customer2)
    assert line1.accept(customer3)
    assert line1.can_accept(customer1) is False
    assert customer1.arrival_time == -1
    assert line1.queue == [customer2, customer3]
    line2 = ExpressLine(2)
    assert line2.accept(customer2)
    assert line2.accept(customer3)
    assert line2.can_accept(customer1) is False
    assert customer2.arrival_time == -1
    assert line2.queue == [customer2, customer3]
    line3 = SelfServeLine(2)
    assert line3.accept(customer2)
    assert line3.accept(customer3)
    assert line3.can_accept(customer1) is False
    assert customer3.arrival_time == -1
    assert line3.queue == [customer2, customer3]


def test_express_line_accept_over_packaged() -> None:
    """check if a over packaged customer can enter in line """
    customer1 = Customer("bruce", [Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10),\
                                   Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10)])
    line1 = ExpressLine(2)
    assert line1.can_accept(customer1) is False
    assert line1.accept(customer1) is False
    assert customer1.arrival_time == -1
    assert line1.queue == []
    line2 = RegularLine(2)
    assert line2.can_accept(customer1) is True
    assert line2.accept(customer1) is True
    assert line2.queue == [customer1]
    line3 = SelfServeLine(2)
    assert line3.can_accept(customer1) is True
    assert line3.accept(customer1) is True
    assert line3.queue == [customer1]


def test_checkout_len_all_get_in_line() -> None:
    """test the length of a line"""
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    line1 = RegularLine(10)
    assert line1.accept(customer1) is True
    assert line1.accept(customer2) is True
    assert line1.accept(customer3) is True
    assert len(line1) == 3


def test_checkout_len_one_not_get_in_line() -> None:
    """check the length if some customer cannot get in line"""
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    line1 = RegularLine(2)
    assert line1.accept(customer1) is True
    assert line1.accept(customer2) is True
    assert line1.accept(customer3) is False
    assert len(line1) == 2


def test_regular_line_checkout_started() -> None:
    """check checkout started for regular line and express line"""
    customer1 = Customer("bruce", [Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10),
                                   Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10),
                                   Item("banana", 10)])
    customer2 = Customer("tom",[Item("banana", 10), Item("banana", 10)])
    line1 = RegularLine(3)
    assert line1.accept(customer1) is True
    assert line1.accept(customer2) is True
    assert line1.start_checkout() == 90
    line2 = ExpressLine(3)
    assert line2.accept(customer1) is False
    assert line2.accept(customer2) is True
    assert line2.start_checkout() == 20


def test_self_served_line_checkout_started() -> None:
    """test for checkout started for self serve line"""
    customer1 = Customer("bruce", [Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10),
                                   Item("banana", 10), Item("banana", 10), Item("banana", 10), Item("banana", 10),
                                   Item("banana", 10)])
    customer2 = Customer("tom", [Item("banana", 10), Item("banana", 10)])
    line1 = SelfServeLine(3)
    assert line1.accept(customer1) is True
    assert line1.accept(customer2) is True
    assert line1.start_checkout() == 180


def test_complete_checkout_no_customer_left() -> None:
    """check complete with no customer left"""
    customer1 = Customer("bruce", [Item("banana", 10)])
    line1 = RegularLine(3)
    assert line1.accept(customer1) is True
    assert line1.complete_checkout() is False
    line2 = ExpressLine(3)
    assert line2.accept(customer1) is True
    assert line2.complete_checkout() is False
    line3 = SelfServeLine(3)
    assert line3.accept(customer1) is True
    assert line3.complete_checkout() is False


def test_complete_checkout_two_people_in_line() -> None:
    """check for complete checkout with two people in line"""
    customer1 = Customer("bruce", [Item("banana", 10)])
    customer2 = Customer("tom", [Item("banana", 10)])
    line1 = RegularLine(3)
    assert line1.accept(customer1) is True
    assert line1.accept(customer2) is True
    assert line1.complete_checkout() is True
    line2 = ExpressLine(3)
    assert line2.accept(customer1) is True
    assert line2.accept(customer2) is True
    assert line2.complete_checkout() is True
    line3 = SelfServeLine(3)
    assert line3.accept(customer1) is True
    assert line3.accept(customer2) is True
    assert line3.complete_checkout() is True


def test_close_line_people_in_line() -> None:
    """check close line with people in line"""
    customer1 = Customer("bruce", [])
    customer2 = Customer("tom", [])
    customer3 = Customer("mary", [])
    line1 = RegularLine(3)
    assert line1.accept(customer1) is True
    assert line1.accept(customer2) is True
    assert line1.accept(customer3) is True
    assert line1.close() == [customer2, customer3]
    assert line1.is_open is False
    assert line1.queue == [customer1]
    assert line1.can_accept(customer2) is False
    line2 = ExpressLine(3)
    assert line2.accept(customer1) is True
    assert line2.accept(customer2) is True
    assert line2.accept(customer3) is True
    assert line2.close() == [customer2, customer3]
    assert line2.is_open is False
    assert line2.queue == [customer1]
    assert line2.can_accept(customer2) is False
    line3 = SelfServeLine(3)
    assert line3.accept(customer1) is True
    assert line3.accept(customer2) is True
    assert line3.accept(customer3) is True
    assert line3.close() == [customer2, customer3]
    assert line3.is_open is False
    assert line3.queue == [customer1]
    assert line3.can_accept(customer2) is False


def test_close_line_no_one_in_line() -> None:
    """check close line with no one in line"""
    line1 = RegularLine(3)
    assert line1.close() == []
    assert line1.is_open is False
    line2 = ExpressLine(3)
    assert line2.close() == []
    assert line2.is_open is False
    line3 = SelfServeLine(3)
    assert line3.close() == []
    assert line3.is_open is False


def test_close_line_one_customer_in_line() -> None:
    """check close line with one customer in line"""
    customer1 = Customer("bruce", [])
    line1 = RegularLine(3)
    assert line1.accept(customer1) is True
    assert line1.close() == []
    assert line1.is_open is False
    line2 = ExpressLine(3)
    assert line2.accept(customer1) is True
    assert line2.close() == []
    assert line2.is_open is False
    line3 = SelfServeLine(3)
    assert line3.accept(customer1) is True
    assert line3.close() == []
    assert line3.is_open is False


if __name__ == '__main__':
    import pytest
    pytest.main(['test_checkouts.py'])
