# study-scheduler
## Introduction

For my AI & ML BYOP capstone, I built the Smart Study Scheduler. It is a Python script that runs in the terminal to help figure out what to actually focus on before exams. Instead of just guessing what to study, the script uses the PEAS framework to act as a rational agent. It looks at how many days are left until a test and how confident the user is in that subject, and then it generates a prioritized, hour-by-hour study schedule.

## Features

•⁠ **The Urgency Formula:**  
It mathematically ranks subjects using a custom heuristic. It balances the time crunch of an upcoming exam against actual knowledge gaps.

•⁠ **Command Line Interface:**  
You can add subjects, test dates, and your current prep levels right in the terminal while the script is running.

•⁠ **Auto-Scheduling:**  
Once you tell it how many hours you have available to study today, it instantly prints out a customized timetable.

•⁠ **Pure Python:**  
I built this without relying on heavy external libraries like Pandas or NumPy. It runs natively on standard Python.

## Prerequisites

⁠You don't need to run any complex pip install commands to get this working.

•⁠ You just need Python 3.x installed on your computer.

•⁠ A standard terminal or IDE (like VS Code) to run the .py file.

## Code Structure

Here is a quick breakdown of how the logic works under the hood:

•⁠ **The Memory (study_list):**  
A global list of dictionaries that stores all the topics the user types in.

•⁠ **The Sensors (log_subject):**  
This function grabs the user input. It uses the datetime module to figure out exactly how many days are left until the exam date and appends everything to the list.

•⁠ **The Agent & Actuator (make_timetable):**  
This is where the actual AI logic happens. It loops through the syllabus and applies the priority formula: (5 - prep_level) / (days_left + 1). After calculating that, it sorts the list from most to least urgent and prints out the final study blocks.

**Author:** Priyanshu Choudhary  
**Registration Number:** 25BAI11225   

![WhatsApp Image 2026-03-31 at 23 24 05](https://github.com/user-attachments/assets/104ba320-3ef1-4184-b012-dbc5934d49ee)  

![WhatsApp Image 2026-03-31 at 23 24 04](https://github.com/user-attachments/assets/29736e9e-eaad-4a6f-a10c-7fd4a87355ee)


