class Employee:
    def __init__(self, id, name, department):
        self._id = id
        self._name = name
        self._department = department
    
    @property
    def id(self):
        return self._id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    def __str__(self):
        return f"id: {self._id}; name: {self._name}; department: {self._department}"
    
    def __repr__(self):
        return f"id: {self._id}; name: {self._name}; department: {self._department}"

class EmployeeManager:
    def __init__(self):
        self._employees_by_id = {}
        self._employees_by_name = {}
        self._employees_by_department = {}


    def add_employee(self, name, dpt):
        id = len(self._employees_by_id) + 1
        employee = Employee(id, name, dpt)
        self._employees_by_id[id] = employee
        self._employees_by_name[name] = employee
        if not dpt in self._employees_by_department:
            self._employees_by_department[dpt] = []
        self._employees_by_department[dpt].append(employee)


    def remove_employee(self, name):
        if name in self._employees_by_name:
            employee = self._employees_by_name[name]
            del self._employees_by_id[employee.id]
            del self._employees_by_name[name]
            
            #remove employee from department
            dpt_employees = []
            for empl in self._employees_by_department[employee.department]:
                if empl.name != name:
                    dpt_employees.append(empl)
            self._employees_by_department[employee.department] = dpt_employees

    def find_employee_by_id(self, id):
        if id in self._employees_by_id:
            return self._employees_by_id[id]
        return None

    def print_all_employees(self):
        print("All Employees")
        for dpt in self._employees_by_department.keys():
            print(f"Employees in: {dpt}")
            for empl in self._employees_by_department[dpt]:
                print(empl)
            print("-----------------------------------")








manager = EmployeeManager()

manager.add_employee("John", "Finance")
manager.add_employee("Jane", "HR")
manager.add_employee("Bill", "Accounting")
manager.add_employee("Tobi", "Accounting")
manager.add_employee("Troy", "IT")
manager.add_employee("Margaret", "Operations")



manager.print_all_employees()