import sqlite3
connection = sqlite3.connect("inspections.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM data")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print (r)
cursor.execute("SELECT * FROM data")
print("\nfetch one:")
res = cursor.fetchone()
print(res)

print("")
print("")
cursor.execute("SELECT * FROM compliance")
print("fetchall:")
result = cursor.fetchall()
for d in result:
    print (d)
cursor.execute("SELECT * FROM compliance")
print("\nfetch one:")
res = cursor.fetchone()
print(res)
