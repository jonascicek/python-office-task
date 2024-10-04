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

def remove_task():
    task = input ("Please enter the completed task")
    officetasklist.remove(task)
    print(f"{task}removed from your tasklist.")

# Main function

def main():
    while True:
        print("---Your tasklist---")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Show tasklist")
        print("4. Exit tasklist")

    # Save the input from the User with the choice variable

        choice = input("Please enter (1/2/3/4)")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasklist()
        elif choice == "4":
            print("Closing Tasklist! Good Bye!")
            break
        else:
            print("Invalid input. Please type 1, 2, 3 or 4")

if __name__ == "__main__":
    main()

