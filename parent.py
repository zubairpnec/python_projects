class parent_class:
    def __init__(self,company):
        self.parent_list = list()
        self.company = company

    def read_data(self):
        if self.company == "SUPARCO":
            self.parent_list.append(input("Enter P number: "))
            self.parent_list.append(input("Enter name: "))
            self.parent_list.append(input("Enter SPS: "))
        else:
            self.parent_list.append(input("Enter name: "))
    def print_data(self):

        for i in range(len(self.parent_list)):
            print("idx: ",i, "data:" ,self.parent_list[i])


if __name__ == "__main__":
    our_obj = parent_class("SUPARCO")
    our_obj.read_data()
    our_obj.print_data()

