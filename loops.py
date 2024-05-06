# 1. After flipping a coin 10 times you got this result,
#    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#    Using for loop figure out how many times you got heads
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print(f"Heads count : {count}")

# 2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Square of {i} is : {i ** 2}")
    
# 3. Your monthly expense list (from Jan to May) looks like this,
#    expense_list = [2340, 2500, 2100, 3100, 2980]
#    Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
#    If expense is not found then it should print that as well.
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]
e = int(input("Enter expense amount: "))
for i in range(len(expense_list)):
    if expense_list[i] == e:
        print(f"Expense {e} occurred in {month_list[i]}")
        break
else:
    print(f"Expense {e} not found")
    
# 5. Lets say you are running a 5 km race. Write a program that,
#    Upon completing each 1 km asks you "are you tired?"
#    If you reply "yes" then it should break and print "you didn't finish the race"
#    If you reply "no" then it should continue and ask "are you tired" on every km
#    If you finish all 5 km then it should print congratulations message
for km in range(1, 6):
        print(f"You have completed {km} km.")
        response = input("Are you tired? (yes/no): ").lower()
        if response == "yes":
            print("You didn't finish the race.")
            break
        elif response == "no":
            continue
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")
else:
    print("Congratulations! You finished the race!")
    
# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
for i in range(5):
    s = ''
    for j in range(i):
        s += "*"        
    print(s)