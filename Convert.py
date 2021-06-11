def convert():

    options = ["Kilometer", "Meter", "Centimeter", "Mile"]
    for i in range(len(options)):
        print("\n" + str(i+1) + ":", options[i])

    

    while True:
        inp = int(input("\nPlease choose a unit which you want to convert. Enter a number 1-4: "))
        if inp not in range(1, 5):
            print("\nInvalid input! Please Enter a number 1-4: ")    
            continue
        else:
            break

    inp_index = inp
    inp = options[int(inp)-1]
        

    number = int(input("\nHow many " + str(inp) + "s" + " would you like to convert?\n"))
    
    to_options = options[:int(inp_index-1)] + options[(int(inp_index-1) + 1):]
    for i in range(len(to_options)):
        print("\n"+str(i+1) + ":", to_options[i])

    

    while True:
        to_inp = int(input("\nWhich unit would you like to convert to? \nEnter a number 1-3: "))
        if to_inp not in range(1, 4):
            print("\nInvalid input! Please Enter a number 1-3: ")    
            continue
        else:
            break
    
    inp_index = to_inp
    to_inp = to_options[int(to_inp)-1]

        
    ratio = 0.621371
    result = 0
    if inp == "Kilometer" and to_inp == "Mile":
        result = number * ratio
    elif inp == "Kilometer" and to_inp == "Meter":
        result = number / 1000
    elif inp == "Kilometer" and to_inp == "Centimeter":
        result = number / 100000
    elif inp == "Mile" and to_inp == "Kilometer":
        result = number / ratio
    elif inp == "Mile" and to_inp == "Meter":
        result = number / ratio * 1000
    elif inp == "Mile" and to_inp == "Centimeter":
        result = number / ratio * 100000
    elif inp == "Centimeter" and to_inp =="Meter":
        result = number / 100
    elif inp == "Centimeter" and to_inp =="Kilometer":
        result = number / 100000
    elif inp == "Centimeter" and to_inp =="Mile":
        result = number * ratio / 100000
    elif inp == "Meter" and to_inp =="Mile":
        result = number * ratio / 1000
    elif inp == "Meter" and to_inp =="Centimeter":
        result = number / 100
    elif inp == "Meter" and to_inp =="Kilometer":
        result = number / 1000      
    else:
        print("error")
        pass
    
    
    print("\n" + str(number) + " " + str(inp) + "s" + " equals to " + str(round(result, 3)) + " " + str(to_inp) + "s")
    pass

convert()


