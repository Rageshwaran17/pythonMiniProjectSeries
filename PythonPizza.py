print("!!! Welcome to python pizza deliveries!")
size = input("What size pizza you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if(size == 'S'):
    bill = 15
elif(size == 'M'):
    bill = 20
elif(size == 'L'):
    bill = 25
else:
    print("Invalid input given")

if(pepperoni == 'Y' and size == 'M' or size == 'L'):
    bill+=3
if(pepperoni == 'Y' and size == 'S'):
    bill+=2
if(extraCheese == 'Y'):
    bill+=1
print(f'''Your final bill is: ${bill}''')