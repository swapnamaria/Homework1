class Student:
    def __init__(self, name, gpa, age):
        self.name = name
        self.gpa = gpa
        self.age = age
        print("A student object is created.")

    def __str__(self):
        return \
            '%s, %s, %s' % (self.name, self.gpa, self.age)

    def __eq__(self, other):
        if ((self.name.lower(), self.gpa, self.age) ==
                (other.name.lower(), other.gpa, other.age)):
            return True
        return False
    def __lt__(self, other):
        if ((self.name.lower(), self.gpa, self.age) <
                (other.name.lower(), other.gpa, other.age)):
            return True
        return False

    def __gt__(self, other):
        if ((self.name.lower(), self.gpa, self.age) >
                (other.name.lower(), other.gpa, other.age)):
            return True
        return False

    def __hash(self):
        return hash(self.name, self.age, self.gpa)

list_names= dict(name1 = 'John', name2 = 'Abe', name3 = 'Mary')
list_names_new = sorted(list_names, key=list_names.get)
print(list_names_new)

student_objects = [
    {'name': 'John', 'gpa': 4.2, 'age': 29},
    {'name': 'Jane', 'gpa': 3.0, 'age': 42},
    {'name': 'Dave', 'gpa': 3.9, 'age': 35},
    {'name': 'Mithra', 'gpa': 3.0, 'age': 26},
    {'name': 'Chen', 'gpa': 4.0, 'age': 52}
]
print(sorted(student_objects, key=lambda k: (k['gpa'],k['name'],k['age'])))
