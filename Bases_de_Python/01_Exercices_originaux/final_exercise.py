'''
Imagine you are hired by a local transportation company to build the backend engine for their vehicle rental platform.
Instead of just tracking data in simple lists, you need to build a system where a RentalAgency object manages an inventory of different Vehicle objects (Cars and Trucks).

System Architecture Requirements:
1.	Vehicle (Parent Class):
- 	Should initialized with: vin (a unique string ID), model (string), and daily_rate (float).
- It should track a boolean attribute: is_rented (defaults to False).
- It should have a __str__ method that returns: "[VIN] Model - $DailyRate/day (Available/Rented)"
2.	Car (Child Class):
- Inherits from Vehicle.
- Has a method calculate_rental_cost(days) that returns daily_rate * days. However, if the car is rented for 7 days or more, apply a 10% discount to the total cost.
3.	Truck (Child Class):
- Inherits from Vehicle.
- Accepts an additional attribute during initialization: payload_capacity (int, in lbs).
- Overrides the calculate_rental_cost(days) method. Because trucks experience more wear and tear, they have a flat $50 insurance fee added to the total cost, regardless of how many days they are rented.
4.	RentalAgency (Management Class):
- Initialized with a name (string).
- Has an attribute fleet which is an empty dictionary {}. This dictionary will store vehicles using their vin as the key, and the actual Vehicle object as the value.
- Method add_vehicle(vehicle_obj): Adds the vehicle to the fleet dictionary.
- Method rent_out(vin, days): Checks if the vehicle exists and is available. If it is, switch its is_rented status to True, calculate the cost using that specific vehicle's calculation logic, and print the receipt summary. If it's already rented, print an error.

'''

# --- Base Vehicle Class ---
class Vehicle:
    def __init__(self, vin, model, daily_rate):
        self.vin = vin
        self.model = model
        self.daily_rate = daily_rate
        self.is_rented = False

    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f"[{self.vin}] {self.model} - ${self.daily_rate}/day ({status})"

# --- Write the Car Child Class Here ---
class Car(Vehicle):
    def __init__(self,vin,model,daily_rate) :
        super().__init__(vin, model,daily_rate)
        
    
    def calculate_rental_cost(self,days) :
        self.days = days
        if (self.days >= 7) :
            return (self.daily_rate * self.days)*0.90
        else :
            return self.daily_rate * self.days


# --- Write the Truck Child Class Here ---

class Truck(Vehicle):
    def __init__(self,vin,model,daily_rate,payload_capacity) :
        super().__init__(vin, model, daily_rate)
        self.payload_capacity = payload_capacity
    
    def calculate_rental_cost(self,days) :
        self.days = days
        if (self.days >= 7) :
            return ((self.daily_rate * self.days)*0.90 )+ 50
        else :
            return (self.daily_rate * self.days )+ 50        


# --- Write the RentalAgency Management Class Here ---

class RentalAgency :
    def __init__(self, name) :
        self.name = name
        self.fleet = {}
 

    def add_vehicle(self,vehicle_obj) : 
        self.fleet[vehicle_obj.vin] = vehicle_obj
    
    def rent_out(self,vin,days) :
        if vin not in self.fleet:
            print(f"Error: VIN {vin}.")
            return

        vehicle = self.fleet[vin]

        if vehicle.is_rented:
            print(f"Error: Vehicle {vin} is already rented.")
            return
        else :
            vehicle.is_rented = True
            print(f"Receipt for {vehicle.model} : Total cost for {days} days is ${vehicle.calculate_rental_cost(days)}")

        #Receipt for Honda Civic: Total cost for 3 days is $135.0
    def display_fleet(self) : 
        for veh in self.fleet.values():
            print(veh)



if __name__ == "__main__":
    # ==========================================
    # --- TEST CODE (Do Not Modify Below) ---
    # ==========================================

    # 1. Create the agency
    agency = RentalAgency("Apex Rentals")

    # 2. Create vehicles
    car1 = Car("C101", "Tesla Model 3", 80.0)
    car2 = Car("C102", "Honda Civic", 45.0)
    truck1 = Truck("T201", "Ford F-150", 120.0, 2000)

    # 3. Populate the agency's fleet
    agency.add_vehicle(car1)
    agency.add_vehicle(car2)
    agency.add_vehicle(truck1)

    print("--- Initial Fleet Status ---")
    agency.display_fleet()
    print("\n--- Processing Transactions ---")

    # Rent a car for a short duration (No discount)
    agency.rent_out("C102", 3) 

    # Rent a car for a long duration (10% discount applied)
    agency.rent_out("C101", 10) 

    # Rent a truck (Flat $50 fee applied)
    agency.rent_out("T201", 2) 

    # Rent a truck (Flat $50 fee applied)
    agency.rent_out("T201", 2) 

    # Attempt to rent a vehicle that is already out
   
    print("--- Final Fleet Status ---")
    agency.display_fleet()
# ----------------
# EXPECTED OUTPUT
# ----------------
'''
--- Initial Fleet Status ---
[C101] Tesla Model 3 - $80.0/day (Available)
[C102] Honda Civic - $45.0/day (Available)
[T201] Ford F-150 - $120.0/day (Available)

--- Processing Transactions ---
Receipt for Honda Civic: Total cost for 3 days is $135.0
Receipt for Tesla Model 3: Total cost for 10 days is $720.0 (Discount Applied!)
Receipt for Ford F-150: Total cost for 2 days (inc. truck insurance) is $290.0
Error: Vehicle C102 is already rented out!

--- Final Fleet Status ---
[C101] Tesla Model 3 - $80.0/day (Rented)
[C102] Honda Civic - $45.0/day (Rented)
[T201] Ford F-150 - $120.0/day (Rented)

'''