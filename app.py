from os import system

tasks = []

def clear_console():
    system("cls")

def next_step():
    input("\nHit enter to continue")
    clear_console()

def print_error():
    clear_console()
    print("Value Error!")
    
def out_of_range():
    clear_console()
    print("Out of range!")

def swap_tasks(f, t):
    print("Swaped!")
    return t, f

while True:
    clear_console()
# MENU
    print("MENU")
    print("1. add task")
    print("2. show tasks")
    print("3. count task")
    print("4. change task")
    print("5. remove task")
    print("6. swap task position")
    print("0. Exit")
    
    try:
        option = int(input(">> "))
    except:
        clear_console()
        print_error()
        continue
    
    # ADD TASK
    if option == 1:
        clear_console()
        while True:
            new_task = input("Name your next task: ")
            if new_task == "":
                break
            if new_task not in tasks:
                tasks.append(new_task)
            else:
                print("This task already exists")
                
    # SHOW TASKS
    if option == 2:
        clear_console()
        print("\nYour tasks: ")
        
        for i in range(len(tasks)):
            print(i+1, " > ", tasks[i])
        next_step()
    
    # COUNT TASKS
    if option == 3:
        clear_console()
        print(f"You have {len(tasks)} tasks")
        next_step()
    
    # CHANGE TASK
    if option == 4:
        clear_console()
        try:
            while True:
                try:
                    index = int(input("Enter task position: ")) - 1
                except:
                    print_error()
                    continue
                if index <= len(tasks) and index >= 0:
                    new_task = input(f"Enter new task title for <{tasks[index]}>: ")
                    if new_task and new_task not in tasks:
                        tasks[index] = new_task
                        next_step()
                        break
                    else:
                        print("The value cannot be empty or had the same value")
                else:
                    out_of_range()
        except:
            print_error()
            
    # REMOVE TASK
    if option == 5:
        clear_console()
        try:
            while True:
                try:
                    index = int(input("Enter task position: ")) - 1
                except:
                    print_error()
                    continue
                if index <= len(tasks) and index >= 0:
                    remove_task = input(f"Are you sure you want to delete task <{tasks[index]}>?\nPlease type yes or no: ").lower()
                    if remove_task[0] == "y":
                        del tasks[index]
                        print("Deleted!")
                        
                        break
                    else:
                        break
                else:
                    out_of_range()
        except:
            print_error()

    # SWAP TASKS
    if option == 6:
        clear_console()
        try:
            while True:
                try:
                    index_from = int(input("Enter task position from: ")) - 1
                except:
                    print_error()
                    continue
                if index_from <= len(tasks) and index_from >= 0:
                    while True:
                        try:
                            clear_console()
                            index_to = int(input("Enter task position to: ")) - 1
                        except:
                            print_error()
                            continue
                        
                        if index_to <= len(tasks) and index_to >= 0 and index_to != index_from:
                            swap_task = input(
                            f"Are you sure you want to swap task <{tasks[index_from]}> to <{tasks[index_to]}>?\nPlease type yes or no: ").lower()
                            if swap_task[0] == "y":
                                tasks[index_from], tasks[index_to] = swap_tasks(
                                    tasks[index_from], tasks[index_to])
                                next_step()
                                raise StopIteration
                            else:
                                break
                        else:
                            out_of_range()    
                else:
                    out_of_range()
        
        except StopIteration:
            continue
        except:
            print_error()
            
    # EXIT
    if option == 0:
        clear_console()
        print("Bye Bye!")
        break