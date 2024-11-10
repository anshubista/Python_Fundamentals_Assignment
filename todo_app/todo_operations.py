def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def delete_task(tasks, index):
    try:
        task = tasks.pop(index - 1)
        print(f"Task '{task}' deleted.")
    except IndexError:
        print("Invalid index. Please try again.")
