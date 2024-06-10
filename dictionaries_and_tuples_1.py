population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country = input("Enter country name to add: ")
    country = country.lower()
    if country in population:
        print('Country already exists in our dataset. Terminating')
        return
    p = input('Enter population of {country}')
    p = float(p)
    population[country] = p
    print_all()

def remove():
    country = input("Enter country name to add: ")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()
    
def query():
    country = input("Enter country name to query: ")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")
    
    
def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")        

def main():
    option = input('Enter operations (add, remove, query or print):')
    if (option.lower() == 'add'):
        add()
    elif (option.lower() == 'remove'):
        remove()
    elif (option.lower() == 'query'):
        query()
    elif (option.lower() == 'print'):
        print_all()

if __name__ == '__main__':
    main()