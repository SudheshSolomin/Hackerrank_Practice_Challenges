import sys

def main():

    number_of_clouds = int(input().strip())
    clouds = [int(numbers) for numbers in input().strip().split(' ')]
    jumps = -1
    i = 0
    while i < number_of_clouds:
        if i < number_of_clouds-2 and clouds[i+2] == 0: i += 1
        jumps += 1
        i += 1
    print(jumps)

if __name__ == "__main__":
    main()