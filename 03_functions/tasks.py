def add_task(task_list: list, task_name: str, done=False):
    task = {'name': task_name, 'done': done}
    task_list.append(task)
    return task_list

def remove_task(task_list: list, task_index: int) -> list:
    removed_task = task_list.pop(task_index)
    print(f'Removed task: {removed_task["name"]}')
    return task_list

def print_tasks(task_list: list, hide_done=False) -> list:
    for index, task in enumerate(task_list):
        if task['done']:
            is_done = 'X'
        else:
            is_done = '-'
        print(f'{index:4} [{is_done}] {task["name"]}')

def mark_done(task_list: list, task_index: int) -> list:
    pass

def input_task_id(task_list: list):
    task_index = input('Choose Task ID to remove')
    if task_index.isnumeric():
        task_index = int(task_index)
    else:
        print('ERROR: Wrong Task ID, it must be a number')
        if task_index > len(task_list) or task_list < 0:
            print('ERROR: Task ID is too high or negative')
            return None
        return task_index

def main(task_list):
    while True:
        print('---[ Tasks ]---')
        print('0: Exit')
        print('1: Print all tasks')
        print('2: Add a task')
        print('4: remove a task')
        choice = input('Choice: ')
        if choice.startswith('0'):
            break
        if choice.startswith('1'):
            print_tasks(task_list)
        if choice.startswith('2'):
            task_list = add_task(task_list, input('Task name: '))
        if choice.startswith('4'):
            print_tasks(task_list)
            task_list = remove_task(task_list, task_index)

main([])