import math
from collections import Counter

def main():

    number_of_pairs = 0

    # Get Input
    number_of_socks = int(input())
    array = [int(numbers) for numbers in input().split()[:number_of_socks]]

    # Get number of duplicates in an array
    pair_counts = Counter(array) 

    for key, value in pair_counts.items():
        pairs = math.floor(value/2)
        number_of_pairs = pairs + number_of_pairs
    
    print (number_of_pairs)

if __name__ == "__main__":
    main()