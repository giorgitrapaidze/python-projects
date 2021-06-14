from datetime import datetime
import sqlite3

connection = sqlite3.connect("todo.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS todos(
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    date VARCHAR NOT NULL,
                    text VARCHAR NOT NULL,
                    deadline VARCHAR NOT NULL) """)


class Manager:

  
    def add_todo(date, text, deadline):
        cursor.execute("""INSERT INTO todos
                            (date, text, deadline)
                            VALUES
                            (?, ?, ?)""", (date, text, deadline))
        connection.commit()

        print("\nჩანაწერი წარმატებით დამატებულია!\n")
    
    
    def edit_todo(self, uid):

        text = input("შეიტანეთ ახალი ჩანაწერი:")
        deadline = input("შეიტანეთ დედლაინი:")
        date = datetime.now().strftime('%H:%M-%d/%m/%Y')

        cursor.execute("""UPDATE todos 
                            SET date = ?, text = ?, deadline = ?     
                            WHERE uid = ?;""", (date, text, deadline, uid))
        connection.commit()

        print("\nჩანაწერი წარმატებით ჩანაცვლდა!\n")
    
    
    def del_todo(self, uid):

        cursor.execute("""DELETE FROM todos
                            WHERE uid = ?;""", (uid,))

        connection.commit()

        print("ჩანაწერი წარმატებით წაიშალა!\n")

    
    
    def show_all(self):
        cursor.execute("""SELECT * from todos""")
        records = cursor.fetchall()
        for row in records:
            print(row)



def menu():
    
    choice = None
    manager = Manager()


    while choice != "exit" and choice != "quit":

        print("მენიუ: menus")
        print("1. ჩანაწერის დამატება")
        print("2. ჩანაწერის ჩანაცვლება")
        print("3. ჩანაწერის ამოშლა")
        print("4. ჩანაწერების ნახვა")
        print("დაწერეთ 'exit' ან 'quit' პროგრამიდან გამოსვლისთვის")

        choice = input("\nაირჩიეთ მოქმედება: choose ")


        if choice == "1":
            
            text = input("შეიტანეთ ტექსტი:")
            deadline = input("შეიტანეთ დედლაინი:")

            date = datetime.now().strftime('%H:%M-%d/%m/%Y')

            Manager.add_todo(date, text, deadline)



        elif choice == "2":
            
 

            while True:
                manager.show_all()

                index = input("აირჩიეთ ჩასანაცვლებელი ჩანაწერის N:")

                if not index.isdigit():
                    print("\nგთხოვთ შეიტანოთ რიცხვი!\n")
                    continue


                uid = int(index)


                manager.edit_todo(uid)

                break





        elif choice == "3":
  

                while True:
                    manager.show_all()

                    index = input("აირჩიეთ წასაშლელი ჩანაწერის N:")

                    if not index.isdigit():
                        print("\nგთხოვთ შეიტანოთ რიცხვი!\n")
                        continue


                    uid = int(index)


                    manager.del_todo(uid)

                    break



        elif choice == "4":
            
            manager.show_all()


        else:
            print("შეიტანეთ კორექტული მნიშვნელობა!")




menu()
