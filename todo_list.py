""" Author: Marvin Aguilar """
""" A small Python script for a to-do list """
""" CRUD (Create, Replace, Update, Delete) """

import os

# Function to load tasks from a file
def load_tasks(filename):
    if not os.path.exists(filename):
        with open(filename, "w"):
            pass

    tasks = []
    with open(filename, "r") as file:
        tasks = file.read().splitlines()
    return tasks


# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        file.write("\n".join(tasks))


# Function to add a task
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")


# Function to remove a task
def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


# Function to mark a task as complete
def complete_task(tasks, task):
    if task in tasks:
        index = tasks.index(task)
        tasks[index] = f"{task} (Completed)"
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("╔══════════════════ To-Do List ══════════════════╗")
        for i, task in enumerate(tasks, start=1):
            task_display = f"║ {i}. {task}"
            if "(Completed)" in task:
                print(task_display.ljust(48) + " ║")
            else:
                print(task_display.ljust(48) + " ║")
        print("╚════════════════════════════════════════════════╝")
    else:
        print("Your to-do list is empty. 📋")


# Function to press enter to continue and clear the console
def press_enter_to_continue():
    input("\nPress [Enter] to continue...")
    clear_console()


# Function to clear the console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    filename = "todo.txt"
    tasks = load_tasks(filename)

    while True:
        clear_console()
        display_tasks(tasks)
        print("\nOptions:")
        print("1. ➕ Add Task")
        print("2. ➖ Remove Task")
        print("3. ✅ Mark Task as Complete")
        print("4. 🚪 Save and Exit")

        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        print("\n")

        if choice == "1":
            task = input("Enter the task to add: ").strip()
            add_task(tasks, task)
        elif choice == "2":
            task = input("Enter the task to remove: ").strip()
            remove_task(tasks, task)
        elif choice == "3":
            task = input("Enter the task to mark as complete: ").strip()
            complete_task(tasks, task)
        elif choice == "4":
            save_tasks(filename, tasks)
            print("Your to-do list has been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        press_enter_to_continue()


if __name__ == "__main__":
    main()
