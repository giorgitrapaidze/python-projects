import requests
from bs4 import BeautifulSoup


r = requests.get("https://geographyfieldwork.com/WorldCapitalCities.htm")
c = r.text


soup = BeautifulSoup(c, "html.parser")



table = soup.find("table", {"summary":"World Capitals"})
rows = table.find_all("tr")

countries_capitals = []
countries = []


for item in rows:

	for sup in item.find_all('sup'):
			sup.decompose()

	tds = item.find_all("td", {"height":"17"})

	try:
		country = tds[0].text.strip()
		capital = tds[1].text.strip()
	except IndexError:
		continue

	countries.append(country)
	country_capital = (country, capital)
	countries_capitals.append(country_capital)
 

while True:
    user_input = input("Please input a country: \n").capitalize()
    if user_input not in countries:
        print("\nInvalid input!")    
        continue
    else:
        break

for i in countries_capitals:
	 	if i[0] == user_input:
	 		print("\nThe Capital of " + i[0] + " is " +i[1] + ".")
 		

