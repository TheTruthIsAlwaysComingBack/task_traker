# primero debemos definir la manera de crear y agregar elementos para poder crear el archivo json y sera donde tendremos que manejar la logica 
import datetime 
import file_manager
import click

@click.group()
def tasktraker():
    pass

@tasktraker.command()
@click.argument('status', required=False, default='')
def list(status):
    data = file_manager.read_json()    
    if status not in ["todo", "in-progress", "done", ""]:
        print("Invalid status")
        return
    
    # If no status provided (empty string), show all tasks
    if status == "":
        for task in data:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        return

    # Show tasks filtered by status
    matching_tasks = False
    for task in data:
        if task["status"] == status:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
            matching_tasks = True
    
    if not matching_tasks:
        print(f"No tasks found with status: {status}")

@tasktraker.command()
@click.argument('description', nargs= -1, required=True)
def add(description):    
    if not description: 
        print("No se a ingresado ninguna tarea")
        return
    
    desc = ' '.join(description)

    data = file_manager.read_json()
    new_id = data[-1]["id"] + 1 if data else 1
    new_task = {
        "id": new_id,
        "description": desc,
        "status": "todo",
        "createdAt": str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")),
        "updatedAt": ''
    }
    
    data.append(new_task)
    file_manager.write_json(data)
    print(f"Task added successfully (ID: {new_id})")  
    
@tasktraker.command()
@click.argument('id_to_update')
@click.argument('description', nargs = -1)

def update( id_to_update, description):
    desc = ' '.join(description)
    
    data = file_manager.read_json()
    for task in data:
        if task["id"] == int(id_to_update):
            task["description"] = desc
            task["updatedAt"] = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            break
    else:
        print("Task not found")
        return
    
    file_manager.write_json(data)
    print(f"Task updated successfully (ID: {desc})")    


@tasktraker.command()
@click.argument('id_to_delete')
def delete(id_to_delete):
    data = file_manager.read_json()
    for task in data:
        if task["id"] == int(id_to_delete):
            data.remove(task)
            break
    else:
        print("Task not found")
    
    file_manager.write_json(data)
    print(f"Task deleted successfully (ID: {id_to_delete})")

@tasktraker.command()
@click.argument('id_task')
def mark_in_progress(id_task):
    data = file_manager.read_json()
    for task in data:
        if task["id"] == int(id_task):
            task["status"] = "in-progress"
            task["updatedAt"] = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            break
    else:
        print("No tasks in progress")
        return
    
    file_manager.write_json(data)    

@tasktraker.command()
@click.argument('id_task')
def mark_done(id_task):
    data = file_manager.read_json()
    for task in data:
        if task["id"] == int(id_task):
            task["status"] = "done"
            task["updatedAt"] = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            break
    else:
        print("No tasks in progress")
        return
    
    file_manager.write_json(data)


if __name__ == '__main__':
    tasktraker()