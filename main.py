import tasks

def menu():
    print(
    """
'stop' - to end program
'help' - to see all commands
'listall' - to see all tasks
'add' - to add task,
'delete' - to remove task,
change and listall
    """)

if __name__ == "__main__":
    tasks.create_db()
    tasks.init_db()
    menu()
    while True:
        input_command = input("-~-").strip().lower()
        if input_command: 
            if input_command == 'stop':
                break
            elif input_command == 'help':
                menu()

            elif input_command == 'add':
                tasks.add_task()
        
            elif input_command == 'delete':
                tasks.delete_task()

            elif input_command == 'update':
                tasks.toggle_task()

            elif input_command == 'listall':
                tasks.list_tasks()