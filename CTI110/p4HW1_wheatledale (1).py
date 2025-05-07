#Dale Wheatle
#march 24,2025
#p4HW1
#creating loops for the test scores 


grade_book=[]
num_scores=int(input("How many scores do you want to enter?"))
for score in range(num_scores):
    grade=float(input(f"Enter score # {score+1}:"))
    while grade<0 or grade>100:
        print("invalid grade")
        grade=float(input(f"Enter score # {score+1} again:"))
    grade_book.append(grade)

'''
#testing the list 
print(grade_book)
'''
#getting the lowest scores
smallest=min(grade_book)

#print(f"smallest number in the list is:{smallest}")

#modified list 
mod_list=grade_book.remove(smallest)

#testing the new modified grade list
#print(grade_book)

#getting the average for scores 
average=sum(grade_book)/len(grade_book)

#getting the letter grades for the scores 
if average >=90:
    grade="A"
elif average >=80:
    grade="B"
elif average >=70:
    grade="C"
elif average >=60:
    grade="D"
else:
    grade="F"





print()
print()
print("-------------------------Results--------------------")
print(f"{'lowest Score ':<15}: {smallest:.2f}")
print(f"{'modified List ':<15}: {grade_book}")
print(f"{'Scores Average :':>10} {average:.2f}")
print(f"{'Grade':<15}: {grade}")
print("-----------------------------------------------------")

