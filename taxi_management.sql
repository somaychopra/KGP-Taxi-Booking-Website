CREATE DATABASE TAXI_MANAGEMENT;
USE TAXI_MANAGEMENT;
CREATE TABLE `user` (
  `email` varchar(255) PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(11) NOT NULL
);

CREATE TABLE `driver` (
  `email` varchar(255) PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `rating` decimal,
  `is_available` boolean NOT NULL,
  `curr_car_number` varchar(12)
);

CREATE TABLE `admin` (
  `email` varchar(255) PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
);

CREATE TABLE `location` (
  `location_id` varchar(10) PRIMARY KEY,
  `location_name` varchar(50) NOT NULL,
  `is_outstation` boolean NOT NULL
);

CREATE TABLE `route` (
  `route_id` varchar(10) PRIMARY KEY,
  `loc_start` varchar(10) NOT NULL,
  `loc_end` varchar(10) NOT NULL,
  `distance` decimal NOT NULL
);

CREATE TABLE `car` (
  `number` varchar(12) PRIMARY KEY,
  `is_available` int NOT NULL,
  `number_seats` int NOT NULL,
  `current_loc` varchar(10) NOT NULL,
  `model` varchar(20) NOT NULL
);

CREATE TABLE `booking_received` (
  `booking_id` varchar(10) PRIMARY KEY,
  `car_num` varchar(12) NOT NULL,
  `driver_email` varchar(255) NOT NULL,
  `is_started` bool NOT NULL,
  `time_epochs` varchar(255) NOT NULL,
  `route_id` varchar(10) NOT NULL,
  `user_email` varchar(255) NOT NULL
);

CREATE TABLE `trip_completed` (
  `booking_id` varchar(10) PRIMARY KEY ,
  `time_epochs_start` varchar(255) NOT NULL,
  `time_epochs_end` varchar(255) NOT NULL,
  `driver_email` varchar(255) NOT NULL,
  `car_num` varchar(12) NOT NULL,
  `route_id` varchar(10) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `review_id` varchar(10) 
);

CREATE TABLE `review` (
  `review_id` varchar(10) PRIMARY KEY,
  `rating` int NOT NULL,
  `feedback_text` varchar(255) ,
  `driver_email` varchar(255) NOT NULL
);

ALTER TABLE `driver` ADD FOREIGN KEY (`curr_car_number`) REFERENCES `car` (`number`);

ALTER TABLE `route` ADD FOREIGN KEY (`loc_start`) REFERENCES `location` (`location_id`);

ALTER TABLE `route` ADD FOREIGN KEY (`loc_end`) REFERENCES `location` (`location_id`);

ALTER TABLE `car` ADD FOREIGN KEY (`current_loc`) REFERENCES `location` (`location_id`);

ALTER TABLE `booking_received` ADD FOREIGN KEY (`driver_email`) REFERENCES `driver` (`email`);

ALTER TABLE `booking_received` ADD FOREIGN KEY (`car_num`) REFERENCES `car` (`number`);

ALTER TABLE `booking_received` ADD FOREIGN KEY (`route_id`) REFERENCES `route` (`route_id`);

ALTER TABLE `booking_received` ADD FOREIGN KEY (`user_email`) REFERENCES `user` (`email`);

ALTER TABLE `trip_completed` ADD FOREIGN KEY (`driver_email`) REFERENCES `driver` (`email`);

ALTER TABLE `trip_completed` ADD FOREIGN KEY (`car_num`) REFERENCES `car` (`number`);

ALTER TABLE `trip_completed` ADD FOREIGN KEY (`route_id`) REFERENCES `route` (`route_id`);

ALTER TABLE `trip_completed` ADD FOREIGN KEY (`user_email`) REFERENCES `user` (`email`);

ALTER TABLE `trip_completed` ADD FOREIGN KEY (`review_id`) REFERENCES `review` (`review_id`);

DELIMITER $$
CREATE TRIGGER update_driver_ratings_insert AFTER INSERT ON review    
FOR EACH ROW BEGIN
	
	UPDATE driver
	SET rating = (SELECT SUM(review.rating)/COUNT(*) 
		FROM review 
		WHERE review.driver_email = NEW.driver_email)
    WHERE driver.email = NEW.driver_email; 
END$$
DELIMITER ;

INSERT INTO admin VALUES("abc@gmail.com","abc","pass");
INSERT INTO location VALUES("0000000000","Cab Base Point",0);
INSERT INTO location VALUES("1","MS",0);
INSERT INTO location VALUES("2","VS",0);
INSERT INTO location VALUES("3","SNIG",0);

INSERT INTO route VALUES ("I1","0000000000","0000000000",0);
INSERT INTO route VALUES ("I2","1","1",0);
INSERT INTO route VALUES ("I3","2","2",0);
INSERT INTO route VALUES ("I4","3","3",0);

INSERT INTO route VALUES ("A1","0000000000","1",5);
INSERT INTO route VALUES ("A2","0000000000","2",10);
INSERT INTO route VALUES ("A3","0000000000","3",15);
INSERT INTO route VALUES ("12","1","2",12);
INSERT INTO route VALUES ("21","2","1",12);
INSERT INTO route VALUES ("13","1","3",8);
INSERT INTO route VALUES ("23","2","3",8);
INSERT INTO route VALUES ("31","3","1",7);

INSERT INTO driver VALUES("d1@gmail.com","Nikhil Driver","Male",20,"pass1","9292929292",NULL,True,NULL);
INSERT INTO driver VALUES("d2@gmail.com","Second Driver","Male",20,"pass1","9292929292",NULL,True,NULL);
INSERT INTO driver VALUES("d3@gmail.com","Third Driver","Male",20,"pass1","9292929292",NULL,True,NULL);
INSERT INTO driver VALUES("d4@gmail.com","Good Driver","Female",20,"pass1","9292929292",NULL,True,NULL);
INSERT INTO driver VALUES("d5@gmail.com","Name5 Driver","Male",20,"pass1","9292929292",NULL,True,NULL);

INSERT INTO user VALUES("u1@gmail.com","Dvij","Male",20,"pass1","9992999200");
INSERT INTO user VALUES("u2@gmail.com","Somay","Male",20,"pass1","9992999200");
INSERT INTO user VALUES("u3@gmail.com","Nikp","Male",20,"pass1","9992999200");
INSERT INTO user VALUES("u4@gmail.com","User 4","Female",20,"pass1","9992999200");
INSERT INTO user VALUES("u5@gmail.com","User 5","Male",20,"pass1","9992999200");

INSERT INTO car VALUES("HR20AZ0001",True,5,"0000000000","Tesla - S class");
INSERT INTO car VALUES("RJ31AC0001",True,5,"0000000000","Audi Q5");
INSERT INTO car VALUES("GJ20AZ0540",True,5,"0000000000","Mercedes Benz");
INSERT INTO car VALUES("HR20AZ5001",True,5,"0000000000","Maruti 800");