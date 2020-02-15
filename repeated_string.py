def main():
    input_string = input().strip()
    number_of_repeats = int(input().strip())
    number = input_string.count('a')

    if number==0:
        print (0)

    elif number==1 and len(input_string)==1:
        print (number_of_repeats)

    else:
        repeats=number_of_repeats//len(input_string) 
        remainders=number_of_repeats%len(input_string)

        print (int(number*repeats+input_string[:remainders].count('a')))

if __name__ == "__main__":
    main()