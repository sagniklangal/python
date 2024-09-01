class Train:
    def __init__(self,name,seats,fare):
        list = []
        self.name = name
        self.seats = seats
        self.fare = fare
    def bookTicket(self):
        if self.seats>0:
            print(f"The ticket has been booked in {self.name}")
        self.seats = self.seats - 1
    def status(self):
        print(f"In the {self.name} there are {self.seats} ",end="")
        print(f"seats available")
    def fareInfo(self):
        print(f"The fare of the train is {self.fare}")
    def cancelTicket(self):
        self.seats+=1

t1 = Train("Rajdhani",300,200)
t1.fareInfo()
t1.bookTicket()
t1.status()
t1.bookTicket()
t1.status()
t1.cancelTicket()
t1.cancelTicket()
t1.status()