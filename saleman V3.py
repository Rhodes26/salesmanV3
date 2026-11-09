#saleman V3 
#Objective: Help User choose vehicle. Once choosen, end program.
import time

#my resonsing: creating instances  for class since the user (you) will have choose a selection in the display termainal 
class vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

#instances and objcect. A dictionary or dataclass would probably be better...

car1 = vehicle("Honda", "Civic", 1997, 7975)
car2 = vehicle("Toyota", "MK4 Supra", 1999, 43994)
car3 = vehicle("Ford", "Mustang GT", 2016, 3244)
car4 = vehicle("Chevy", "Camaro", 2016, 35600)
car5 = vehicle("BMW", "BMW M4", 2026, 82200)

options = [car1, car2, car3, car4, car5]


def intro():
 print("Program Start")
 time.sleep(0.2)
 

#Show Menu, Get Input, Check Quit, Loop  through cars
#USE DRY
def selection():
    for car in options:
        print(car.brand, car.model, car.year, car.price)
        time.sleep(0.2)

    while True:
        user = input(
            "Salesmanv3: What car would you like to choose "
            "(Type selection in menu or Q to quit)?: "
        ).strip()

        if user.lower() in {"q", "quit"}:
            print("Program End")
            break

        for car in options:
            if user == car.brand:
                print("Well Done")
                return

            if user == car.model:
                print("Good")
                return  
   
#Early return complete. :)
intro()
selection()

