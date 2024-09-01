class Train:
    def __init__(sagnik,name,seats,fare): # self can be anything
        sagnik.name = name
        sagnik.seats = seats
        sagnik.fare = fare
    def status(sagnik):
        print(f"In the {sagnik.name} there are {sagnik.seats} ",end="")
        print(f"seats available")
    def fareInfo(sagnik):
        print(f"The fare is {sagnik.fare}")

t1 = Train("Rajdhani Express",300,200)
t1.status()
t1.fareInfo()
