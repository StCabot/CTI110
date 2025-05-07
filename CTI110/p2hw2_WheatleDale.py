#Dale Wheatle
#feb 24,2025
#P2hw2
#making a list with grades

#creating varibales 
mod_1=float(input("enter grade for module 1: "))
mod_2=float(input("enter grade for module 2: "))
mod_3=float(input("enter grade for module 3: "))
mod_4=float(input("enter grade for module 4: "))
mod_5=float(input("enter grade for module 5: "))
mod_6=float(input("enter grade for module 6: "))

#creating an empty list 
grade_list=[]

#using the append method to add all the grades 
#code looks like:list_name.append()

grade_list.append(mod_1)
grade_list.append(mod_2)
grade_list.append(mod_3)
grade_list.append(mod_4)
grade_list.append(mod_5)
grade_list.append(mod_6)
print()

#display the list 
print(grade_list)
print()

print("------results-------")
print()

#display values for the user/ also using a f string to format the information given by the user
print(f"{'lowest grade:':<20}{min(grade_list)}") #lowest 
print(f"{'Highest grade:':<20}{max(grade_list)}") #highest 
print(f"{'sum of grades:':<20}{sum(grade_list)}") # adding them all together

#creating a new veraible for average   len()=number of variables 
average=sum(grade_list)/len(grade_list) 

print(f"Average:{average}")  # using f string you are requierd to wrap the variable in curlly bracets
print("--------------------------")