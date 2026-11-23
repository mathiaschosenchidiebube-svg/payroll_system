class Staff:
    def __init__(self, name, base_salary):
        if base_salary <= 0:
            raise ValueError("Salary can't be zero or negative")
        self.name = name
        self.base_salary = base_salary
        
    def pay(self):
        return self.base_salary
staff1 = Staff("Ada",10)
print(staff1.base_salary)
print(staff1.pay())

class Teacher(Staff):
    def __init__(self, name, base_salary, number_of_classes_taught):
        super().__init__(name, base_salary)
        self.number_of_classes_taught = number_of_classes_taught
        
    def pay(self):
        bonus = self.number_of_classes_taught * 500
        return super().pay() + bonus
staff2 = Teacher("Austin", 100,5)
print(staff2.pay())

class Driver(Staff):
    def __init__(self, name, base_salary, trips):
        super().__init__(name, base_salary)
        self.trips = trips

    def pay(self):
        bonus = self.trips * 500
        return super().pay() + bonus
staff3 = Driver("Tunde", 500, 3)
print(staff3.pay())

all_staff = [staff1, staff2, staff3]
for person in all_staff:
    print(f"{person.name} earns {person.pay()}")