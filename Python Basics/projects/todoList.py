def add_task(task, task_list):
    task_list.append(task)
    print(f'Task "{task}" added to the list.')
    
def show_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
            
def remove_task(task_index, task_list):
    if 0 <= task_index < len(task_list):
        removed_task = task_list.pop(task_index)
        print(f'Task "{removed_task}" removed from the list.')
    else:
        print("Invalid task index.")

def main():
    print("Welcome to the To-Do List App!")
    for i in range(3):
        print("\n")
    
    task_list = []
    while True:
        show_tasks(task_list)
        
        for i in range(2):
            print("\n")
    
        task = input("Enter a task to add, 'remove' to delete a task, or 'exit' to quit: ")
        
        if task.lower() == 'exit':
            break
        
        if task.lower() == 'add':
            task = input("Enter the task to add: ")
            add_task(task, task_list)
        elif task.lower() == 'remove':
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                remove_task(task_index, task_list)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid command. Please enter 'add', 'remove', or 'exit'.")
    
    print("Goodbye!")    

if __name__ == "__main__":
    main()