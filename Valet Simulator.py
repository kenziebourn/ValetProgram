#Github: kenziebourn
#By: McKenzie Bourn
#This program is a Valet simulator that stores cars when they are in the lot and allows customers to request their car to be pulled
#Daily rates are $10/hr , Overnight rates are a flat $45/night (>24hrs)

#There are four classes:
#Vehicle - Constructor with base attributes of a vehicle

#Car  - subclass of vehicle

#Motorcycle - subclass of vehicle

#Garage
#Displays spots available in Garage
#Adds/Removes vehicles from Garage
#Shows vehicles in Garage
#Charges appropriate rate when vehicle leaves
#Allows overnight customers to request car (unlimited in/out priviledges)

#Night Audit feature: program will create CSV file of all vehicle information for current guests in Garage sorted in alphabetical order (guest names) using Quicksort Algorithm

class Vehicle:
    """Represents the basic vehicle attributes"""
    def __init__(self,ticket_number, name, color, make, model,):
        """initializes the Vehicle item with ticket number, guest name, make, model , color """
        self._ticket_number= ticket_number
        self._name= name
        self._color = color
        self._make= make
        self._model= model

    def __repr__(self):
        """Returns printable representation of vehicle attributes"""
        return f'{self._ticket_number}, {self._name}, {self._color}, {self._make}, {self._model}'

    #Get methods
    def get_ticket_number(self):
        """gets valet ticket number"""
        return self._ticket_number

    def get_name(self):
        """gets name for owner of vehicle"""
        return self._name

    def get_make(self):
        """gets make of vehicle"""
        return self._make

    def get_model(self):
        """gets model of vehicle"""
        return self._model

    def get_color(self):
        """gets color of vehicle"""
        return self._color

class Car(Vehicle):
    """Represents a Car inherited from Vehicle class"""
    def __init__(self, ticket_number, name, color, make, model):
        super().__init__(ticket_number, name, color, make, model)

class Motorcycle(Vehicle):
    """Represents a Motorcycle inherited from Vehicle class"""
    def __init__(self, ticket_number, name, color, make, model):
        super().__init__(ticket_number, name, color, make, model)

class LotFullError(Exception):
    """Represents base class inheriting from Exception"""
    #used to define custom exception LotFullError
    pass

class UnavailableError(Exception):
    """Represents base class inheriting from Exception"""
    #used to define custom exception UnavailableError
    pass

class Garage:
    """Represents a database of vehicles currently in valet possession"""
    def __init__(self):
        self._vehicles_added = []
        self._spots = 30 #Max capacity of 30 spots in garage
        self._vehicle_info = {}
        self._data = []

    def spots_available(self):
        """Method to return numbers of spots left in Garage"""
        return self._spots

    def add_vehicle(self, vehicle):
        """Method used to add vehicle to Garage object"""
        #Each vehicle is assigned to a parking spot
        self._spot_numbers = ['P1', 'P2', 'P3', 'P4', 'P5','P6', 'P7', 'P8', 'P9', 'P10',
                             'P11', 'P12', 'P13', 'P14', 'P15','P16', 'P17', 'P18', 'P19', '20',
                             'P21', 'P22', 'P23', 'P24', 'P25','P26', 'P27', 'P28', 'P29', 'P30']

        # Check if spots are available
        if self._spots > 0:
            self._vehicles_added.append(str(vehicle).split(', '))
            self._spots -= 1
            #vehicle info dictionary modified so that car attributes are stored as values under associated key
            self._vehicle_info = {'Spot Number': [],'Ticket Number': [], 'Guest Name': [], 'Vehicle Color': [], 'Vehicle Make': [], 'Vehicle Model': [] }

            #iterate through the cars_added list to access all the cars in the garage
            for index, i in enumerate(self._vehicles_added):

                #appends vehicle details to appropriate key
                self._vehicle_info['Spot Number'].append(self._spot_numbers[index])
                self._vehicle_info['Ticket Number'].append(i[0])
                self._vehicle_info['Guest Name'].append(i[1])
                self._vehicle_info['Vehicle Color'].append(i[2])
                self._vehicle_info['Vehicle Make'].append(i[3])
                self._vehicle_info['Vehicle Model'].append(i[4])

            return "Vehicle successfully added to lot."

        else:
            raise LotFullError


    def remove_vehicle(self, ticket_number, hours):
        current_tickets = len(self._vehicle_info['Ticket Number']) #amount of ticket numbers issued assigned to variable
        if ticket_number not in self._vehicle_info['Ticket Number']: #checks if ticket_number entered is in ticket number of vehicle info dictionary
            raise UnavailableError
        else:
            for index, value in enumerate(self._vehicle_info['Ticket Number']):
                if value == ticket_number:
                    print("Now removing vehicle:")
                    print("Ticket Number:",self._vehicle_info['Ticket Number'][index])
                    print("Guest Name:", self._vehicle_info['Guest Name'][index])
                    print("Vehicle Color:", self._vehicle_info['Vehicle Color'][index])
                    print("Vehicle Make:", self._vehicle_info['Vehicle Make'][index])
                    print("Vehicle Model:", self._vehicle_info['Vehicle Model'][index])

                    vehicles_removed = self._vehicle_info['Ticket Number'].pop(index)
                    self._vehicle_info['Guest Name'].pop(index)
                    self._vehicle_info['Vehicle Color'].pop(index)
                    self._vehicle_info['Vehicle Make'].pop(index)
                    self._vehicle_info['Vehicle Model'].pop(index)

                    self._spots += 1


        stayover = input("Is the guest returning (y/n)? ")
        response = stayover.lower() #convert user response to all lowercase in order to handle capital entries
        if response == 'no' or response == 'n':
            hours = int(input("Please enter the amount of hours vehicle has been in Garage: ")) #charges appropriate rates based on hours in Garage
            if hours < 0:
                return "Error: Please enter a positive value"
            while hours >= 0:
                if hours <= 24:
                    self.total = hours *10
                    return f'Total Amount due: ${self.total}'
                else:
                    self.total = hours / 24 * 45
                    return f'Total Amount due: ${self.total}'
                break
        if response == 'yes' or response == 'y':
            return "Vehicle successfully removed."


    def cars_in_garage(self):
        """Method returns information on current vehicles in garage"""
        for i in self._vehicle_info.items():
            print(i)

    def save_as_csv(self):
        headers = ["Ticket Number" , "Guest Name", "Vehicle Color", "Vehicle Make", "Vehicle Model"]
        header_string = ','.join([str(x) for x in headers])  # separates headers with commas
        with open('audit.csv', 'w') as outfile:  # writes column headers as first line in output file
            outfile.write(str(header_string) + '\n')\
        for i in self._vehicle_info.items():
            return i
        with open('audit.csv','w') as outfile:
            outfile.write(i + '\n')


my_lot = Garage()
print(my_lot.spots_available())
my_lot.add_vehicle(Car('130', 'McKenzie', 'Silver','Mazda','CX-5'))
my_lot.add_vehicle(Car('131', 'Thalia', 'Black','Porsche','Macan'))
my_lot.add_vehicle(Car('132', 'Tom', 'White','Jeep', 'Renegade'))
my_lot.add_vehicle(Motorcycle('133', 'Ben', 'Red','Yamaha','R1'))
my_lot.cars_in_garage()
print(my_lot.remove_vehicle('131', '10'))
print(my_lot.spots_available())
my_lot.save_as_csv()





