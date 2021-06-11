from datetime import datetime

class Zodiac():
	"""docstring for Zodiach"""
	def __init__(self):
		self.name = input("Please enter your name: ")

		while True:

			try:
				self.date = datetime.strptime(input("Enter date(dd/mm/yyyy): "), "%d/%m/%Y")
				break

			except ValueError: 
				print("Please enter birth date in following format (dd/mm/yyyy): ")



	zodiacs = [(120, 'Capricorn'), (218, 'Aquarius'), (320, 'Pisces'), (420, 'Aries'), (521, 'Taurus'),
		   (621, 'Gemini'), (722, 'Cancer'), (823, 'Leo'), (923, 'Virgo'), (1023, 'Libra'),
           (1122, 'Scorpion'), (1222, 'Saggitarius'), (1231, 'Capricorn')]


	def get_zodiac_of_date(self):
		date_number = int(self.date.strftime("%m") + 
						self.date.strftime("%d"))
		for z in self.zodiacs:
			if date_number <= z[0]:
				print("Hello "  + self.name +  ", Your zodiac is "  + z[1] + ".")
				return

	    


a = Zodiac()
a.get_zodiac_of_date()


		


		