# Payroll System

A small Python program that works out what each staff member earns, built with classes and inheritance.

## What it does
- `Staff` is the parent class. It stores a name and a base salary, and has a `pay` method.
- `Teacher` and `Driver` inherit from `Staff`. Each overrides `pay` to add a bonus: 500 per class taught for a teacher, 500 per trip for a driver.
- A base salary of zero or less is refused with a `ValueError`. The check is in `Staff`, so teachers and drivers are covered too.
- A loop goes through a list of staff and calls `pay` on each one without checking which kind it is (polymorphism).

## How to run it
Run `payroll.py` with Python (I run it in Pydroid on my phone). It prints each person's name and pay, for example:

Ada earns 10
Austin earns 2600
Tunde earns 2000

## What I will improve next (version 2)
- Ask the admin for each staff member's name, base salary and the extra (classes or trips), instead of fixed values in the file
- Ask for the bonus rate, so the 500 is no longer typed in two places
- Add a currency label (naira or dollars) to the output, as a label only with no conversion
- Handle bad input with `try`, `except ValueError` and `else`, and show the error message
- Tidy the indents and label the output lines

## What I learned
Inheritance, `super()`, overriding, raising errors, and polymorphism.
