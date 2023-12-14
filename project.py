#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Name : Budget Tracker
Purpose: CS50 Python Project
Created on Thu Dec 13 17:41:20 2023
@author: roshanivijayan
"""
def main():
    """
    Main function to run the Budget Tracker.
    """
    expense_list = []
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Expense - Food")
        print("2. Add Expense - Clothing")
        print("3. Add Expense - Utility")
        print("4. Add Expense - Miscellaneous")
        print("5. View Total Expenses")
        print("6. View Category Expenses")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_expense(expense_list, "Food", float(input("Enter expense amount for Food: ")))
        elif choice == "2":
            add_expense(expense_list, "Clothing", float(input("Enter expense amount for Clothing: ")))
        elif choice == "3":
            add_expense(expense_list, "Utility", float(input("Enter expense amount for Utility: ")))
        elif choice == "4":
            add_expense(expense_list, "Miscellaneous", float(input("Enter expense amount for Miscellaneous: ")))
        elif choice == "5":
            total = total_expenses(expense_list)
            print(f"Total Expenses: ${total:.2f}")
            input("Press Enter to continue...")
        elif choice == "6":
            print("\nExpense Categories:")
            display_categories()
            category_choice = input("Enter category to view expenses (1-5): ")
            if category_choice == "5":
                continue  # Go back to the main menu
            category = get_category_by_choice(category_choice)
            category_total = category_expenses(expense_list, category)
            print(f"Total Expenses for {category}: ${category_total:.2f}")
            input("Press Enter to continue...")
        elif choice == "7":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            input("Press Enter to continue...")

def add_expense(expense_list, category, amount):
    """
    Add an expense to the expense list.
    """
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid numeric amount.")
    if amount < 0:
        raise ValueError("Amount must be a non-negative value.")
    expense_list.append({"category": category, "amount": amount})
    print(f"{category} expense added successfully!")
    input("Press Enter to continue...")

def total_expenses(expense_list):
    """
    Calculate the total expenses.
    Parameters:
    - expense_list: List containing expenses.
    Returns:
    - total: Total expenses.
    """
    total = sum(item["amount"] for item in expense_list)
    return total

def category_expenses(expense_list, category):
    """
    Calculate the total expenses for a specific category.
    Parameters:
    - expense_list: List containing expenses.
    - category: Category for which to calculate expenses.
    Returns:
    - category_total: Total expenses for the specified category.
    """
    category_total = sum(item["amount"] for item in expense_list if item["category"].lower() == category.lower())
    return category_total

def get_category_by_choice(choice):
    """
    Get the category based on the user's choice.
    Parameters:
    - choice: User's choice as input.
    Returns:
    - category: Corresponding category.
    """
    categories = ["Food", "Clothing", "Utility", "Miscellaneous"]
    try:
        index = int(choice) - 1
        if 0 <= index < len(categories):
            return categories[index]
        else:
            raise ValueError("Invalid choice. Please enter a valid category number.")
    except ValueError:
        raise ValueError("Invalid choice. Please enter a valid numeric category number.")

def display_categories():
    """
    Display the expense categories.
    """
    categories = ["Food", "Clothing", "Utility", "Miscellaneous"]
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

if __name__ == "__main__":
    main()
