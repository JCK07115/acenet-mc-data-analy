# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.
"""
    desc: collates weekly progress status of tasks and habits, then displays them to the user
          modified to take in 3 args:
            - data[0] : habits
            - data[1] : tasks
            - data[2] : file_name
"""
def gen_weekly_report(*data_set_args):
    
    # only proceed if the number of args is as expected (the 3 mentioned above)
    if(len(data_set_args)==3):
        
        # tasks
        print(f"\n")
        print(f"--------------------------------------------")
        print(f"WEEKLY TASK REPORT FOR {data_set_args[2]}")
        print(f"--------------------------------------------")

        weekly_tasks = data_set_args[1]
        if len(weekly_tasks)==0:
            print(f"There are currently no pending tasks in the week!")
        else:
            completed_tasks = []
            incomplete_tasks = []

            # LOOP COMPREHENSION
            for day in days:
                completed_tasks.extend([(day,task) for task in weekly_tasks[day] if weekly_tasks[day][task]])
                incomplete_tasks.extend([(day,task) for task in weekly_tasks[day] if not weekly_tasks[day][task]])
                
            # LOOP
            # for day in days:
            #     for task, completeness in weekly_tasks[day].items():
            #         if completeness:
            #             completed_tasks.append((day, task))
            #         else:
            #             incomplete_tasks.append((day, task))

            print(f"completed tasks: {completed_tasks}")
            print(f"incomplete tasks: {incomplete_tasks}")

            if len(completed_tasks)==0:
                print(f"You haven't completed any tasks... YET, there's still time ;). You've got this! 💪🏾")
            elif len(incomplete_tasks)==0:
                print(f"Fantastic job completing all your scheduled tasks! :]")
            elif len(incomplete_tasks) > len(completed_tasks):
                print(f"Keep going! :]")
            elif len(completed_tasks) > len(incomplete_tasks):
                print(f"You're almost there! :]")

            print(f"\n")

        # habits
        print(f"--------------------------------------------")
        print(f"WEEKLY HABIT REPORT FOR {data_set_args[2]}")
        print(f"--------------------------------------------"  )

        weekly_habits = data_set_args[0]
        if len(weekly_habits)==0:
            print(f"There are currently no tracked habits in the week!")
        else:
            habits = []

            # LOOP COMPREHENSION
            for habit in weekly_habits:
                i=0
                habit_progress = sum([i+1 for day in weekly_habits[habit] if weekly_habits[habit][day]])
                habits.append((habit, habit_progress))
            
            # LOOP
            # for habit in weekly_habits:
            #     habit_progress = 0
            #     for day, completeness in weekly_habits[habit].items():
            #         if completeness:
            #             habit_progress+=1
                    
            #     habits.append((habit, habit_progress))

            for (habit, habit_progress) in habits:        
                print(f"{habit}: {habit_progress}/7 days")

            print(f"\n")


# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = [
                "dictionaries_1.txt",
                "dictionaries_2.txt",
                "dictionaries_3.txt",
                "dictionaries_4.txt",
                "dictionaries_5.txt",
                "dictionaries_6.txt",
                "dictionaries_7.txt",
                "dictionaries_8.txt",
                "dictionaries_9.txt",
                "dictionaries_10.txt"
            ] 

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the gen_week_report() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        gen_weekly_report(data[0], data[1], file_name)
