class student:
    def __init__(self, name , mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("name=", self.name)
        print("mark=", self.mark)
s1=student("chachin","100",)
s1.display()
