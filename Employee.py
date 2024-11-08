# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: 
# name, ID number, department, and job title.

# Once you have written the class, write a program that creates 
# three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer

# The program should store the data in the three objects, 
# then display the data for each employee on the screen.

class employee:
    #count = 0
    def __init__(self, name, ID, department, title):
        self._name = name
        self._ID = ID
        self._department = department
        self._title = title
        #employee.count += 1

    def display(self):
        print(self._name, self._ID, self._department, self._title)
        

emp1 = employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
emp2 = employee('Mark Jones', '39119', 'IT', 'Programmer')
emp3 = employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

print('Name:', 'ID Number:', 'Department:', 'Job Title')
print(emp1.display())
print(emp2.display())
print(emp3.display())
