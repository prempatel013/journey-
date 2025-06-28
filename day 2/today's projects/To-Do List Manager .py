# Project 2: To-Do List Manager 📝
# Concepts Used: Lists, loops, error handling

# start coding here





menu_list=[]

while True:

    ask=int(input('what do you want to do : \n 1.add task \n 2.Remove task \n 3.View all tasks \n 4.Quit\n :'))

    if ask==1:
        task=input("so write which task you want to add: ")
        menu_list.append(task)
        
    elif ask==2:
        remove=input(f'{menu_list} which task you want to remove')
        menu_list.remove(remove)
    elif ask==3:
        print(f"{menu_list}")
    elif ask==4:
        quit()
        



























# Key Learning Outcomes:
# ✅ Handle real user input with error checking
# ✅ Build interactive programs with menus
# ✅ Practice core Day 2 concepts in practical scenarios