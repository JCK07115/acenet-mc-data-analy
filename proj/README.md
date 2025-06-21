#  HOW THE TASK AND HABIT TRACKERS WORKS

## TASKS

Tasks are individual activities that you can add to any day within the week; from singing to swimming to dancing to walking to learning a new skill.

Below are the functions that you can work with in relation to tasks. 

<b>NOTE: While using any of the following functions, you can enter the letter 'Q' into a prompt, followed by pressing the ' Enter ↵ ' key, in order to exit out of the function/program.</b>

### <u>Adding a Task</u>
When you run this function, you will be prompted for which day you'd like to attach a task to.

Once you enter a valid day of the week, you will then be prompted for the particular task that you'd like to add.

If the task is valid, it will be added to the task tracker. The updated list of tracked tasks is displayed before the function is exited.

<b> NOTE: A valid task cannot be blank/empty  ("").

A single task can be added to multiple days of the week, but cannot be added to a day that it has already been added to prior.</b>

### <u>Marking a Task (as complete)</u>
The benefit of a task tracker lies in being able to mark tasks as complete once they have been accomplished.

When you run this function, the current list of tracked tasks is displayed to aid your selection of the right one.

If there are no tasks in the tracker, a message is displayed to inform you, and then the function is exited. Otherwise, if there is at least one task in the tracker, you will be prompted to enter a valid task you would like to mark as complete.

In order to validate marking of tasks, the function automatically obtains the current day from the date. 

If the task exists on this particular day and has been already been marked as complete on this particular day, a message is displayed to inform you. Otherwise, it is immediately marked as complete.

</b>Recall</b> that duplicate tasks are permitted across the week, so this function must account for that.

If the task is valid, that is it exists in the tracker, but it is being tracked on a different day (say yesterday or the day before yesterday), the function searches through and attempts to find the a day (before the current day) where the task is being tracked, and then marks it as complete; this is following the logic that tasks cannot be completed in the future - they are either completed in a prior day or on the current day.

Finally, the updated list of tracked tasks is displayed as a confirmation.

### <u>Removing a Task</u>
Sometimes, you might decide to forego a task, and as such, you'd like to remove it from the tracker.

When you run this function, you will be shown the currently tracked <b>and</b> pending tasks, to aid your selection.

You will then be prompted for the day you'd like to remove a task from, followed by a prompt for the specific task to remove.

Once valid entries are made, the task is removed from that specific day of the week. Finally, the updated task tracker is displayed for confirmation.

<b>NOTE: Once again, since duplicate tasks are permitted, a task might be removed from a specific day, but still exist on another day. To remove it from the week entirely, it must be removed from each day it is being tracked on.</b>

<hr>

## HABITS

### <u>Adding a habit</u>
When you run this function, you will be only be prompted for the actual habit, not for any particular day of the week.

This is because an entry differs from a task, in the sense that for a specific habit, an entry for each day of the week is created in the habit tracker.

Once you enter a valid habit, it will be added to the tracker. The updated list of tracked habits is displayed before the function is exited.

<b> NOTE: A valid habit cannot be blank/empty ("").

Habits are unique; the same habit cannot be added if it already exists in the tracker.</b>

### <u>Marking a Habit (as complete)</u>
Similarly to tasks, habits can be marked as complete.

When this function is run, you will be prompted for the habit you want to mark; if it doesn't exist in the habit tracker, you will be informed and re-prompted.

Once a valid habit is entered, you will be prompted for the day of the week towards which you'd like to mark the habit.

When a valid day is entered, an updated list of tracked habits is displayed as confirmation.

### <u>Removing a Habit</u>
When this function is run, you will be shown the current list of tracked habits, to aid your selection.

If there are available habits, you will then be prompted for the one you'd like to remove from the tracker.

If it is valid, it is immediately removed from the tracker.

Finally, the updated habit tracker is displayed for confirmation.

<hr>

### <u>Daily and Weekly Report Generators</u>
#### <u>Weekly Report Tracker</u>
As the name suggests, this function aggregates weekly details about all tasks and habits and generates a report from these stats.

As far as tasks go, this function compiles a list of completed and incomplete tasks in the task tracker, displays each list and provides an encouraging message to go with the report. 😁

As for the habits, this function compiles a list of each habit in the habit tracker, as well as the progress (number of marked/completed days) per habit, and displays them in a nice format.

#### <u>Daily Report Tracker</u>
Sometimes, you might only be interested in the tasks and habits pertaining to a specific day of the week, and not the entire week itself.

When you run this function, you will be prompted for the specific day you would like to generate a report for.

Once a valid day is entered, the stats related to the relevant tasks and habits for that day are compiled and displayed to you.

<hr>

### MAIN MENU
The Main Menu allows quick access to all of the above functionality. 

To access a specific option (which corresponds to a function), simply enter the number to the left of the option, or in the case of tidying up the notebook or quitting, you can also enter the letters indicated in those options.