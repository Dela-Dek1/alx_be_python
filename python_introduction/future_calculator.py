#!/bin/bash
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter youy total monthly expenses: "))
monthly_savings = monthly_income - monthly expenses
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are: ${monthly_savings: .2f}")
print(f"Your projrcted annual savings after interest are: ${annual_savings:.2f}")

