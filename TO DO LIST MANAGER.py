import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
             return json.load(file)
    except:
        return {"tasks": []}

def create_tasks(tasks):
    description = input("Enter task description: ")
    if description:
        tasks["tasks"].append({"description": description , "complete": False})
        save_tasks(tasks)
        print("Task added")
    else:
        print("Task description can't be empty")

def mark_tasks(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark: "))
        if 1 <= task_number <= len(tasks["tasks"]):
           tasks["tasks"][task_number - 1]["complete"] = True
           save_tasks(tasks)
           print("Task marked as complete")
        else:
            print("Invalid task number")
    except:
           print("Enter valid task number")


def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks added")
    else:
        print("To do list:")
        for idx, task in enumerate(task_list):
            status = "completed" if task["complete"] else "not completed"
            print(f"{idx + 1}. {task['description']} | {status}")


def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
             json.dump(tasks, file)
    except:
        print("failed to save")


def main():
    tasks = load_tasks()

    while True:
        print("TO DO LIST MANAGER")
        print("1. Create new task")
        print("2. Mark tasks")
        print("3. View tasks")
        print("4. Save tasks")
        print("5. Exit")


        choice = input("Enter your choice: ")
        if choice == "1":
            create_tasks(tasks)
        elif choice == "2":
            mark_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
        elif choice == "5":
            exit()
        else:
            print("invalid option")
            continue

main()
