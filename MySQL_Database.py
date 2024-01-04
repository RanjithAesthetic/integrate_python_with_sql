import mysql.connector
from tabulate import tabulate
con = mysql.connector.connect(host="localhost", user="root", password="", database="registration")

def insert():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    address = input("Enter Address: ")
    contact = input("Enter Contact: ")
    mailid = input("Enter MailId: ")

    res = con.cursor()
    sql = "insert into data(name,age,address,contact,mailid) values(%s,%s,%s,%s,%s)"
    res.execute(sql,(name,age,address,contact,mailid))
    con.commit()
    print("/n")
    print("Record Insert Successfully")

def select():
    res = con.cursor()
    sql = "SELECT * FROM data"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result,headers=["ID","NAME","AGE","ADDRESS","CONTACT","MAILID"]))

def update():
    print("1.Name")
    print("2.Age")
    print("3.Address")
    print("4.Contact")
    print("5.MailId")
    print("\n")
    option = int(input("\nWhich field you want to update?: "))
    if option ==1:
        primaryKey = input("Enter your Id: ")
        name = input("Enter your Name: ")
        cur = con.cursor()
        sql = "UPDATE data set name=%s where primaryKey = %s"
        cur.execute(sql,(name,primaryKey))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option ==2:
        primaryKey = input("Enter your Id: ")
        name = input("Enter your Age: ")
        cur = con.cursor()
        sql = "UPDATE data set age=%s where primaryKey = %s"
        cur.execute(sql, (name, primaryKey))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option ==3:
        primaryKey = input("Enter your Id: ")
        name = input("Enter your Address: ")
        cur = con.cursor()
        sql = "UPDATE data set address=%s where primaryKey = %s"
        cur.execute(sql, (name, primaryKey))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option ==4:
        primaryKey = input("Enter your Id: ")
        name = input("Enter your Contact: ")
        cur = con.cursor()
        sql = "UPDATE data set contact=%s where primaryKey = %s"
        cur.execute(sql, (name, primaryKey))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option ==5:
        primaryKey = input("Enter your Id: ")
        name = input("Enter your MaidId: ")
        cur = con.cursor()
        sql = "UPDATE data set mailid=%s where primaryKey = %s"
        cur.execute(sql, (name, primaryKey))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    else:
        print("Invalid")

def delete():
    primaryKey = int(input())
    res = con.cursor()
    sql = "DELETE FROM data where primaryKey=%s"
    res.execute(sql,(primaryKey,))
    con.commit()
    print("\n")
    print("Delete Successfully")

while True:
    print("/n")
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("/n")

    choice =int(input("Enter your Choice :"))
    if choice ==1:
        insert()
    elif choice ==2:
        select()
    elif choice ==3:
       update()
    elif choice ==4:
       delete()
    elif choice ==5:
        exit()
    else:
        print("Invalid Option...!!")

