import tasks
if __name__ == "__main__":
    print(
    """
'stop' - to end program
'help' - to see all commands
'listall' - to see all tasks
'add [task]' - to add task,
also 'delete', change and listall
    """)
    while True:
        input_command = input("-~-").split()
        if input_command: 
            if input_command[0] == 'stop':
                break

            if input_command[0] == 'add':
                tasks.add_task(tasks.Task(input_command[1]))
                tasks.list_tasks()
        
            if input_command[0] == 'delete':
                tasks.delete_task(int(input_command[1]))
                tasks.list_tasks()

            if input_command[0] == 'listall':
                tasks.list_tasks()
