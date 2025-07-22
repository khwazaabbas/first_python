class train:
    def __init__(self, station1, station2):
        self.station1 = station1
        self.station2 = station2
    
    def model(self):
        print("vande bharat express")

class bus:
    def __init__(self, station1, station2):
        self.station1 = station1
        self.station2 = station2
    
    def model(self):
        print("volvo")

class aeroplane:
    def __init__(self, station1, station2):
        self.station1 = station1
        self.station2 = station2
    
    def model(self):
        print("air india")

class taxi:
    def __init__(self, station1, station2):
        self.station1 = station1
        self.station2 = station2
    
    def model(self):
        print("kmvn taxi")

#obj_train = train("tanakpur", "izzatnagar")   # object creation
#obj_bus = bus("bareilly", "lucknow")
#obj_aeroplane = aeroplane("hyderabad", "mumbai")
#obj_taxi = taxi("lohaghat", "dharchula")

#vehicles = [obj_train, obj_bus, obj_aeroplane, obj_taxi] # list of objects
#for x in vehicles:
#    x.model()

# obj_train = train(input("enter the station1 for train  :  "), input("enter the station2 for train  :  "))
# obj_bus = bus(input("enter the station1 for bus  :  "), input("enter the station2 for bus  :  "))
# obj_aeroplane = aeroplane(input("enter the station1 for aeroplane  :  "), input("enter the station2 for aeroplane  :  "))
# obj_taxi = taxi(input("enter the sation1 for taxi  :  "), input("enter the station2 for taxi  :  "))

#for x in (obj_train, obj_bus, obj_aeroplane, obj_taxi):
#    x.model()

vechicles1 = [train("tnakpur", "izzatnagar"),   
            bus("bareilley", "lucknow"),
            aeroplane("hyderabad", "bangalore"),
            taxi("lohaghat", "dharchula")]
for x in vechicles1:
    x.model()