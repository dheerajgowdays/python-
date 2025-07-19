import csv
name=input("What's you name? ")
home =input("What's you home? ")

with open("students.csv" , "a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home}) 