 #Dale Wheatle
#March 10,2025
#p3hw2
#creating a program that will determin the amount of pay the user will get



'''
-get the users name.....employee ....input() function
-get employee's hours worked......float(input()) function
-get employee's pay rate..........float(input()) function 

-calculate some values:
if hours_worked >40:
    calculate ot_hours(hours_worked-40)
    calculate Ot_pay_rate(pay_rate*1.5)
    calculate ot_pay(ot_hours*ot_pay_rate)
    calculate reg_pay (reg_hours*pay_rate)
    calculate gross_pay(ot_pay+reg_pay)



    reg_hours is equal to 40(creating a veraibale)

    #if they dont make overtime 
else:
    ot_hours is zero (create a variable)
    Ot_pay_rate is zero(create a variable)
    ot_pay(create a variable)
    reg_hours is equal to hours_worked(create a variable)
    reg_pay (reg_hours*pay_rate)
    gross_pay(ot_pay+reg_pay)

Display all values with width formating 

Ex:
print(f"{'hours_worked':<20}{'pay_rate':<20}")

'''
#getting the input of the user
user_name=input("Enter employee's Name: ")
hours_worked=float(input("Enter number of hours worked: "))
pay_rate=float(input("Enter employee's pay rate: "))

#calculations initalizing 
reg_pay=(pay_rate*40)
ot_hours=(hours_worked-40)
ot_pay_rate=(pay_rate*1.5)
ot_pay=(ot_hours*ot_pay_rate)

#doing if/else statments to get some calculations correct 
if hours_worked>40:
    ot_hours=hours_worked-40

else:
    ot_hours=0

#gross pay 
gross_pay=(ot_pay+reg_pay)




#displaying the users inputs  
print(f"Enter Employee's name: {user_name} ")
print(f"Enter number of hours worked: {hours_worked}")
print(f"Enter employee's pay rate: {pay_rate}")
print("----------------------------------------------------------------")
print(f"{'Employee name:':<20}{user_name} ")
print()
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-------------------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<20.2f}{pay_rate:<20.2f}{ot_hours:<20.2f}{ot_pay:<20.2f}{reg_pay:<20.2f}{gross_pay:<20.2f}")




