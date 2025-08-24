import sqlite3

user_id = 1

# connect database
mainLis = sqlite3.connect("dolist.db")
cr = mainLis.cursor()

# create table if not exists
cr.execute("""
CREATE TABLE IF NOT EXISTS doList (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id  INTEGER,
    Tasks TEXT,
    importance TEXT
)
""")

def showTASKS():
    print("\n-Your Tasks ")
    cr.execute("SELECT id, Tasks, importance FROM doList WHERE user_id = ?", (user_id,))
    results = cr.fetchall()
    if results:
        for task_id, tas, imp in results:
            print(f"[{task_id}] Task => '{tas}'   | Importance => '{imp}' by ID {user_id}")
    else:
        print("No tasks found.")

def addTASKS():
    Tasks = input("Write a Task name: ").strip().capitalize() 
    importance = input("Write importance (High/Medium/Low): ").strip().capitalize()
    cr.execute("INSERT INTO doList(user_id, Tasks, importance) VALUES(?, ?, ?)", 
            (user_id, Tasks, importance))
    print(f"Task '{Tasks}' with importance '{importance}' added!")

def DeleteTASKS():
    task_id = input("Enter the Task ID to delete: ").strip()
    cr.execute("DELETE FROM doList WHERE user_id = ? AND id = ?", (user_id, task_id))
    print("Task deleted (if ID exists).")

def updateTASKS():
    task_id = input("Enter the Task ID to update: ").strip()
    new_task = input("Enter the new task name: ").strip().capitalize()
    new_importance = input("Enter the new importance: ").strip().capitalize()
    cr.execute("UPDATE doList SET Tasks = ?, importance = ? WHERE user_id = ? AND id = ?", 
            (new_task, new_importance, user_id, task_id))
    print(f"Task {task_id} updated.")

def quit_app():
    print("Quit")

# show  options
print("\n [1-showTasks  2-addTasks  3-deleteTasks  4-updateTasks  5-Quit ]")
userinput = input("Enter your option: ").strip().lower()

if userinput == 's' or userinput == '1':
    showTASKS()
elif userinput == 'a' or userinput == '2':
    addTASKS()
elif userinput == 'd' or userinput == '3':
    DeleteTASKS()
elif userinput == 'u' or userinput == '4':
    updateTASKS()
elif userinput == 'q' or userinput == '5':
    quit_app()
else:
    print("Invalid option, try again.")

# save and close
mainLis.commit()
mainLis.close()
