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
        self.location_id = obj['location_id']
        self.location_name = obj['location_name']
        self.is_outstation = obj['is_outstation']
class Booking_received():
    def __init__(self,obj) :
        self.booking_id = obj['booking_id']
        self.car_num = obj['car_num']
        self.driver_email = obj['driver_email']
        self.is_started = obj['is_started']
        self.time_epochs = obj['time_epochs']
        self.route_id = obj['route_id']
        self.user_email = obj['user_email']

class Trip_completed():
    def __init__(self,obj,vers = True) :
        if vers:
            self.booking_id = obj['booking_id']
            self.car_num = obj['car_num']
            self.driver_email = obj['driver_email']
            self.time_epochs_start = obj['time_epochs_start']
            self.time_epochs_end = 0
            self.route_id = obj['route_id']
            self.user_email = obj['user_email']
            self.review_id = None
        else:
            self.booking_id = obj.booking_id
            self.car_num = obj.car_num
            self.driver_email = obj.driver_email
            self.time_epochs_start = obj.time_epochs
            self.time_epochs_end = 0
            self.route_id = obj.route_id
            self.user_email = obj.user_email
            self.review_id = None

            
# class Booking_received():
#     def __init__(self,obj) :
#         self.booking_id = obj[0]
#         self.car_num = obj[1]
#         self.driver_email = obj[2]
#         self.is_started = obj[3]
#         self.time_epochs = obj[4]
#         self.route_id = obj[5]
#         self.user_email = obj[6]

class Route():
    def __init__(self,obj):
        self.route_id = obj[0]
        self.loc_start = obj[1]
        self.loc_end = obj[2]
        self.distance = obj[3]
    