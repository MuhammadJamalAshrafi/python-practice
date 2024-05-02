# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
football_field_length = 92  # in meters
football_field_width = 48.8  # in meters
football_field_area = football_field_length * football_field_width
print(f"Total area of football field is: {football_field_area} square meters")

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar. Calculate the change using Python.
num_packets = 9
cost_per_packet = 1.49
total_cost = num_packets * cost_per_packet
money_paid = 20
change = money_paid - total_cost
print(f"The shopkeeper will give you back ${change:.2f}")

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
length=5.5
cost_per_square_feet=500
area=length**2
total_cost=area*cost_per_square_feet

print(f"The total cost to replace all tiles is {total_cost:.1f}")

# 4. Print binary representation of number 17
number=17
print(f"Binary of number 17 is: {format(number, 'b')}")