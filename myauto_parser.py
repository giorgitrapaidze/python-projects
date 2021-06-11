import requests
from bs4 import BeautifulSoup


car_id = [[25, "mercedes-benz"],
		  [2, "audi"],
		  [12, "ford"],
		  [19, "jeep"],
		  [22, "land-rover"],
          [29, "mitsubishi"],
          [33, "porsche"],
          [41, "toyota"],
          [42, "volskwagen"],
          [14, "honda"]]



choice = None



while choice != "exit":
	print("Menu: ")
	print("1. Mercedes-benz")
	print("2. Audi")
	print("3. Ford")
	print("4. Jeep")
	print("5. Land-rover")
	print("6. Mitsubishi")
	print("7. Porsche")
	print("8. Toyota")
	print("9. Vokswagen")
	print("10. Honda")
	print("\nდაბეჭდეთ 'exit' პროგრამიდან გამოსასვლელად")



	choice = input("\nშეიყვანეთ მანქანის მარკის შესაბამისი რიცხვი:  ")
	
	if choice.isdigit():
		if int(choice) not in range(1, 11):
			print("\nგთხოვთ შეიყვანეთ რიცხვი დიაპაზონში 1-10!")    
			continue
		else:
			pass
	elif choice == "exit":
		break
	else:
		print("\nგთხოვთ შეიყვანეთ რიცხვი!")
		continue				


	while True:		
			year = input("\nშეიყვანეთ მანქანის გამოშვების წელი: ")
			if year.isdigit():
				if int(year) not in range(1900, 2022):
					print("\nგთხოვთ შეიყვანეთ რიცხვი დიაპაზონში 1900-2021!")    
					continue
				else:
					break
			elif choice == "exit":
				break
			else:
				print("\nგთხოვთ შეიყვანეთ რიცხვი!")
				continue


	year = int(year)
	choice = int(choice)

	car = ""

	if choice in range(1, 11):
		car = (car_id[choice - 1])


	URL = f"https://www.myauto.ge/ka/s/00/0/{car[0]}/00/{year}/{year}/00/00/{car[1]}-{year}-{year}?stype=0&marka={car[0]}&year_from={year}&year_to={year}&currency_id=3&det_search=0&ord=7&keyword=&category_id=m0&page=1"

	# print(URL)




	h = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	}
  

	prerequest = requests.get(URL, headers = h)
	precontent = prerequest.text

	presoup = BeautifulSoup(precontent, "html.parser")

	li = presoup.find("li", {"class":"last-page"})


	try:
		link = li.find("a")["href"]
	except AttributeError:
		print(f"\n{year} წლის გამოშვების {car[1]} არ მოიძებნა.\n")
		continue

	position = link.find("page=") + 5

	endnumber = int(link[position:])



	BASE_URL = URL[:-1]

	carinfo =""
	number = 0

	for page in range(1, endnumber + 1):


		r = requests.get(BASE_URL + str(page), headers = h)
		c = r.text

		soup = BeautifulSoup(c, "html.parser")

		data = soup.find("div", {"class":"search-lists-container"})
		rows = data.find_all("div", {"class":"current-item"})



		for item in rows:

			title = item.find("h4").text.strip()
			mileage = item.find("div", {"data-engin":"გარბენი"}).text.strip()
		

			try:
				prices = item.find_all("span", {"class":"car-price"})
				gel = prices[0].text.strip()
				usd = prices[1].text.strip()

			except:
				gel = None
				usd = None

			
			
			number += 1

			cardata = f"განცხადება N{number}\n {title}\n გარბენი: {mileage}\n ფასი: {gel} ლარი  {usd} დოლარი\n\n"
			carinfo += cardata


	file = open(f"{car[1]}{year}data.txt", "w", encoding = "utf-8")
	file.write(carinfo)
	print(f"{number} შედეგი ჩაიწერა ფაილში {car[1]}{year}data.txt")

