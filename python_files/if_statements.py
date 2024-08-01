## Exercise: Python If Condition
# Using following list of cities per country,
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#   1. Write a program that asks user to enter a city name, and
#   it should tell which country the city belongs to
city = input("Enter a city name? ")
if city in india:
    print(f"{city} in india")
elif city in pakistan:
    print(f"{city} in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")

#   2. Write a program that asks user to enter two cities, and it tells you if they both are in same country or not.
#   For example if I enter mumbai and chennai, it will print "Both cities are in India"
#   but if I enter mumbai and dhaka it should print "They don't belong to same country"
city_one = input("Enter city 1: ")
city_two = input("Enter city 2: ")
if city_one in india and city_two in india:
    print("Both cities are in india")
elif city_one in pakistan and city_two in pakistan:
    print("Both cities are in pakistan")
elif city_one in bangladesh and city_two in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")

