import pymysql.cursors
from user.models import *


# Connect to the database
def get_connection() :
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='chopra123',
                                database='TAXI_MANAGEMENT',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def validate_password(email,password):  
    # connection = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='dvijvirat123',
    #                          database='TAXI_MANAGEMENT',
    #                          cursorclass=pymysql.cursors.DictCursor)
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
            sql = "SELECT `email`, `password` FROM `user` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            #print(result)
    flag = True
    if result == None:
        result = "User Not Found"
        flag = False
        return flag,result
    if result['password']!=password:
        result = "Incorrect Password"
        flag = False
    return flag,result

def get_user_details(email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT email, `name`, `gender`, age, password, phone_number FROM `user` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            print(result)
            obj = User(result)
            return obj

def get_driver_details(email) :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM driver WHERE driver.email=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            obj = Driver(result)
            return obj

def get_car_details(number) :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM car WHERE car.number=%s"
            cursor.execute(sql, (number))
            result = cursor.fetchone()
            obj = Car(result)
            return obj

def get_route_details(start,end) :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT route.route_id,route.loc_start,route.loc_end,route.distance FROM route as route, location as start, location as end WHERE route.loc_start=start.location_id AND route.loc_end=end.location_id\
                AND start.location_name=%s AND end.location_name=%s"
            cursor.execute(sql, (start,end))
            result = cursor.fetchone()
            if(result==None):
                return False
            print("Idhar")
            obj = Route(result)
            print(obj)
            return obj

def add_booking(car_num,driver_email,is_started,time_epochs,route_id,user_email):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO booking_received\
                VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (time_epochs[2:],car_num,driver_email,is_started,time_epochs,route_id,user_email))
            connection.commit()
            sql = "UPDATE driver\
                SET is_available=0 WHERE driver.email=%s"
            cursor.execute(sql, (driver_email))
            connection.commit()
            return time_epochs[2:]

def get_status(booking_id) :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT is_started FROM booking_received WHERE booking_id=%s"
            cursor.execute(sql, (booking_id))
            result = cursor.fetchone()
            if result==None :
                return "trip_completed"
            if result['is_started'] == False :
                return "waiting"
            return "in_car"

def register_feedback(booking_id,driver_email,feedback_id,rating,feedback):
    if int(rating)<0 or int(rating)>5 :
        return False, "Please rate between 0 to 5"
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql="INSERT INTO review VALUES(%s,%s,%s,%s)"
            cursor.execute(sql, (feedback_id,rating,feedback,driver_email))
            connection.commit()
            sql="UPDATE trip_completed SET review_id=%s WHERE booking_id=%s"
            cursor.execute(sql, (feedback_id,booking_id))
            connection.commit()
            return True, "Thanks for your valuble feedback!"
            
def get_loc_list() :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT location_name FROM location ORDER BY location_name"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            loc_list = []
            for res in result :
                loc_list.append(res['location_name'])
            return loc_list

def find_route(from_loc, to_loc, car_type):
    if from_loc=="" or to_loc=="" :
        return False, "Hey man!, either from or to is empty", None, None, None, 0
    if(get_route_details(from_loc,to_loc)==False):
        return False,"No route present!",None,None, None, 0
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            if car_type=="" :
                sql = "SELECT driver.email, car.number,f.location_id,r.distance \
                    FROM car as car, driver as driver, location as f, location as t, route as r\
                    WHERE t.location_name=%s AND car.current_loc=f.location_id\
                    AND r.loc_start=f.location_id AND r.loc_end=t.location_id\
                    AND driver.curr_car_number=car.number AND driver.is_available=1\
                    ORDER BY r.distance"
                print(sql)
                cursor.execute(sql, (from_loc))
                result = cursor.fetchone()
            if car_type!="" :
                sql = "SELECT driver.email, car.number,f.location_id,r.distance \
                    FROM car as car, driver as driver, location as f, location as t, route as r\
                    WHERE t.location_name=%s AND car.current_loc=f.location_id\
                    AND r.loc_start=f.location_id AND r.loc_end=t.location_id\
                    AND driver.curr_car_number=car.number AND car.model=%s AND driver.is_available=1\
                    ORDER BY r.distance"
                cursor.execute(sql, (from_loc, car_type))
                result = cursor.fetchone()
        if result == None: 
            with connection.cursor() as cursor:
            # Read a single record
                flag = False
                return flag,"Our bad!, no car available for this route at this moment",None,None,None,0
        else:
            print(result)
            return True, "Mil gyi, isko gaadi mil gyi",get_car_details(result['number']),get_driver_details(result['email']),get_route_details(from_loc,to_loc),result['distance']


def add_user(email,password,name,phone_number,age,gender):  
    # connection = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='',
    #                          database='TAXI_MANAGEMENT',
    #                          cursorclass=pymysql.cursors.DictCursor)
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `email`, name, gender, age, `password`, phone_number FROM `user` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            #print(result)
            flag = True
    

    # connection = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='',
    #                          database='TAXI_MANAGEMENT',
    #                          cursorclass=pymysql.cursors.DictCursor)
    connection = get_connection()
    with connection:
        if result == None: 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "INSERT INTO `user` (`email`, name, gender, age, `password`, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (email,name, gender, age, password, phone_number)) 
                connection.commit()   
                flag = True
                return flag,"Badhai Ho"
        else:
            return False, "Username Already Registered"

