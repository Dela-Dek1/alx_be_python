#!/bin/bash

task = input("Enter the task description: ")
time_bound = input("Is the task time-bound? (yes or no): ")
priority = input("Enter the task's priority (high, medium, low): ")
match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority."
    case "medium":
        reminder = f"The task '{task}' is of medium priority."
    case "low":
        reminder = f"The task '{task}' is of low priority."
    case _:
        reminder = f"The task '{task}' is an unknown priority level."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
print(reminder)


