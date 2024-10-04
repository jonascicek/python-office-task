# python-office-task

# Empty officetasklist
officetasklist = []

# Add task function

def add_task():
    task = input ("Please enter a task to be added to your task list")
    officetasklist.append(task)
    print(f"{task}has been added to your task list")

# Show tasklist function

def show_tasklist():
    if officetasklist:
        print("Your tasklist:")
        for task in officetasklist:
            print(f"{task}")
    else:
        print("Your tasklist is empty.")