class Appliance:
    def __init__(self, b, m, c):
        self.__brand = b
        self.material = m
        self.color = c
        
    def change_brand(self, b):
        self.__brand = b
        
    def print_brand(self):
        print("Brand: ", self.__brand)
        
class Aircon(Appliance):
    def __init__(self, w, t, h, b, m, c):
            super().__init__(b, m, c)
            self.weight = w
            self.ac_type = t
            self.horsepower = h
        
    def print_type(self):
        print("Type: ", self.ac_type)
    
    def print_hp(self):
        print("Horsepower: ", self.horsepower)
        
class Stove(Appliance):
    def __init__(self, f, u, d, b, m, c):
            super().__init__(b, m, c)
            self.fuel = f
            self.temp_increase = u
            self.temp_decrease = d
        
    def print_fuel(self):
        print("I run on: ", self.fuel)
        
    def print_increase(self):
        print(self.temp_increase)
        
    def print_decrease(self):
        print(self.temp_decrease)

#brandname is the Appliance parent class attributes        
brandname = Appliance("Samsung", "Metal", "GunMetal")

#test print brand name of the appliances
brandname.print_brand()

#aircon child
inverter = Aircon(5, "Inverter aircon", 1,"Samsung", "Metal", "GunMetal")
split = Aircon(7, "Split type aircon", 2,"Samsung", "Metal", "GunMetal")

#stove child parameters
induction = Stove("Electric", "increase voltage", "decrease voltage","Samsung", "Metal", "GunMetal")
gas = Stove("Gasul", "more gas", "less gass","Samsung", "Metal", "GunMetal")


#test Aircon child
inverter.print_brand()
inverter.print_type()
inverter.print_hp()
split.print_brand()
split.print_type()
split.print_hp()

#test stove child
induction.print_brand()
induction.print_increase()
gas.print_brand()
gas.print_decrease()

#changing the brand name
brandname.change_brand("Though Mama")
brandname.print_brand()
