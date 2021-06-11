import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk


r = requests.get("https://www.worldometers.info/coronavirus/")
c = r.text

soup = BeautifulSoup(c, "html.parser")

data = soup.find("table", {"id":"main_table_countries_today"})
rows = data.find_all("a", {"class":"mt_a"})


countries = [str(r.text.strip()) for r in rows]


def country_stats(country1):

	for r in rows:
		link = r.get("href")
		try:
			country = r.text.strip()

			if country1.upper()==country.upper():
				
				rNew = requests.get(f"https://www.worldometers.info/coronavirus/{link}")
				cNew = rNew.text

				soup1 = BeautifulSoup(cNew, "html.parser")

				print(soup1)

				rows1 = soup1.find_all("div",{"style":"margin-top:15px;"})


				for i in rows1:
					return f"{country} \nstats: \n{i.text}"

			continue

		except IndexError:
			return "No data for the given country"
			continue

def check(event):

		country = str(entry.get())
		if country.capitalize() in countries or country == "USA":
			label["text"] = country_stats(country)
		else:
			label["text"] = "That's not a country! "




window = Tk()

window.title("Coronavirus stats")

entry = Entry(window, width = 30, font = 8)

button = Button(window, text = "Search for Country's Recovered stats ")
label0 = Label(window, width = 30,  font = 8)
label0["text"] = "Please Enter the country"
label = Label(window, width = 30,  font = 8)
entry.grid(row = 1, column = 0)

label0.grid(row = 0, column = 0)
button.grid(row = 2, column = 0)
label.grid(row = 3, column = 0, columnspan = 2, pady = (20))

button.bind("<Button-1>", check)


window.mainloop()