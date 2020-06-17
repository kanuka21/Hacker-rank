
import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    lastAnswer = 0
    answerList = []
    seqLists = [[] for i in range(n)]

    for i in range(len(queries)):
        query_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]

        if query_type == 1:
            seq = (x^lastAnswer) % n
            seqLists[seq].append(y)
        else:
            seq = (x^lastAnswer) % n
            size = len(seqLists[seq])
            index = y % size
            lastAnswer = seqLists[seq][index]
            answerList.append(lastAnswer)

    return answerList
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
