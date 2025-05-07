#Dale Wheatle
#3/3/2025
#p3lab
#using if/else statments to determing coin combonations 

#get a float form the user 

input_money=float(input("Enter the amount of money as a float: $"))

money=int(input_money*100) #converting a decmial into a whole number 


#calculate number of whole dollars 
num_dollars=money//100 
#print(f"number of dollars are {num_dollars}") #using this to test 

#remove the dollar from the amount of money assigning a new value

money=money-(num_dollars*100) #removing the dollars to juist cents 

#print(f"the remaining money is {money}")

#______------______------________-----breaking it up 



#calculate number of quateres 
num_quarters=money//25
#print(f"number of quaters are {num_quarters}") #using this to test 

#remove the dollar from the amount of money assigning a new value

money=money-(num_quarters*25) #removing the dollars to juist cents 

#print(f"the remaining money is {money}")

#______------______------________-----breaking it up 



#calculate number of dimes 
num_dimes=money//10
#print(f"number of dimes are {num_dimes}") #using this to test 

#remove the dollar from the amount of money assigning a new value

money=money-(num_dimes*10) #removing the dollars to juist cents 

#print(f"the remaining money is {money}")

#______------______------________-----breaking it up 



#calculate number of nickles
num_nickles=money//5
#print(f"number of nickles are {num_nickles}") #using this to test 

#remove the dollar from the amount of money assigning a new value

money=money-(num_nickles*5) #removing the dollars to juist cents 

#print(f"the remaining money is {money}")

#______------______------________-----breaking it up 



#calculate number of penies
num_pennies=money
#print(f"number of pennies are {num_pennies}") #using this to test

#______------______------________-----breaking it up 

#display the coins and dollars needed if only used
#ensure all grammer is correct (ex: peenies/penny)
print()
print()
print()
#if no change is due, make it dispay "no change"
if input_money==0.00:
    print("$0.00 no change")

if num_dollars>0:
    if num_dollars==1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

#displaying quaters 
if num_quarters>0:
    if num_quarters==1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

#displaying Dimes
if num_dimes>0:
    if num_dimes==1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

#displaying Nickles

if num_nickles>0:
    if num_nickles==1:
        print(f"{num_nickles} Nickel")
    else:
        print(f"{num_nickles} Nickels")

#displaying peenies 

if num_pennies>0:
    if num_pennies==1:
        print(f"{num_pennies} Peeny")
    else:
        print(f"{num_pennies} Peenies")

