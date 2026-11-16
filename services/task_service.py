from models.task import Tasks

task_list: list[Tasks] = []
def task_create(task:Tasks):
    task_list.append(task)
    return task
def list_tasks():
    return task_list
