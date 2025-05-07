#Dale Wheatle
#feb 27,2025
#p2lab2
#creating a dictionary

#creating the dictionary
cars={"Camaro":18.21,
     "Prius":52.36,
      "Model s":110,
      "Silverado":26
      }
#get keys from dictionary 
cars_keys=cars.keys()
print(cars_keys)
print(*cars_keys,sep=",") #print(*list_name,sep=",") this prints the list much nicer
print()
#promt the user to input a car 
car_name=input("enter the car you have: ")
print()
#get mpg for the given car
car_mpg=cars[car_name]
print(f"The {car_name} get {car_mpg} miles per gallon.")
print()
#get miles from user
miles_driven=float(input(f"How many miles will you drive the {car_name}?"))
print()
#calcuate 
gallons_needed=miles_driven/car_mpg

#displaying the total amount of gallons needed

print(f"{gallons_needed:.2f} of gallons are needed to drive the {car_name} {miles_driven} miles.")