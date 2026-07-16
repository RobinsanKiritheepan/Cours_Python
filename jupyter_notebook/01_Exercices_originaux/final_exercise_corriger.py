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


class Car(Vehicle):
    def calculate_rental_cost(self, days):
        if days >= 7:
            return (self.daily_rate * days) * 0.90
        return self.daily_rate * days


class Truck(Vehicle):
    def __init__(self, vin, model, daily_rate, payload_capacity):
        super().__init__(vin, model, daily_rate)
        self.payload_capacity = payload_capacity

    def calculate_rental_cost(self, days):
        if days >= 7:
            return (self.daily_rate * days) * 0.90 + 50
        return self.daily_rate * days + 50


class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.fleet = {}

    def add_vehicle(self, vehicle_obj):
        self.fleet[vehicle_obj.vin] = vehicle_obj

    def rent_out(self, vin, days):
        if vin not in self.fleet:
            print(f"Error: VIN {vin} not found.")
            return

        vehicle = self.fleet[vin]

        if vehicle.is_rented:
            print(f"Error: Vehicle {vin} is already rented out!")
            return

        vehicle.is_rented = True
        cost = vehicle.calculate_rental_cost(days)

        if isinstance(vehicle, Truck):
            print(f"Receipt for {vehicle.model}: Total cost for {days} days (inc. truck insurance) is ${cost}")
        elif days >= 7:
            print(f"Receipt for {vehicle.model}: Total cost for {days} days is ${cost} (Discount Applied!)")
        else:
            print(f"Receipt for {vehicle.model}: Total cost for {days} days is ${cost}")

    def display_fleet(self):
        for veh in self.fleet.values():
            print(veh)


if __name__ == "__main__":
    agency = RentalAgency("Apex Rentals")

    car1 = Car("C101", "Tesla Model 3", 80.0)
    car2 = Car("C102", "Honda Civic", 45.0)
    truck1 = Truck("T201", "Ford F-150", 120.0, 2000)

    agency.add_vehicle(car1)
    agency.add_vehicle(car2)
    agency.add_vehicle(truck1)

    print("--- Initial Fleet Status ---")
    agency.display_fleet()
    print("\n--- Processing Transactions ---")

    agency.rent_out("C102", 3)
    agency.rent_out("C101", 10)
    agency.rent_out("T201", 2)
    agency.rent_out("C102", 2)

    print("\n--- Final Fleet Status ---")
    agency.display_fleet()