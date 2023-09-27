# filename: virtual_city.py

def create_city(rows, cols):
    city = [['-' for _ in range(cols)] for __ in range(rows)]
    return city

def add_building(city, row, col):
    if row < len(city) and col < len(city[0]):
        city[row][col] = 'X'
    else:
        print("Invalid position. The building could not be placed.")
    return city

def print_city(city):
    for row in city:
        print(' '.join(row))

# create a 5x5 city
city = create_city(10, 10)

# specify the location of the building
building_row = 5
building_column = 2

# add the building to the city
city = add_building(city, building_row, building_column)

# print the final city plan
print_city(city)