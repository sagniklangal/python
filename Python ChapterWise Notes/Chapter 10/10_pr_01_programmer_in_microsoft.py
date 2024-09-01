class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"Name of the {self.company} employee is {self.name} and product is {self.product}")
p1 = Programmer("Sagnik","Bing")
p2 = Programmer("Saikat","Skype")
p1.getInfo()
p2.getInfo()