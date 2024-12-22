#!/bin/bash

task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes/no):")
priority = input("Priority (high/medium/low):")

match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority."
        print("Reminder: ", reminder)
    case "medium":
        reminder = f"The task '{task}' is of medium priority."
        print("Reminder: ", reminder)
    case "low":
        reminder = f"The task '{task}' is of low priority."
        print("Note: ", reminder)
    case _:
        reminder = f"The task '{task}' has an unknown priority level."
        print("Oops!: ", reminder)

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
    print("Reminder: ', reminders)


