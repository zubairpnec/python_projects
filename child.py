from parent import parent_class

class child_class(parent_class):
    def __init__(self):
        self.company = input("organization name: ")
        parent_class.__init__(self,self.company)
        self.age = None
        self.car = None
        self.bank = None

    def read_data(self):
        parent_class.read_data(self)
        self.age = input("Enter age: ")
        self.bank = input("Enter bank: ")
        self.car = input("Enter car: ")

    def print_data(self):
        parent_class.print_data(self)
        text = f'\nand  {self.age}\'is age {self.bank} is bank and : {self.car} is car'
        print(text)


if __name__ == "__main__":
    our_obj = child_class()
    our_obj.read_data()
    our_obj.print_data()

