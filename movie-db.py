import sqlite3

connection = sqlite3.connect("exam.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
					uid INTEGER PRIMARY KEY AUTOINCREMENT,
					name VARCHAR NOT NULL,
					studio VARCHAR NOT NULL) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS info(
					sid INTEGER NOT NULL,
					year INTEGER NOT NULL,
					imdb REAL NOT NULL) """)

class Movie:

	def __init__(self, name, studio):
		self.name = name
		self.studio = studio

		cursor.execute("""INSERT INTO movies
							(name, studio)
							VALUES
							(?, ?)""", (self.name, self.studio))
		connection.commit()

		cursor.execute("SELECT last_insert_rowid()")

		self.uid = cursor.fetchone()[0]



	def add_movie (name, studio):
		cursor.execute("""INSERT INTO movies 
							(name, studio)
							VALUES
							(?,?)""",
							(name, 
							studio))

		connection.commit()

	def show_all():
		cursor.execute("""SELECT uid, name from movies""")
		records = cursor.fetchall()
		for row in records:
			print(row)


	def edit_movie (uid):
		new_name = input("Please enter the new movie name: ")
		new_studio = input("Please enter the new studio name: ")

		cursor.execute("""UPDATE movies 
							SET name = ?
							WHERE uid = ?""", (new_name, uid))
		cursor.execute("""UPDATE movies
							SET studio = ?
							WHERE uid = ?""", (new_studio, uid))
		connection.commit()



	def del_movie (uid):

		cursor.execute("""DELETE FROM movies
							WHERE uid = ?;""", (uid,))

		connection.commit()


class Info:


	def add_info (uid, year, imdb):
		cursor.execute("""INSERT INTO info 
							(sid, year, imdb)
							VALUES
							(?,?,?)""",
							(uid, 
							year,
							imdb))

		connection.commit()

	def show_all():
		cursor.execute("""SELECT movies.uid, name, studio, info.year,
									 info.imdb
								FROM movies JOIN info ON movies.uid = info.sid
								""")
		data = cursor.fetchall()

		for item in data:
			print(item)


	def edit_info (uid):
		new_year = input("Please enter the correct release year: ")
		new_imdb = input("Please enter the changed imdb score: ")

		cursor.execute("""UPDATE info 
							SET year = ?
							WHERE sid = ?""", (new_year, uid))
		cursor.execute("""UPDATE info
							SET imdb = ?
							WHERE sid = ?""", (new_imdb, uid))
		connection.commit()



	def del_info (uid):

		cursor.execute("""DELETE FROM info
							WHERE sid = ?;""", (uid,))

		connection.commit()





def menu():


	choice = None


	while choice != "exit" and choice != "quit":

		print("Menu")
		print("1. Add movie")
		print("2. Edit movie")
		print("3. Delete movie")
		print("4. Add Info")
		print("5. Edit Info")
		print("6. Delete Info")
		print("7. Search movies by Year")
		print("Type 'exit' or 'quit' to leave the software")

		choice = input("\n choose: ")


		if choice == "1":
            
			Movie.add_movie(input("Please enter the movie name: "),
						input("Please enter the studio name: "))


		elif choice == "2":

			Movie.show_all()

			inp_uid = int(input("Please enter the movie id to edit: "))
			


            
			Movie.edit_movie(inp_uid)


		elif choice == "3":

			Movie.show_all()

			inp_uid = int(input("Please enter the movie id to delete: "))

			Movie.del_movie(inp_uid)


		elif choice == "4":

			Movie.show_all()

			inp_uid = int(input("Please enter the movie id to add info:  "))

			Info.add_info(inp_uid, input("Release year: "), input("Imdb Score: "))


		elif choice == "5":

			Info.show_all()

			inp_sid = int(input("Please enter the movie id to edit info: "))

			Info.edit_info(inp_sid)


		elif choice == "6":

			Info.show_all()

			inp_sid = int(input("Please enter the movie id to delete info: "))

			Info.edit_info(inp_sid)

		elif choice == "7":
			try:
				inp_year = int(input("Search movies by Year! \n Enter the year: "))
			except ValueError:
				Print("No movie found")
			cursor.execute("""SELECT movies.uid, name, studio, info.year,
										 info.imdb
									FROM movies JOIN info ON movies.uid = info.sid
									WHERE info.year=?""",(inp_year,)
									)
			data = cursor.fetchall()

			for item in data:
				print(item)

			


		else:
			print("Enter the correct value!")




menu()







