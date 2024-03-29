create database vanguard;
use vanguard;

CREATE TABLE demo (
client_id INT,
 clnt_tenure_yr FLOAT,
 clnt_tenure_mnth FLOAT,
 clnt_age FLOAT,
 gendr VARCHAR(255),
 num_accts FLOAT,
 bal FLOAT,
 calls_6_mnth FLOAT,
 logons_6_mnth FLOAT,
 PRIMARY KEY (`client_id`)
 );
 CREATE TABLE experiment (
 client_id INT,
 variation VARCHAR(255),
 CONSTRAINT `experiment_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `demo` (`client_id`)
 );
CREATE TABLE web (
client_id INT,
process_step VARCHAR(255), 
date_time VARCHAR(255),
 CONSTRAINT `web_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `demo` (`client_id`)
);
