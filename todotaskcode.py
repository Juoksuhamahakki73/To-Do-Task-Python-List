# This imports the time into the file
import time
from time import gmtime, strftime

# Get the current time formatted
s = strftime("%a, %d %b %Y %H:%M:%S", gmtime())

# Function for getting the user name
def user_name():
    name = input("Hello! Please enter your name: ")
    return name

# Get the user's name
name = user_name()

# This will greet the user and say the Date and Time
print("Hello " + name)

# This will tell the time for the user
print("The time is: " + s)

#This will ask the user what their to do task are for today
print( name + ", What are your to do list for today?")

 # Function to get the to-do tasks
def todo_task():
    todolist = input("Enter Tasks separated by commas: ").split(',')
    return todolist

# Get the tasks
tasks = todo_task()

# Print the tasks
print("Your tasks for today are: " + ', '.join(tasks))
