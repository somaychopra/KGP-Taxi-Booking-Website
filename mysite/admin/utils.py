import pymysql.cursors

# Connect to the database
def get_connection():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='chopra123',
                                database='TAXI_MANAGEMENT',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def validate_password(email,password):  
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `email` , `password` FROM `admin` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
    flag = True
    if result == None:
        result = "Entered email is not an Admin!"
        flag = False
        return flag,result
    if result['password']!=password:
        print(result['password'])
        result = "Incorrect Password"
        flag = False
    return flag,result

def add_car(number,number_seats,model): 
    if(number==""):
        return False, "Cab Plate Number empty!"
    if(number_seats==""):
        return False, "Number of seats empty!"
    if(model==""):
        return False, "Cab model empty!" 
    if(int(number_seats)<=1):
        return False, "Enter valid number of seats!"
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `number` FROM `car` WHERE `number`=%s"
            cursor.execute(sql, (number))
            result = cursor.fetchone()
            #print(result)
            flag = True
    

    connection = get_connection()
    with connection:
        if result == None: 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT `number` FROM `car` WHERE `number`=%s"
                cursor.execute(sql, (number))
                result = cursor.fetchone()
                flag = True
                sql = "INSERT INTO `car` VALUES (%s,1,%s,'0000000000',%s)"
                cursor.execute(sql, (number,number_seats,model)) 
                connection.commit()   
                flag = True
                return flag,"Car added Successful"
        else:
            return False, "Car Already Exists"

def add_location(location_id,location_name,is_outstation):  
    if(location_id==""):
        return False, "Location Id empty!"
    if(location_name==""):
        return False, "Location Name empty!"
    if(is_outstation==""):
        return False, "Outstation field empty!"
    if(int(is_outstation)<0 or int(is_outstation)>1):
        return False, "Outstation field can only be 0(for NO) or 1(for YES)"
    
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `location_id` FROM `location` WHERE `location_id`=%s OR `location_name`=%s"
            cursor.execute(sql, (location_id,location_name))
            result = cursor.fetchone()
            #print(result)
            flag = True
    connection = get_connection()
    with connection:
        if result == None: 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT `location_id` FROM `location` WHERE `location_id`=%s"
                cursor.execute(sql, (location_id))
                result = cursor.fetchone()
                flag = True
                sql = "SELECT COUNT(*) FROM `location`"
                cursor.execute(sql)
                result = cursor.fetchone()
                print(type(result['COUNT(*)']))
                counter = result['COUNT(*)'] + 1
                rand_id = f'{counter}'
                rand_id = "I"+rand_id 
                sql = "INSERT INTO `location` VALUES (%s,%s,%s)"
                cursor.execute(sql, (location_id,location_name,is_outstation)) 
                connection.commit()   
                sql = "INSERT INTO `route` VALUES (%s,%s,%s,0)"
                cursor.execute(sql, (rand_id,location_id,location_id)) 
                connection.commit()  
                flag = True
                return flag,"Location added Successful"
        else:
            return False, "Location Already Exists"

def loc_name_to_id(loc_name):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            #print(loc_name)
            sql = "SELECT `location_id` FROM `location` WHERE `location_name`=%s"
            cursor.execute(sql, (loc_name))
            result = cursor.fetchone()
            #print("Converted")
            return result['location_id']

def add_route(route_id,loc_start,loc_end,distance):
    print("HEMLLOOOOOOOOOOOOOOOOo") 
    if(route_id==""):
        return False, "Route Id Empty"
    if(distance==""):
        return False, "Distance field empty!"
    if(int(distance)<=0):
        return False, "Enter a valid distance"
    connection = get_connection()
    #print("Heyy")
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            print(loc_end)
            lloc_start_id = loc_name_to_id(loc_start)
            lloc_end_id = loc_name_to_id(loc_end)
            sql = "SELECT `route_id` FROM `route` WHERE `route_id`=%s OR (`loc_start`=%s AND `loc_end`=%s)"
            cursor.execute(sql, (route_id,lloc_start_id,lloc_end_id))
            result = cursor.fetchone()
            flag = True
            #print(result)
    connection = get_connection()
    with connection:
        if result == None: 
            with connection.cursor() as cursor:
            # Read a single record
                sql = "SELECT `route_id` FROM `route` WHERE `route_id`=%s"
                cursor.execute(sql, (route_id))
                result = cursor.fetchone()
                flag = True
                sql = "INSERT INTO `route` VALUES (%s,%s,%s,%s)"
                loc_start_id = loc_name_to_id(loc_start)
                loc_end_id = loc_name_to_id(loc_end)
                cursor.execute(sql, (route_id,loc_start_id,loc_end_id,distance)) 
                connection.commit()   
                flag = True
                return flag,"Route added Successful"
        else:
            return False, "Route Already Exists"

def allocate(driver_email,car_number):  
    if driver_email == None or driver_email == "" or car_number == "" or car_number == None:
        return False, "Empty Field"
    connection = get_connection()
    print("Agayaaaaaaaa")
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "UPDATE `driver` SET `curr_car_number` = %s WHERE `email` = %s"
            cursor.execute(sql, (car_number,driver_email))
            connection.commit()   
            result = cursor.fetchone()
            sql2 = "UPDATE `car` SET `is_available` = 0 WHERE `number` = %s"
            cursor.execute(sql2, (car_number))
            connection.commit()   
            result2 = cursor.fetchone()
            flag = True
        return flag,"Car Allocation Successful"

def get_driver_car_list() :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT email FROM driver WHERE curr_car_number IS NULL ORDER BY email"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            sql2 = "SELECT number FROM car WHERE is_available = 1 ORDER BY number"
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            print(result2)
            car_list = []
            for res in result2 :
                car_list.append(res['number'])
            driver_list = []
            for res in result :
                driver_list.append(res['email'])
            return driver_list,car_list

def get_loc_list() :
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT location_name FROM location ORDER BY location_name"
            cursor.execute(sql)
            result = cursor.fetchall()
            loc_list = []
            for res in result :
                loc_list.append(res['location_name'])
            return loc_list


