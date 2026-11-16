
# Import required libraries
import itertools
import math

# Store the coordinates of each city
cities = {
    0: (0, 0),
    1: (2, 4),
    2: (5, 2),
    3: (6, 6),
    4: (1, 5)
}

# Function to calculate the distance between two cities
def distance(c1, c2):

    # Get the coordinates of both cities
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]

    # Apply the Euclidean distance formula
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Function to calculate the total distance of a route
def path_length(path):

    total = 0

    # Calculate the distance between consecutive cities
    for i in range(len(path)):
        total += distance(path[i], path[(i + 1) % len(path)])

    # Return the total route distance
    return total


# Function to solve the Travelling Salesman Problem
def solve_tsp():

    # Get all city IDs
    city_ids = list(cities.keys())

    # Fix the first city as the starting city
    start = city_ids[0]

    # Store the remaining cities
    rest = city_ids[1:]

    # Initialize the shortest route and distance
    best_path = None
    best_length = float('inf')

    # Generate all possible arrangements of remaining cities
    for perm in itertools.permutations(rest):

        # Create a complete route starting from City 0
        path = [start] + list(perm)

        # Calculate the total distance of the current route
        length = path_length(path)

        # Check whether the current route is shorter
        if length < best_length:

            # Update the shortest route and distance
            best_length = length
            best_path = path

    # Return the shortest route and its distance
    return best_path, best_length


# Call the function to find the optimal route
best_path, best_length = solve_tsp()

# Display the shortest route and total distance
print("Best route:", best_path + [best_path[0]])
print("Total distance:", round(best_length, 2))
