from manager import TaskManager

def run():
    manager = TaskManager()
    
    while True:
        print("\n--- Task Pro ---")
        for i, task in enumerate(manager.tasks):
            print(f"{i + 1}. {task}")
        
        choice = input("\n(a)dd task or (q)uit: ").lower()
        if choice == 'a':
            title = input("Enter task: ")
            manager.add_task(title)
        elif choice == 'q':
            break

if __name__ == "__main__":
    run()