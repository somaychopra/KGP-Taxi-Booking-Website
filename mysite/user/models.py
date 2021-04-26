
class User():
    def __init__(self,obj):
        self.email = obj['email']
        self.name = obj['name']
        self.gender = obj['gender']
        self.age = obj['age']
        self.password = obj['password']
        self.phone_number = obj['phone_number']


class Car():
    def __init__(self,obj):
        self.number = obj['number']
        self.is_available = obj['is_available']
        self.number_seats = obj['number_seats']
        self.current_loc = obj['current_loc']
        self.model = obj['model']
        

class Driver():
    def __init__(self,obj):
        self.email = obj['email'] 
        self.name = obj['name'] 
        self.gender = obj['gender']
        self.age = obj['age']
        self.password = obj['password']
        self.phone_number = obj['phone_number']
        self.rating = obj['rating']
        self.is_available = obj['is_available']
        self.curr_car_number = obj['curr_car_number']

class Admin():
    def __init__(self,obj):
        self.email = obj[0]
        self.name = obj[1]
        self.password = obj[2]

class Location():
    def __init__(self,obj) :
        self.location_id = obj[0]
        self.location_name = obj[1]
        self.is_outstation = obj[2]


class Route():
    def __init__(self,obj):
        self.route_id = obj['route_id']
        self.loc_start = obj['loc_start']
        self.loc_end = obj['loc_end']
        self.distance = obj['distance']



