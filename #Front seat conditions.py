#Front seat conditions 
#Bu kodumuz ile belli yaş altındaki bireylerin ön koltukta oturma koşunu inceliyoruz.
try:
    passenger_age = int(input("Enter your age please: "))
except ValueError:
    print("Invalid input! Please enter a number.")
if passenger_age < 12:
    print("You can't front passenger seat")
else:
    print("you can front passenger seat") 













