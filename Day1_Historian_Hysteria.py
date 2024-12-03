'''
Advent of code day 1.

- Two unsorted lists as an input
- Lists need to be sorted
- Calculate difference between the values at each index of the sorted lists
- Sum the differences 
'''
from collections import Counter

def calculate_total_distance(first_locations, second_locations):
    """Function to calculate the total distance between
    two lists of locations."""
    first_locations = sorted(first_locations)
    second_locations = sorted(second_locations)
    total_distance = 0
    for i in range(len(first_locations)):
        total_distance += abs(first_locations[i] - second_locations[i])
    
    return total_distance


def calculate_similarity_score(first_locations, second_locations):
    """Calculates the sum of each number in first_locations 
    multiplied by the number of times it occurs in second_locations"""
    similarity_score = 0
    occurences = Counter(second_locations)
    for item in first_locations:
        similarity_score += (item * occurences[item])
    return similarity_score



def read_input(filename):
    """Reads an input file and puts the values into 2 lists"""
    with open(filename) as file:
        data = file.read().splitlines()

    more_data = []
    for item in data:
        more_data.append(item.split('   '))
    
    return more_data


def main():
    """Main function of the program."""
    first_locations = []
    second_locations = []
    more_data = read_input('Day1_input.txt')
    for thing in more_data:
        first_locations.append(int(thing[0]))
        second_locations.append(int(thing[1]))
    #distance = calculate_total_distance(first_locations, second_locations)
    #print("Total distance is: {0}\n".format(distance))
    similarity_score = calculate_similarity_score(first_locations, second_locations)
    print("Similarity Score is: {0}\n".format(similarity_score))

if __name__ == "__main__":
    main()


