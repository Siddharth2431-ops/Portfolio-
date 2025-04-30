#Making A.I using python.
name= input("Enter your name: ")
print("Hello",name)
print("Which service do you want?")
print("1. Info, 2. Goods, 3. Help")
flt= int(input("Enter the service no= "))
if flt==1:
      print(name,"This is Info area. I am A.I chatbot which is specially designed to help you.")
elif flt==2:
      print("This is Goods area, see the store location:")
      print("Cold drink:Left")
      print("Fashion:Straight")
      print("Electronics:Right")
      print("Refugees:Back")
elif flt==3:
      print("This help area, enter the service you want:-")
      print("a. Refugee, b. Temple, c. Railways")
srvc= input("Enter the service which you want within option : ")
if srvc=='a':
       print("Move back and turn left, you will find refugee")
elif srvc=='b':
       print("Move towards stairs and move as the way directed --->")
elif srvc=='c':
       print("Turn back and move left towards parking, you will find railway station")
       print("Good bye",name)
else:
      print("Have a good journey",name)