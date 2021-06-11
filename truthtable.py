
from tkinter import *

def check(event):

	try:
		A = int(entry1.get())
		B = int(entry2.get())

		if (i.get() ==1):
			if A == 0 and B == 0:
				label1["text"] = "0"
			elif A == 0 and B == 1:
				label1["text"] = "0"
			elif A == 1 and B == 0:
				label1["text"] = "0"
			elif A == 1 and B == 1:
				label1["text"] = "1"
			else:
				label1["text"] = "შეიტანე 1 ან 0!"

		elif (i.get() ==2):
			if A == 0 and B == 0:
				label1["text"] = "0"
			elif A == 0 and B == 1:
				label1["text"] = "1"
			elif A == 1 and B == 0:
				label1["text"] = "1"
			elif A == 1 and B == 1:
				label1["text"] = "1"
			else:
				label1["text"] = "შეიტანე 1 ან 0!"
		else:
			label1["text"] = "მონიშნეთ AND ან OR"
	except ValueError:
		label1["text"] = "შეიტანეთ რიცხვი 1 ან 0!"




window = Tk()

window.title("Truth Table")
i = IntVar()

entry1 = Entry(window, width = 3, font = 16)
entry2 = Entry(window, width = 3, font = 16)
r1 = Radiobutton(window, text="AND", value=1, variable=i)
r2 = Radiobutton(window, text="OR", value=2, variable=i)
button1 = Button(window, text = "შემოწმება")
label1 = Label(window, width = 30, font = 16)
# ვქმნით პასუხის გამომტან არეს შესაბამისი ზომებით


entry1.grid(row = 0, column = 0)
entry2.grid(row = 0, column = 1)
r1.grid(row = 1, column = 0, pady = (15,25))
r2.grid(row = 1, column = 1)
button1.grid(row = 2, column = 0, columnspan = 2)
label1.grid(row = 3, column = 0, columnspan = 2, pady = (20))


# ვაბამთ მაუსის მარცხენა ღილაკის დაჭერის მომენტს შესაბამის ფუნქციასთან
button1.bind("<Button-1>", check)

window.mainloop()  