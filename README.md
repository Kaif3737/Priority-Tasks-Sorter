# Priority Task Sorter

## Description
A simple Python program that sorts a list of tasks by user-assigned priority. Users input tasks and assign a priority number (1 = highest). The program outputs the tasks ranked from highest to lowest priority.

## How to Use
1. Run the script.
2. Enter your tasks one by one. Press **Enter** or type **quit** to stop.
3. Enter a priority for each task (1 = highest). The program checks that the input is valid.
4. The program displays your tasks sorted by priority.

## Features
- Input validation to ensure priorities are numbers within the correct range.
- Automatically sorts tasks using Python’s `sorted` function and `lambda`.
- Easy to use for any number of tasks.

## Demo

**Example Input:**
```python
Enter the task (enter 'quit' or enter to stop): Homework
Enter the task (enter 'quit' or enter to stop): Laundry
Enter the task (enter 'quit' or enter to stop): Shopping
Enter the task (enter 'quit' or enter to stop): quit

Now, assign priorities to the tasks (1 being the highest priority).
Enter the priority for 'Homework': 2
Enter the priority for 'Laundry': 3
Enter the priority for 'Shopping': 1

Example Output:

Tasks sorted by priority:
Task: Shopping, Priority: 1
Task: Homework, Priority: 2
Task: Laundry, Priority: 3
```

## Future Improvements
- Prevent duplicate priorities.
- Add additional factors like estimated time or urgency.