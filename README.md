# CPRG 217 - Scripting

Welcome to the CPRG 217 Scripting course! This course is designed to take your basic Python knowledge learned from CPRG 216 and apply it to practical scripting tasks, focusing on automation, system interaction, data processing, and error handling.

## Course Overview

This course will guide you through the process of building robust Python scripts for real-world applications. You will learn how to interact with operating systems (Linux and Windows), handle data effectively, manage errors gracefully, schedule tasks, and even integrate with automation tools like Ansible. By the end of this course, you will be equipped to automate repetitive tasks, manage system configurations, and build powerful scripting tools.

## Presentations

https://sait-its.github.io/cprg-217/index.html

## Resources and Discussions

https://github.com/sait-its/awesome-cprg-217

https://github.com/sait-its/awesome-cprg-217/discussions

## Textbooks

- [Automate the Boring Stuff with Python, 2nd Edition (free online ebook)](https://automatetheboringstuff.com/)
- [Python Crash Course, 3rd Edition](https://nostarch.com/python-crash-course-3rd-edition)

## Recommended Resources

- [Beyond the Basic Stuff with Python (free online ebook)](https://inventwithpython.com/beyond/)
- [Real Python Tutorials](https://realpython.com/)

## Prerequisites

Before starting this course, you should have a solid understanding of Python fundamentals from CPRG 216, including:

*   Basic Python syntax
*   Variables and data types (strings, integers, floats, booleans)
*   Control flow (if/elif/else statements)
*   Loops (for and while loops)
*   Functions (defining and calling functions)
*   Basic understanding of Classes and Objects

Familiarity with using a command-line interface (Terminal in Linux/macOS or Command Prompt/PowerShell in Windows) is also recommended.

## Learning Units

---

### **Unit 1: Scripting Fundamentals**

Get started with the essentials of Python scripting.

*   What is a Scripting Language
*   Setting up a Python Development  environment.
*   Writing and running your first Python scripts.
*   Understanding scripting interfaces (command-line arguments).
*   Reading and examining text file contents using Python.
*   Executing basic Linux commands from within Python scripts.
*   Reviewing common programming components and best practices.

[Unit 1 Slides](https://sait-its.github.io/cprg-217/cprg-217-unit-01.html)

[Unit 1 Resources](./unit-01/unit-01.md)

---

### **Unit 2: Error Handling**

Learn how to make your scripts more reliable by anticipating and handling errors.

*   Interpreting Python error messages (tracebacks).
*   Identifying potential runtime errors in your code.
*   Validating user input to prevent errors.
*   Implementing error handling using `try`, `except`, and `finally` blocks.
*   Raise and handle exceptions.
*   Error Handling strategies (LBYL and EAFP).

[Unit 2 Slides](https://sait-its.github.io/cprg-217/cprg-217-unit-02.html)

[Unit 2 Resources](./unit-02/unit-02.md)

---

### **Unit 3: Data Processing and Organization**

Master techniques for working with data within your scripts.

*   Choosing appropriate data structures (lists, dictionaries, sets, tuples) for data collection.
*   Filtering data based on specific criteria.
*   Sorting data effectively.
*   Structuring code with well-defined functions for data processing tasks.
*   Understanding key terminology and concepts related to data types and data structures.
*   Working with JSON.

[Unit 3 Slides](https://sait-its.github.io/cprg-217/cprg-217-unit-03.html)

---

### **Unit 4: Automating Linux System Tasks**

Dive into interacting with the Linux operating system using Python.

*   Understanding the structure and key features of the Linux OS.
*   Contrasting Linux and Windows environments from a scripting perspective.
*   Identifying important configuration and system files in Linux.
*   Developing Python scripts to:
    *   Gather system information (CPU, memory, disk usage).
    *   Execute common Linux system administration tasks.

---

### **Unit 5: Automating Windows System Tasks**

Learn how to perform system administration tasks on Windows using Python.

*   Understanding the structure and key features of the Windows OS.
*   Introduction to the `pywin32` library for Windows automation.
*   Identifying appropriate `pywin32` modules and methods for specific tasks.
*   Developing Python scripts to:
    *   Gather Windows system information.
    *   Execute Windows system administration tasks.

---

### **Unit 6: Scheduling Automated Tasks**

Make your scripts run automatically at specific times or intervals.

*   Defining parameters required for scheduled tasks.
*   Understanding Task Scheduler in Windows.
*   Understanding the `Crontab` utility in Linux.
*   Outlining the steps to create and manage `Cron` jobs.
*   Creating scheduled tasks in `Crontab` using or for Python scripts.

---

### **Unit 7: Scalable Automation and Networking**

Build more complex and scalable automation solutions.

*   Using configuration files (e.g., INI, JSON, YAML) to manage script settings.
*   Introduction to Socket Programming in Python for network communication.
*   Understanding the principles of sending information between systems.
*   Developing scripts that run in sequence based on programming logic.
*   Setting up and running a series of scheduled scripts automatically.

---

### **Unit 8: Introduction to Configuration Management with Ansible**

Integrate Python scripting with a powerful automation engine.

*   Understanding the architecture and core concepts of Ansible.
*   Defining the components of an Ansible automation workflow (playbooks, inventory, modules).
*   Exploring `ansible-core` and how Python interacts with it.
*   Configuring and controlling Ansible tasks using Python scripts.

---

## Tools and Environment

*   **Python 3.10+:** Ensure you have a recent version of Python 3 installed.
*   **Python package management tools:** pip, uv.
*   **Python virtual environments:** venv, uv.
*   **Text Editor/IDE:** A good editor like VS Code, PyCharm, Sublime Text, or NeoVim is recommended.
*   **Terminal Emulator:** Windows Terminal, WezTerm, kitty, Ghostty, iTerm2.
*   **Operating Systems:** Access to both a Linux environment (physical machine, or VM in VMware Workstaion) and a Windows environment will be necessary to complete all units.
*   **Required Libraries:** Specific Python libraries like `os`, `sys`, `subprocess`, `json`, `pywin32` (for Windows), `socket`, and potentially Ansible-related Python libraries will be used.

Happy Scripting!