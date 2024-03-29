use vanguard;

SELECT * FROM vanguard.demo;

SET global local_infile = 1;

SHOW VARIABLES LIKE "secure_file_priv";

LOAD DATA LOCAL INFILE '/Users/leilajavanmardi/Desktop/Leila/Coding_IronHack/Data_Analytics_Bootcamp/week5/Project/SQL/df_demo_clean.csv'
INTO TABLE demo
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/Users/leilajavanmardi/Desktop/Leila/Coding_IronHack/Data_Analytics_Bootcamp/week5/Project/SQL/df_demo_clean.csv' INTO TABLE demo FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
SHOW VARIABLES LIKE 'secure_file_priv';]]