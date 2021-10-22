def second_large(array):
    sorted_array = sorted(set(array))
    print (sorted_array[-2])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_large(arr)