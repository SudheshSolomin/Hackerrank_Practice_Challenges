def hourglass_sum(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            yield (matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] +
                   matrix[i + 1][j + 1] +
                   matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2])

def max_hourglass_sum(matrix):
    return max(hourglass_sum(matrix))

def main():
    matrix = []

    for _ in range(6):
        matrix.append(list(map(int, input().rstrip().split())))

    hourglass_sum(matrix)

    result = max_hourglass_sum(matrix)

    print (result)

if __name__ == "__main__":
    main()