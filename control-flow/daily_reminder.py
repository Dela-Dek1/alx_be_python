#!/bin/bash

task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes/no):").lower()
priority = input("Priority (high/medium/low):").lower()

match priority:
    case "high":
        reminder = f"The task '{task}' is of high priority."
    case "medium":
        reminder = f"The task '{task}' is of medium priority."
    case "low": 
        reminder = f"The task '{tsk}' is of low priority."
    case _:
        reminder = f"The task '{task}' has an unknown priority level."

if time_bound == "yes":
    rerminder += " It requires immediate attention today!"
prin(f"Reminder: {reminder}")

