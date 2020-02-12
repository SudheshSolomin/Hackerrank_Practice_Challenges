def main (): 
    
    number_of_sequences, queries = map(int, input().split())
    last_answer = 0
    seqList = [[] for _ in range(number_of_sequences)]

    for __ in range(queries):
        q, x, y = map(int, input().split())
        index = (x ^ last_answer) % number_of_sequences
        seq = seqList[index]
        if q == 1:
            seq.append(y)
        elif q == 2:
            size = len(seq)
            last_answer = seq[y % size]
            print(last_answer)
        else:
            raise ValueError()
        
if __name__ == '__main__':

    main()
    