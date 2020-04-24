def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an number! Try again.")
       continue
    else:
       return userInput 
       break 
     

print("What is your name?")
user_name = input()
print("Hello, " + user_name + "!")


#blinmaker
print("Blinmaker is starting...")

print("How many eggs do you have?")
eggs_ammount = inputNumber("(enter just numbers!)   ")
print("you have chosen " + str(eggs_ammount) + " eggs" )

print("How much mililiters of milk do you have?")
milk_ammount = inputNumber("(enter just numbers!)   ")

print("How much grams of flour do you have?")
flour_ammount = inputNumber("(enter just numbers!)   ")


#calculation
if eggs_ammount + milk_ammount + flour_ammount < 101:
 while 3 > 2:
  print("No blins today :(")

ppe = eggs_ammount
ppf = flour_ammount / 50
ppm = milk_ammount / 50
pcnt = ppe

if ppf < pcnt:
    pcnt = ppf

if ppm < pcnt:
    pcnt = ppm
print("You can make " + str(pcnt) + " blins.")
input("Press Enter to exit")