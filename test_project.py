#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 18:50:10 2023
Purpose: CS50 Python Project Test Code
@author: roshanivijayan
"""
import pytest
from project import add_expense, total_expenses, category_expenses, get_category_by_choice

def test_get_category_by_choice():
    assert get_category_by_choice("1") == "Food"
    assert get_category_by_choice("2") == "Clothing"
    assert get_category_by_choice("3") == "Utility"
    assert get_category_by_choice("4") == "Miscellaneous"
    with pytest.raises(ValueError, match=".*numeric category number.*"):
        get_category_by_choice("5")

def test_add_expense():
    expense_list = []
    with pytest.raises(ValueError, match=".*amount.*"):
        with pytest.raises(OSError, match=".*reading from stdin.*"):
            add_expense(expense_list, "Food", "invalid_amount")

def test_get_category_by_choice_invalid_input():
    with pytest.raises(ValueError, match=".*choice.*"):
        get_category_by_choice("invalid_choice")

def test_add_expense_invalid_input():
    expense_list = []
    with pytest.raises(ValueError, match=".*amount.*"):
        add_expense(expense_list, "Clothing", "invalid_amount")

def test_total_expenses():
    expense_list = [
        {"category": "Food", "amount": 50.0},
        {"category": "Clothing", "amount": 30.0},
        {"category": "Utility", "amount": 100.0},
    ]
    total = total_expenses(expense_list)
    assert total == 180.0

def test_category_expenses():
    expense_list = [
        {"category": "Food", "amount": 50.0},
        {"category": "Clothing", "amount": 30.0},
        {"category": "Food", "amount": 20.0},
    ]
    category_total = category_expenses(expense_list, "Food")
    assert category_total == 70.0
