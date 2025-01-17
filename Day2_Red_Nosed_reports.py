"""
Part 1:
 - Read rows from input file
 - Count number of rows that have values in descending order

 Using rows rather than 'reports'

"""

def safe_rows(rows):
    """Returns the number of safe rows"""
    num_safe = 0
    for row in rows:
        row_len = len(row)
        if is_safe(row, row_len):
            num_safe += 1
        else:
            #Loop row_len times 
            #remove element at index i from the row
            #Check if the row is now safe  
            for i in range(row_len):
                row_copy = row[:]
                del row_copy[i]
                if is_safe(row_copy, row_len - 1):
                    num_safe += 1
                    #If the row is safe by removing this value, then we don't want to keep checking for this row
                    break
    return num_safe


def is_safe(row, row_len):
    """Returns true if a row is safe"""
    increase_count = 1
    decrease_count = 1
    for i, num in enumerate(row):
        if i == 0:
            continue
        difference = abs(num - row[i - 1])
        #If current num is greater than previous num by no more than 3
        if difference > 0 and difference <= 3 and num > row[i - 1]:
            increase_count += 1

        #If current num is less than previous num by no more than 3  
        if difference > 0 and difference <= 3 and num < row[i - 1]:
            decrease_count += 1

    #If all elements are increasing, or all are decreasing then return True
    if increase_count == row_len or decrease_count == row_len:
        return True
     

def read_input(filename):
    """Reads an input file in appropriate lists"""
    with open(filename) as file:
        rows = file.read().splitlines()
  
    #creates a 2d-array of rows and each element in each row is converted to integer type 
    rows = [[int(item) for item in row.split()] for row in rows]

    return rows


def main():
    """Main function of the program."""
    rows = read_input("Day2_input.txt")
    print('\n')
    print(safe_rows(rows))


if __name__ == "__main__":
    main()