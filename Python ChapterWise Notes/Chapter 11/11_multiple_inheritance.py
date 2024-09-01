class Employee:
    company = "Google"
class PubgPlayer:
    company = "Pubg"
    level = 50
class Programmer(Employee,PubgPlayer):
    def upgradeLevel(self):
        self.level = self.level + 1

p1 = Programmer()
print(p1.company)
print(p1.level)
p1.upgradeLevel()
print(p1.level)
print(p1.company) #Google will get printed as 
                  #class Programmer(Employee,PubgPlayer), here
                  #Employee is inherited first

                  #If Programmer(PubgPlayer,Employee), then Pubg
                  #would be printed