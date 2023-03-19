#===================================Capstone Project 3=============================

#===========================================SECTION 1: START OF PROGRAM:

# Importing python modules:
import re
import datetime
import csv
today=datetime.date.today()

# Setting and printing title:
company_name = "Welcome to Destination Legacy"
empty_string = " "
print(empty_string)
print(company_name.center(80,"~"))

# Setting and printing current date:
print("Date:",today,"\n")

# Openining up file and setting it to read per lines:
users__data = open('user.txt','r+')
user_txt = users__data.readlines()

# Stripping lines and comma's to capture into dictionary list:
user_dict={}
for user in user_txt:
    user_names = (user.strip("\n").split(", "))
    user_dict[user_names[0]] = user_names[1]

# The code belows determines if username is already in file data.
print("What is your username?")
username = input(">")
while not username in user_dict:
    print("Error! Incorrect user name entered (try again):\n")
    print("What is your username?")
    username = input().lower()

# Once username is correct a password is required
# This code below determines if the key is equal to the
# value in the dictionary 'user_dict':
print("What is your password?")
password = input(">")

while user_dict[username]!=password:
    print("Error! Incorrect password entered (try again):\n")
    print("What is your password?")
    password = input().lower()
print("You have successfully logged in!\n")

#==================================================SECTION 2: SETTING FUNCTIONS:
# defining functions to use under menu in program:

# ===========Setting user register:
# Function allows the user to add a new user to the text file.
# Using csv reader to split the data into lines per column
# 1) It searches if username is already in file
# 2) It then checks if the passwords entered match
def reg_user():
  if username != "admin":
        print("Sorry, You are not authorised for this option.\n")

  elif username == "admin":
      print("============== register a new user: =============")
      new_username=input("Please enter a username:\n>")

      with open("user.txt") as my_file:
            user_search = csv.reader(my_file, delimiter=',')
            for row in user_search:
                if new_username == row[0]:
                    print("Error-This user has already been added\n")
                    return
                else:
                    pass

            new_password = input("Please enter a password:\n>")
            password_confirm = input("Re-enter you password\n>")
            new_user = ""

      if password_confirm != new_password:
            print("Error! Passwords do not match, please try again:")
            new_user = input(">")
      if password_confirm == new_password or new_user==new_password:
          with open("user.txt","a") as file:
              file.write(new_username + ", " + password_confirm + "\n")
              print("Thanks, new user added!\n")
                   
#===========Setting adding a task function:
# The function allows users to add a task
# to the txt file.
# The data on the file has been split
# into words, then casts them into
# seperate variables -ie-'task_title','task_desc'.
# once all the data is entered it writes it on
# a new line in the text file-"task.txt"
def add_task():
    print("============== adding a new task: =============")
    username_assign = input("Please enter the username for whom the task is assigned for:\n")
    task_title = input("Please enter the title of the task:\n")
    task_desc = input("Please enter the description of the task:\n")
    task_date = input("Please enter the due date of the course (*yyyy/mm/dd):\n")

    with open("tasks.txt","a") as file:
        file.writelines("\n" + username_assign + ", " + task_title + ", " + task_desc + ", "+ str(today) + ", " + task_date + ", " + "No")
        print(f"Thanks, new task added for {username_assign}.\n")

        file.close()

#===========Setting viewing all tasks function:
# The function allows the user to view all
# the tasks in the file in a neat display.
# The words in the lines are split into 
# seperate variables.  
def view_all():
    print("====================== All Tasks: ======================")
    tasks__data = open('tasks.txt','r+')
    lines = tasks__data.readlines()

    for words in lines:
        x=words.strip()
        user, tsk_title,tsk_description,assign_date,due_date,status = x.split(", ")
        tasks_all=(f'''Task:                     \t{tsk_title}
Assigned to:                \t{user}
Date assigned:              \t{assign_date}
Due date:                   \t{due_date}
Task complete(Yes/No)?:     \t{status}
Task Description:\n{tsk_description}\n''')
        print(tasks_all)
    
#======Setting viewing specific task function:
# The function allows the user to view 
# their specific tasks
# 1) The user can view the index to each task
#    and can select the index they would like to view
#    or else can select '-1' to go back to main menu
# 2) The user can then select if they want their task marked
#    complete. 
# 3) The user can edit their task by either reassigning the username 
#    or changing the due date.
# The code takes all the edited info and sets them into
# a new variable then rewrites the entire line with the new variable info.
# By using 'newline' in if statement, the newline element is stripped as it
# reads in a textfile as'\n'.
# by using a for loop the proram goes through entire list and only outputs the
# usernames information:
def view_mine():
    user_list=[]
    i=0
    print("====================== My Tasks: ======================")
    with open ('tasks.txt', 'r') as task_data:
        lines=task_data.readlines() 
        for words in lines:
            x = words.strip()
            user, tsk_title,tsk_description,assign_date,due_date,status = x.split(", ")
            user_list.append(words)
            i+=1

            tasks_mine=(f'''======================Task nr: {i} ======================
Task:                     \t{tsk_title}
Assigned to:                \t{user}
Date assigned:              \t{assign_date}
Due date:                   \t{due_date}
Task complete(Yes/No)?:     \t{status}
Task Description:\n{tsk_description}\n''')
            
            if username == user:
                print(tasks_mine)
    index=int(input('''======== Please select the following options: ========
*Enter the task number you would like to view:
*or enter -1 to go back to main menu\n>'''))
    if index >= 1:
        task_index = index-1
        task_chosen = user_list[task_index]
        user, tsk_title,tsk_description,assign_date,due_date,status=task_chosen.split(", ")

        if status == status.strip("\n"):
            newline = False

        else:
            newline = True
        status = status.strip("\n")

        tasks_mine=(f'''Task:                     \t{tsk_title}
Assigned to:                \t{user}
Date assigned:              \t{assign_date}
Due date:                   \t{due_date}
Task complete(Yes/No)?:     \t{status}
Task Description:           \n{tsk_description}''')
        
        print(f"\n=====You have selected the following task:======\n{tasks_mine}\n")
    if index == -1:
        return
   
    print('''======Please select the following options:=====
*option (a)                 mark your task complete
*option (b)                 edit the task\n''')
    option_select = input(">")
    if option_select == "a":
        status = "Yes"
        print("============= Task marked as complete: ==============")
        print((f'''\nTask:                     \t{tsk_title}
Assigned to:                \t{user}
Date assigned:              \t{assign_date}
Due date:                   \t{due_date}
Task complete(Yes/No)?:     \t{status}
Task Description:           \n{tsk_description}\n'''))

    elif option_select == "b":
        print("============================= Editing Tasks =============================")
        print('''Would you like to assign this task to another user or edit the due date? 
select <user> or <date>:''')
        task_edit=input(">").lower()
        
        if task_edit == "user":
            user_assign = input("Who would you like to Assign?\n>")
            user=user_assign
            print(f"\nThanks now {user_assign} is assigned for task!\n")
        if task_edit == "date":
            user_date_change = input("Please enter the new due date (*yyyy/mm/dd):\n>")
            due_date = user_date_change
            print(f"Thanks date changed to {user_date_change}.\n")
    else:
        print("Sorry, your input was incorrect.\n")
        return

    if newline == True:
        status += "\n"
    final_changes = (f"{user}, {tsk_title}, {tsk_description}, {assign_date}, {due_date}, {status}")
    
    old_task = user_list[task_index]
    i=0
    for lines in user_list:
        if old_task == lines:
            user_list[i] = final_changes
        i+=1

    tasks_data=open("tasks.txt","w")
    tasks_data.writelines(user_list)

#==========Setting generating reports function:
# This function has a variety of codes in order to gather
# all the data from the file and execute the correct code
def gen_reports():
    reports_title = "Destination Legacy Reports:"
    print(reports_title.center(60,"="))

# Task overview section ==============>
# This section gathers all the data to generate a overview of the 
# tasks and users information:

    # By counting the number of lines we get the total nr of tasks:
    f = open("tasks.txt","r")
    f_readlines = f.readlines()
    tasks_total = (len(f_readlines))
   
    # By counting the number of "Yes" statement we get
    # the nr of completed tasks:
    f=open("tasks.txt","r")
    f_read = f.read()
    tasks_completed = f_read.count("Yes")

    # By subtracting the the 2 values we get the nr of tasks uncompleted:
    tasks_uncomplete = tasks_total-tasks_completed

    # This function changes the date type from date into string
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")
    date =today.strftime("%Y/%m/%d")

    # Setting counters
    i=0
    overdue_count=0
    with open('tasks.txt',"r") as tasks_data:
        lines = tasks_data.readlines()
        current_user = ''

        # Seperating data into seperate variables:
        for words in lines:
            x=words.strip()
            user, tsk_title,tsk_description,assign_date,due_date,status=x.split(", ")
            if due_date<date:
                overdue_count+=1
        
            if due_date<date and status=="No":
                i+=1
        
        # Calculating the perecentage of incomplete tasks for overview
        # Calculating the percentage of overdue Tasks for overview
        incomplete_tasks = (tasks_uncomplete/tasks_total)*100
        incomplete_tasks = round(incomplete_tasks,2)
        overdue_tasks = (i/tasks_total)*100.
        overdue_tasks = round(overdue_tasks,2)

        tasks_overview =(f'''\n==================Tasks overview:===================
Total nr of tasks:                           \t{tasks_total}
Total nr of completed tasks:                 \t{tasks_completed}
Total nr of uncompleted tasks:               \t{tasks_uncomplete}
Total nr of tasks uncompelted and overdue:   \t{i}
Tasks incomplete %                           \t{incomplete_tasks}%
Tasks overdue %                              \t{overdue_tasks}%
    ''')

        # Writing 'tasks_overview' varaible into text file, 'tasks_overview.txt':
        file_write=open("tasks_overview.txt","w")
        file_write.write("Destination legacy reports:"+tasks_overview)
        file_write.close()

# Setting option choice for user to select which report they would like to view:
    report_choice=input('''\nPlease select which report you would like to access:
Tasks overview - (select:'t')
User overview  - (select:'u')\n>''').lower()
    count=0
    user_list2=[]
    user_list3=[]

# Getting data from text file and splitting it into lines.
# Then printing each line per index value:
    if report_choice == "t":
         with open('tasks_overview.txt','r') as file_p:
            lines = file_p.readlines() 
            for words in lines[2:]:
                x = words.strip().split()
                user_list3.append(words)

            print(f'''\n==================Tasks overview:===================
{user_list3[0]}
{user_list3[1]}
{user_list3[2]}
{user_list3[3]}
{user_list3[4]}
{user_list3[5]}
''')

# User overview section ==============>
# If the user selects option u they will obtain the users reports:
# This code below strips the data from the text file and seperates
# it into seperate variables
# by using current user variable, it removes all 
# duplicate usernames to avoid miscalculations
    elif report_choice == "u":
        with open ('tasks.txt', 'r') as task_data:
            lines=task_data.readlines() 
        for words in lines:
            x = words.strip()
            user, tsk_title,tsk_description,assign_date,due_date,status=x.split(", ")
            user_list2.append(words)
            count+=1
            if current_user == user:
                continue
            else:
                current_user = user

            #Printing user nr with username to assist user to select correctly:
            user_tag=(f"\n========User:{user}=======\nTag nr:{count}")
            print(user_tag)
            
        user_choice=int(input("\nPlease select which user tag nr you would like to view:\n>"))
        user_name=(input("Please confirm the username?\n>"))

        # Setting counters:
        i=0
        counter1=0
        counter2=0
        counter3=0
        counter4=0
        counter5=0
        user_list4=[]

        # This code determines which data to execute as per usernames and tag chosen
        # by user
        # It calculates the percentage values as follows:
        #-Total nr of tasks assigned:                 
        #-Total nr of tasks assigned (ie-%) compared to the other users:   
        #-Tasks completed:                          
        #-Tasks to still be completed:              
        #-Tasks uncompleted and overdue:            
        
        if user_choice >= 1:
            task_index=user_choice-1
            task_chosen=user_list2[task_index]
            user, tsk_title,tsk_description,assign_date,due_date,status=task_chosen.split(", ")
            tasks_assigned = f_read.count(user)
       
        for line in lines:
            temp = line.strip()
            user, tsk_title,tsk_description,assign_date,due_date,status=temp.split(", ")
            
            if user == user_name:
                counter1+=1
                percentage_user = round(((tasks_assigned/tasks_total)*100),2)

            if user == user_name and status == "Yes":
                counter2+=1

            else:
                counter3+=0

            tasks_completed = round(((counter2)/tasks_assigned)*100)
            tasks_left = round((100-tasks_completed),2)

            if user==user_name and due_date<date:
                counter4+=1
            else:
                counter5+=0
            tasks_overdue = round((((counter3+counter4)/tasks_assigned)*100),2)

        user_overview=(f'''==============Report overview for: {user_name}:=================
Total nr of tasks assigned:                 \t{tasks_assigned}
Tasks assigned percentage over all tasks:   \t{percentage_user}%
Tasks completed %                           \t{tasks_completed}%
Tasks to still be completed %               \t{tasks_left}%
Tasks uncompleted and overdue %:            \t{tasks_overdue}%
''')  

        # Writing 'user_overview' variable to text file 'user_overviw.txt':
        file_write2=open("user_overview.txt","w")
        file_write2.write(user_overview)
        file_write2.close() 

        # Opening up file for to get data
        # by using dictionary splitting lines per users
        # and removing the duplicates
        # Then clauclating the number of users in the file
        file = open("tasks.txt","r")
        file2 = file.readlines()
        task_dict={}
        for task in file2:
            user_names = (task.strip("\n").split(", "))
            task_dict[user_names[0]] = user_names[1]
        nr_users = len(task_dict)

        # Getting data from text file and splitting it into lines.
        # Then printing each line per index value:
        with open('user_overview.txt','r') as file_u:
            lines = file_u.readlines() 
            for words in lines:
                x = words.strip().split()
                user_list4.append(words)
            print(f'''\n================== General Overview: ===================\n
Total number of users registered: {nr_users}
Total number of tasks: {tasks_total}\n
{user_list4[0]}
{user_list4[1]}
{user_list4[2]}
{user_list4[3]}
{user_list4[4]}
{user_list4[5]}
===========================================================
''')
                  
    else:
        print("\nSorry your input was incorrect.Please try again:")
        gen_reports()

#========Setting display statistics function:
# The function allows the user to view the following stats:
# 1) total nr of tasks
# 2) total nr of users
# 3) the percentage ratio of completed tasks 
# The code calculates nr of lines in the file to get total tasks
# The code gets usernames from dictionary, which excludes duplicate names
def display_stats():
    file = open("tasks.txt","r")
    for count, line in enumerate(file):
        pass
    total_lines = count + 1

    file = open("tasks.txt","r")
    file2 = file.readlines()
    task_dict={}
    for task in file2:
        user_names = (task.strip("\n").split(", "))
        task_dict[user_names[0]] = user_names[1]
    nr_users = len(task_dict)

    file = open("tasks.txt", "r")
    data = file.read()
    occurrences = data.count("Yes")
    percentage=(occurrences/nr_users)*100

    print("========= Destination Legacy Statistics: =========")
    print('''\nStatistics report for Desination Legacy:
Total nr of tasks:              \t{}
Total nr of users:              \t{}
Completed Tasks %:              \t{}%\n'''.format(total_lines,nr_users,int(percentage)))
       
#========Setting exit menu function:
# The function allows users to exit the main menu:
def exit_menu():
  print('Goodbye!!!')
  exit()

#===========================================SECTION 3: Setting the menu:
# By using while true statement this allows
# the main menu to be in a loop
# Setting 2 different types of menu, if username is admin
# the user then gets a more extensive menu options
# if username not admin then the user get limited option
# setting all the creating functions into menu section to flow

#========Setting options for admin menu:
while True:
    if username == "admin":
        print("============*Menu Options===========")
        menu=print(('''Select one of the following options below:\n
r  - Register a new user
a  - Add a new task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - Display statistics
e  - Exit
'''))

#========Setting options for general menu:
    if username != "admin":
        print("============*Menu Options===========")
        menu = print(('''Select one of the following options below:\n
r  - Register a new user
a  - Add a new task
va - View all tasks
vm - View my task
e  - Exit
'''))
    users_menu_choice=input(">").lower() 

    if users_menu_choice == "r":
        reg_user()
        
    elif users_menu_choice == 'a':
        add_task()

    elif users_menu_choice == 'va':
        view_all()
        
    elif users_menu_choice == "vm":
        view_mine()

    elif users_menu_choice == "gr":
        gen_reports()

    elif users_menu_choice == "ds":
        display_stats()   
        
    elif users_menu_choice == 'e':
        exit_menu()

    else:
        print("Sorry, your input was incorrect.\n")

#======================================== Project complete ===============================
        














