class Student():
    def __init__(self, name, grade, classes):
        if not name or not grade:
            raise TypeError("Name and/or grade can't be blank")

        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        for one_class in self.classes:
            if one_class.lower() == class_name.lower():
                return None

        self.classes.append(class_name)

    def get_num_classes(self):
        return len(self.classes)

    def summary(self):
        return f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"
