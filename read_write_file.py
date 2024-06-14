# 1. poem.txt contains famous poem "Road not taken" by poet Robert Frost.
#    You have to read this file in your python program and find out words with maximum occurance.

from collections import Counter
import string

# Read and process the file
with open("files/poem.txt", "r") as file:
    text = (
        file.read()
        .lower()
        .translate(str.maketrans("", "", string.punctuation))
        .replace("\n", " ")
    )

# Split text into words and count occurrences
word_stats = Counter(text.split())

# Find the maximum occurrence
max_occurrence = max(word_stats.values())

# Print the results
print(f"Words with the maximum occurrence ({max_occurrence} times):")
for word, count in word_stats.items():
    if count == max_occurrence:
        print(word)

# 2. stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# Your input format (stocks.csv) is,

# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572
# Output.csv should look like this,

# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68

with open("files/stocks.csv", "r") as f, open("files/output.csv", "w") as out:
    out.write("Company Name, PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock}, {pe}, {pb}\n")
