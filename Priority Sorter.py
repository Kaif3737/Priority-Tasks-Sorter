tasks = []

# Input tasks
while True:
    task = input("Enter the task (enter 'quit' or enter to stop): ").strip().capitalize()
    if task.lower() == 'quit' or task == '':
        break
    tasks.append(task)

# Input priorities
print ("\nNow, assign priorities to the tasks (1 being the highest priority).")
print("These are your tasks: ")
for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")
    
tasks_with_priorities = {}

for task in tasks:

    while True:
        try:
            priority = int(input(f"Enter the priority for '{task}': "))
            if priority < 1 or priority > len(tasks):
                print("Priority must be a positive integer and smaller than or equal to the number of tasks. Please try again.")
                continue
            tasks_with_priorities[task] = priority
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

# Sort tasks by priority
sorted_tasks = sorted(tasks_with_priorities.items(), key=lambda x: x[1])

# Display sorted tasks
print("\nTasks sorted by priority:")
for task, priority in sorted_tasks:
    print(f"Task: {task}, Priority: {priority}")