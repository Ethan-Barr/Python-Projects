import json

def load_todo(filename):
    try:
        with open(filename, 'r') as file:
            todos = json.load(file)
            return todos
    except FileNotFoundError:
        return []
    
def save_todo(filename, todos):
    with open(filename, 'w') as file:
        json.dump(todos, file, indent=4)

def add_todo(todos, task):
    todos.append({"task": task, "completed": False})
    return todos

def complete_todo(todos, task):
    for todo in todos:
        if todo["task"] == task:
            todo["completed"] = True
            return todos
    return todos

def list_todos(todos):
    for todo in todos:
        print(todo["task"])
        print(f"{todo['title']} - {'Completed' if todo['completed'] else 'Pending'}")
        # status = "✔️" if todo["completed"] else "❌"
        # print(f"{status} {todo['task']}")

def main():
    filename= './assets/todos.json'
    todo_list = load_todo(filename)
    print(todo_list)
    
    while True:
        print("Todo List:")
        list_todos(todo_list)
        
        print("\nOptions:")
        print("1. Add Todo")
        print("2. Complete Todo")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list = add_todo(todo_list, task)
            save_todo(filename, todo_list)
        
        elif choice == '2':
            task = input("Enter the task to complete: ")
            todo_list = complete_todo(todo_list, task)
            save_todo(filename, todo_list)
        
        elif choice == '3':
            print("Exiting the Todo List application.")
            exit()
            
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()