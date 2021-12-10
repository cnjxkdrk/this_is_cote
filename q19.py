from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_result = 1000000000
max_result = -1000000000

op_list = []
for i in range(4):
    for _ in range(ops[i]):
        op_list.append(i)


result = data[0]
for aa in list(permutations(op_list, n-1)):

    for i in range(n-1):
        if aa[i] == 0:
            result = result+data[i+1]

        elif aa[i] == 1:
            result = result - data[i + 1]

        elif aa[i] == 2:
            result = result * data[i + 1]

        elif aa[i] == 3:
            if result <0:
                result *= -1
                result //= data[i+1]
                result *= -1
            else:
                result //= data[i+1]

    max_result = max(max_result, result)
    min_result = min(min_result, result)
    result = data[0]

print(max_result)
print(min_result)
