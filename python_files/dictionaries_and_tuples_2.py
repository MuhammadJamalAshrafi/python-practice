import statistics

stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}

def print_stocks():
    for stock, price_list in stocks.items():
        print(f"{stock} ==> {price_list} ==> avg: {round(statistics.mean(price_list), 2)}")

def add_stock():
    s = input("Enter a stock ticker to add:")
    p = input("Enter price of this stock:")
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    
    print_stocks()
    
def main():
    operation = input('Enter operation (print, add or amend):')
    if operation.lower() == 'add':
        add_stock()
    elif operation.lower() == 'print':
        print_stocks()
    else:
        print(f"Unsupported operation {operation.lower()}")

if __name__ == "__main__":
    main()