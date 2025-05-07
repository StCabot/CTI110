#dale wheatle
#feb 26,2025
#p2hw1
#formatting 

budget=float(input("Enter Budget:"))
Travel_destination=input("enter your travel destination:")
gas=float(input("how much do you think you will spend on gas?:"))
hotel=float(input("how much do you need for lodging?:"))
food=float(input("how do you need for food?:"))
remaining_balance=budget-(gas+hotel+food)
print()
print("--------Travel exspenses-------")

print(f"{'location:':<20}{Travel_destination}")
print(f"{'inital Budget:':<20}{budget:.2f}")
print(f"{'gas:':<20}{gas:.2f}")
print(f"{'lodging:':<20}{hotel:.2f}")
print(f"{'Food:':<20}{food:.2f}")
print("------------------------")
print()
print(f"{'Remaining Balance:':<20}{remaining_balance:.2f}")