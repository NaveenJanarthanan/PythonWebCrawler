import sqlite3
connection = sqlite3.connect("inspections.db")

cursor = connection.cursor()
#Uncomment the line below if you're running the program more than once, or you can delete the data file
cursor.execute("""DROP TABLE data;""")

facility_data = [ ("1313 MAIN STREET", "1313 MAIN ST", "NAPA", "CA", "94559", "11/02/2016", "Routine", "A"),
                  ("641 MAIN STREET", "641 MAIN ST", "SAINT HELENA", "CA", "94574", "11/22/2016","Routine", "A"),
                  ("A & A KITCHENS LLC", "391 LA FATA ST", "ST HELENA", "CA", "94574", "04/03/2012", "Routine", "A"),
                  ("A & B MARKET", "1855 OLD SONOMA RD", "Napa", "CA", "94558", "03/10/2016", "Routine", "A"),
                  ("A DOZEN VINTNERS", "3000 St. Helena Hwy N", "SAINT HELENA", "CA", "94574", "12/02/2011", "Routine", "A"),
                  ("A DOZEN VINTNERS", "3000 St. Helena Hwy N", "SAINT HELENA", "CA", "94574", "10/03/2012", "Routine", "A"),
                  ("A&W/KFC", "501 MAIN ST", "SAINT HELENA", "CA", "94574 ", "02/04/2013", "Routine", "A"),
                  ("A-1 FOOD & LIQUOR INC", "75 COOMBS ST", "NAPA", "CA", "94559", "02/19/2016", "Routine", "A"),
                  ("A-1 SANDWICH CO (DIET TO GO)", "429 Cabot RD S", "Francisco", "CA", "94080", "01/25/2013", "Routine", "A"),
                  ("ABC FOODS", "1825 Old Sonoma RD", "Napa", "CA", "94558", "03/10/2016", "Routine", "A")]

sql_command = """
CREATE TABLE data (
facility_number INTEGER PRIMARY KEY,
fname VARCHAR (20),
saddress VARCHAR (100),
city VARCHAR(50),
state VARCHAR (25),
zipcode VARCHAR(10),
inspectiond VARCHAR(20),
inspectiont VARCHAR(10),
inspectiong CHAR(1));"""

cursor.execute(sql_command)
for x in facility_data:
    format_str = """INSERT INTO data (facility_number, fname, saddress, city, state, zipcode, inspectiond, inspectiont, inspectiong)
    VALUES (NULL, "{facility}", "{add}", "{c}", "{s}", "{z}", "{date}", "{type}", "{grade}");"""

    sql_command = format_str.format(facility=x[0], add=x[1], c=x[2], s=x[3], z=x[4], date=x[5], type=x[6], grade=x[7])
    cursor.execute(sql_command)



#Uncomment the line below if you're running the program more than once, or you can delete the data file
cursor.execute("""DROP TABLE compliance;""")
sql_c = """
CREATE TABLE compliance (
facility_number INTEGER PRIMARY KEY,
fname VARCHAR (20),
violation_number1 VARCHAR (2) DEFAULT NULL,
violation_name1 VARCHAR (30) DEFAULT NULL,
violation_number2 VARCHAR (2) DEFAULT NULL,
violation_name2 VARCHAR (60) DEFAULT NULL,
violation_number3 VARCHAR (2) DEFAULT NULL,
violation_name3 VARCHAR (30) DEFAULT NULL,
violation_number4 VARCHAR (2) DEFAULT NULL,
violation_name4 VARCHAR (30) DEFAULT NULL,
violation_number5 VARCHAR (2) DEFAULT NULL,
violation_name5 VARCHAR (30) DEFAULT NULL);"""

cursor.execute(sql_c)
sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES (NULL, "1313 MAIN STREET", "35", "Equipment/Utensils - approved; installed; clean; good repair; capacity", "44", "Premises; personal/cleaning items; vermin-proofing", "48", "Plan Review", NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)


sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "641 MAIN STREET", "6", "Adequate handwashing facilities supplied & accessible", "35", "Equipment/Utensils - approved; installed; clean; good repair; capacity", NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A & A KITCHENS LLC", "14", "Food contact surfaces: clean and sanitized", "35", "Equipment/Utensils - approved; installed; clean; good repair; capacity", NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A & B MARKET", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A DOZEN VINTNERS", "35", "Equipment/Utensils - approved; installed; clean; good repair; capacity", "41", "Plumbing; proper backflow devices",  NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A DOZEN VINTNERS", "41", "Plumbing; proper backflow devices",  NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A&W/KFC", "14", "Food contact surfaces: clean and sanitized","41", "Plumbing; proper backflow devices", "42", "Garbage and refuse properly disposed; facilities maintained", "44", "Premises; personal/cleaning items; vermin-proofing", "45", "Floors, walls and ceilings: built, maintained, and clean");"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A-1 FOOD & LIQUOR INC", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "A-1 SANDWICH CO (DIET TO GO)", "39", "Thermometers provided and accurate",  NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)

sql_c = """INSERT INTO compliance (facility_number, fname, violation_number1, violation_name1, violation_number2, violation_name2, violation_number3, violation_name3, violation_number4, violation_name4, violation_number5, violation_name5)
    VALUES  (NULL, "ABC FOODS", NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"""
cursor.execute(sql_c)
connection.commit()

connection.close()


#sql_c = format_str.format(facility=p[0], vnumber1=p[1], vname1=p[2], vnumber2=p[3], vname2=p[4], vnumber3=p[5], vname3=p[6], vnumber4=p[7],  vname4=p[8], vnumber5=p[9], vname5=p[10])
