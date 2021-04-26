import pymysql.cursors
from mysite.models import *
import time
# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='',
#                              database='dbms_proj',
#                              cursorclass=pymysql.cursors.DictCursor)
def get_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='chopra123',
                             database='TAXI_MANAGEMENT',
                             cursorclass=pymysql.cursors.DictCursor)


def validate_password(email,password):  
    connection = get_connection()
    with connection:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `email`, `password` FROM `driver` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            #print(result)
    flag = True
    if result == None:
        result = "Driver name Not Found"
        flag = False
        return flag,result
    if result['password']!=password:
        result = "Incorrect Password"
        flag = False
    return flag,result


def add_driver(obj):  
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `email`, `password` FROM `driver` WHERE `email`=%s"
            cursor.execute(sql,obj['email'] )
            result = cursor.fetchone()
            #print(result)
            flag = True
    

    connection = get_connection()
    with connection:
        if result == None: 
            with connection.cursor() as cursor:
                flag = True
                sql = "INSERT INTO `driver` (`email`, `name`,`gender`,`age`,`password`,`phone_number`,`rating`,`is_available`,`curr_car_number`) VALUES (%s, %s,%s,%s,%s, %s,%s,%s,%s)"
                cursor.execute(sql, (obj['email'],obj['name'],obj['gender'],obj['age'],obj['password'],obj['phone_number'],obj['rating'],obj['is_available'],obj['curr_car_number'])) 
                connection.commit()   
                flag = True
                return flag,"Badhai Ho"
        else:
            return False, "Driver Already Registered"

def get_driver_details(email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `driver` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
    print(email)
    print(result)
    return Driver(result)

def get_location_list():
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `location`"
            cursor.execute(sql)
            results = cursor.fetchall()
    locs = []
    for result in results:
        locs.append(Location(result))
    return locs
def get_booking(email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `booking_received` where `driver_email` = %s"
            cursor.execute(sql,(email))
            result = cursor.fetchone()
    if result == None or len(result) == 0:
        return None
    else:
        return Booking_received(result)

def get_car_details(car_num):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `car` where `number` = %s"
            cursor.execute(sql,(car_num))
            result = cursor.fetchone()
    if result == None or len(result) == 0:
        return None
    else:
        return Car(result)
    

#def get_completed_trips:
    ######
def get_route_details(route_id):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `route` where `route_id` = %s"
            cursor.execute(sql,(route_id))
            result = cursor.fetchone()
    loc_start = get_location_from_id(result['loc_start'])
    loc_end = get_location_from_id(result['loc_end'])
    distance = result['distance']
    return loc_start, loc_end, distance

    ########
def get_location_from_id(location_id):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `location` where `location_id` = %s"
            cursor.execute(sql,(location_id))
            result = cursor.fetchone()
    if result == None or len(result) == 0:
        return None
    else:
        return Location(result)
    #######
def get_user_details(user_email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `user` where `email` = %s"
            cursor.execute(sql,(user_email))
            result = cursor.fetchone()
    if result == None or len(result) == 0:
        return None
    else:
        return User(result)
    #######
def get_car_details(car_num):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `car` where `number` = %s"
            cursor.execute(sql,(car_num))
            result = cursor.fetchone()
    if result == None or len(result) == 0:
        return None
    else:
        return Car(result)
    #######
def set_unavailable(driver_email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "update driver set is_available = False where email = %s"
            cursor.execute(sql,(driver_email))
            #result = cursor.fetchall()
            connection.commit()   

def set_available(driver_email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "update driver set is_available = True where email = %s"
            cursor.execute(sql,(driver_email))
            connection.commit()   

def start_trip(booking_id):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "update booking_received set is_started = True where booking_id = %s"
            cursor.execute(sql,(booking_id))
            connection.commit()   
    
def end_trip(booking_id,driver_email):
    print("****************************************")
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "select * from booking_received where booking_id = %s"
            cursor.execute(sql,(booking_id))
            result = cursor.fetchone()
            sql = "delete from booking_received where booking_id = %s"
            cursor.execute(sql,(booking_id))
            connection.commit()   

    booking = Booking_received(result)
    comp = Trip_completed(booking,False)
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE driver\
                SET is_available=1 WHERE driver.email=%s"
            cursor.execute(sql, (driver_email))

            # Read a single record
            sql = "INSERT INTO trip_completed (booking_id,time_epochs_start,time_epochs_end,driver_email,car_num,route_id,user_email,review_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql,(comp.booking_id,comp.time_epochs_start,comp.time_epochs_end,comp.driver_email,comp.car_num,comp.route_id,comp.user_email,comp.review_id))
            connection.commit()

            sql = "select * from route where route_id = %s"
            cursor.execute(sql,(comp.route_id))
            result = cursor.fetchone()
            update_location(comp.car_num,result['loc_end'])
    
def update_location(car_number,location_id):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "update car set current_loc =  %s where number = %s"
            cursor.execute(sql,(location_id,car_number))
            connection.commit()


    
       
