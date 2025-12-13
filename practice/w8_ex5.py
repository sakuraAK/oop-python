import json
    
    
class Task:
    def __init__(self, name):
        self.__name = name
        self.__completed = False
    
    
    def __repr__(self):
        return f"Task Name: {self.__name}, Completed: {self.__completed}"
    
    def __str__(self):
        return f"Task Name: {self.__name}, Completed: {self.__completed}"
    
    def __eq__(self, value):
        return self.__name == value.__name
   
    
    def to_dict(self):
        return {
            "name": self.__name,
            "completed": self.__completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"])   
    
    
 
task_list = [
    Task(name="Set up Github account"),
    Task(name="Install VS code"),
    Task(name="Clone the repo"),
    Task(name="Complete HW")]





def save_to_file(list_of_tasks):
    dict_tasks = []
    for x in list_of_tasks:
        dict_tasks.append(x.to_dict())
    with open("task_list.out", "w") as f:
        json.dump(dict_tasks, f, indent=4)


def load_from_file():
    with open("task_list.out", "r") as f:
        data = json.load(f)
    task_list = []
    for t in data:
        task_list.append(Task.from_dict(t))

    return task_list

# save_to_file(task_list)        
        
task_list = load_from_file()
print(task_list)
        


def add_new_task(name):
    completely_new_task = Task(name)     
    for t in task_list:
        if t == completely_new_task:
            print("Duplicate found")
            return
    task_list.append(completely_new_task)
    
    
 
add_new_task("Install VS code")

print(task_list)   
        
    

    







