class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))
        print("✅ Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("⚠️  No tasks found.\n")
            return

        print("\n📋 Current Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"\n--- {i} ---")
            print(task)

    def search_task(self, keyword):
        result = [task for task in self.tasks if keyword.lower() in task.title.lower()]
        if result:
            print("\n🔍 Search Results:")
            for task in result:
                print("\n" + str(task))
        else:
            print("❌ No matching tasks found.\n")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            print(f"🗑️  Task '{removed.title}' deleted.\n")
        except IndexError:
            print("❌ Invalid task number.\n")


def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.add_task(title, description)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            manager.search_task(keyword)

        elif choice == "4":
            manager.view_tasks()
            index = int(input("Enter task number to delete: "))
            manager.delete_task(index)

        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break

        else:
            print("❌ Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
