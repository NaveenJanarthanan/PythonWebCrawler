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


#sql_command = """INSERT INTO mainstreet (address, inspectiond, inspectiont, inspectiong)
#    VALUES(NULL, "facility_name1", "address1", "inspection_date1", "inspection_type1", "inspection_grade");"""



connection.commit()

connection.close()
