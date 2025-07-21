import os
import json
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values(".env")

class Task:
    current_id = 1

    def __init__(self, name, description='not added', category='not added', deadline='indefinitely',status=False):
        self.id = Task.current_id
        Task.current_id +=1
        self.name = name
        self.description = description
        self.category = category
        self.deadline = deadline
        self.status = status
        self.date_creatred = str(datetime.now())[:10]


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'deadline': self.deadline,
            'status': self.status,
            'date_created': self.date_creatred
        }



task_filename = 'tasks.json'



def add_task(task):
    if os.path.exists(task_filename):
        with open(task_filename, 'r') as task_file:
            try:
                tasks_list = json.load(task_file)

            except json.JSONDecodeError:
                tasks_list = [] 
    else:
        tasks_list = []
    tasks_list.append(task.to_dict())
    with open(task_filename, 'w') as task_file:
        json.dump(tasks_list, task_file, indent=4)

def list_tasks():
    if os.path.exists(task_filename):
        with open(task_filename, 'r') as task_file:
                tasks_list = json.load(task_file)
    try:
        for task in tasks_list:
            print(task['id'], '|', task['name'], '(pending)' if task['status'] == False else '(completed)')
    except:
        print('there are no tasks.')
def delete_task(id):
    
    if os.path.exists(task_filename):
        with open(task_filename, 'r') as task_file:
            tasks_list = json.load(task_file)
            tasks_list = [task for task in tasks_list if task['id'] != id ]

        with open(task_filename, 'w') as task_file:
            json.dump(tasks_list, task_file, indent=4)


    with open(task_filename, 'w') as task_file:
        json.dump(tasks_list, task_file, indent=4)

# task1 = Task('do 10 push ups', '', 'sport')
# task2 = Task('go for a walk', '', 'nature')
