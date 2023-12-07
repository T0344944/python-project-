import datetime

class Flight:
    def __init__(self, flight_number, origin, aircraft_number, airline_name, airline_code, distance_from_airport, flight_speed, timetable_arrival):
        self.flight_number = flight_number
        self.origin = origin
        self.aircraft_number = aircraft_number
        self.airline_name = airline_name
        self.airline_code = airline_code
        self.distance_from_airport = float(distance_from_airport)
        self.flight_speed = float(flight_speed)
        self.timetable_arrival = datetime.datetime.strptime(timetable_arrival, '%Y-%m-%d %H:%M')

    def calculate_estimated_arrival(self):
        if self.flight_speed > 0:
            hours_to_arrival = self.distance_from_airport / self.flight_speed
            return self.timetable_arrival + datetime.timedelta(hours=hours_to_arrival)
        else:
            return "Not available"

def load_flights_from_file(filename):
    flights = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                flights.append(Flight(*data))
    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit()
    return flights

def find_flights_by_attribute(flights, attribute, value):
    found_flights = [flight for flight in flights if getattr(flight, attribute, '') == value]
    return found_flights

def main():
    flights = load_flights_from_file("flights_data.txt")

    while True:
        print("\nAirport Flight Arrival Enquiry")
        print("1. Enquire by Flight Number")
        print("2. Enquire by Origin")
        print("3. Enquire by Aircraft Number")
        print("4. Enquire by Airline Name")
        print("5. Enquire by Airline Code")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4', '5']:
            attribute_map = {'1': 'flight_number', '2': 'origin', '3': 'aircraft_number', '4': 'airline_name', '5': 'airline_code'}
            attribute = attribute_map[choice]
            value = input(f"Enter {attribute.replace('_', ' ').title()}: ")
            matched_flights = find_flights_by_attribute(flights, attribute, value)
            if matched_flights:
                for flight in matched_flights:
                    print(f"Flight {flight.flight_number}: Estimated Arrival Time: {flight.calculate_estimated_arrival()}")
            else:
                print("No matching flights found.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()