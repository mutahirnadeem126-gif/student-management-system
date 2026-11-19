# Student Management System (Python CLI)

A menu-driven command-line application built in Python to manage student records with persistent JSON storage, automatic grade calculation, and full input validation.

## Features

- **CRUD Operations:** Add, view, search, update, and delete student records.
- **Automatic Grading:** Assigns grades (`A` to `F`) automatically based on marks.
- **Persistent Storage:** Saves all data in `students.json` so records remain intact after closing the program.
- **Input Validation & Error Handling:** Prevents duplicate IDs, restricts marks to `0–100`, and handles non-numeric inputs gracefully without crashing.

## Grading Criteria

| Marks Range | Grade |
| :--- | :---: |
| 80 – 100 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| Below 50 | F |

## Project Structure

```text
student-management-system/
├── main.py          # Main application code
├── students.json    # Auto-generated JSON database
└── README.md        # Project documentation