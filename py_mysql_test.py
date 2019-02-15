# pip3 install mysql-connector

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raw_python"

)

connect = db.cursor()


def view_data():
    select_sql = "SELECT * FROM student"
    connect.execute(select_sql)
    student_data = connect.fetchall()
    for data in student_data:
        print(data)


while True:
    choice = input(
        "Enter Your Choice \n 1 For New Record \n 2 For View Record \n 3 For Delete Record \n 4 For Update Record \n 5 For Exit")
    if choice == '1':
        name = input("Enter Your Name\n\t")
        address = input("Enter Your Address\n\t")
        insert_sql = "INSERT INTO student(name,address) VALUES(%s,%s)"
        value = (name, address)
        connect.execute(insert_sql, value)
        db.commit()
        view_data()
    elif choice == '2':
        view_data()
    elif choice == '3':
        id = input("Enter Id Which You Want To Delete\t")
        delete_sql = "DELETE FROM student WHERE id=%s"
        value = (id,)
        connect.execute(delete_sql, value)
        db.commit()
        view_data()
    elif choice == '4':
        id = input("Enter id Which You Want to Update")
        select_one = "SELECT * FROM student WHERE id=%s"
        value = (id,)
        connect.execute(select_one, value)
        data = connect.fetchall()
        for i in data:
            print(data)
        name = input("Enter Name For Update")
        address = input("Enter Address For Update")
        update_sql = "UPDATE `student` SET `name`=%s,`address`=%s WHERE id=%s"
        update_value = (name, address, id)
        connect.execute(update_sql, update_value)
        db.commit()
        view_data()
    elif choice == '5':
        break
    else:
        print("Your Choice Is Wring")
db.close()
