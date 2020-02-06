def main():
    sea_level = 0
    number_of_valleys = 0
    total_number_valleys = 0
    number_of_mountains = 0
    total_number_mountains = 0

    array = []

    # Get the input
    number_of_steps = int(input())
    steps = input()[:number_of_steps]

    #Calculate the total number of valleys
    for step in steps:
        
        if step == 'U':
            sea_level = sea_level + 1
        
        else:
            sea_level = sea_level - 1

        array.append(sea_level)
        
    for index in range(len(array)):
        if index < len(array) - 1:
            if array[index] == 0 and array[index + 1] == -1:
                number_of_valleys = number_of_valleys + 1

    if array[0] == -1:
        print (number_of_valleys + 1)
    else:
        print (number_of_valleys)

if __name__ == "__main__":
    main()