#!/bin/bash

task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes/no):").lower()
priority = input("Priority (high/medium/low):").lower()

match priority:
    case "High":
        reminder = f"Reminder: '{task}' is of high priority."
    case "medium":
        reminder = f"Reminder: '{task}' is of medium priority."
    case "low":
        reminder = f"Reminder: '{task}' is of low priority."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level!"

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

