#1.
# Define the length and width of the football field
football_field_length = 92  # in meters
football_field_width = 48.8  # in meters

# Calculate the area of the football field
# The area of a rectangle is calculated by multiplying its length by its width
football_field_area = football_field_length * football_field_width

# Print out the total area of the football field
# The f string formatting is used to insert the value of the football_field_area variable into the string
# print(f"Total area of football field is: {football_field_area} square meters")

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar. Calculate the change using Python.

num_packets = 9
cost_per_packet = 1.49
total_cost = num_packets * cost_per_packet
money_paid = 20
change = money_paid - total_cost

print(f"The shopkeeper will give you back ${change:.2f}.")