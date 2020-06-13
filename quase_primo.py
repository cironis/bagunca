linha1 = input().split()
linha2 = input().split()


n = int(linha1[0])
s = linha2



x = len(s)

value_to_add = 0
value_to_subtract = 0


for i in range(1 << x):

    single_set = []
    multiply = 1

    for j in range(x):
        if i & (1 << j):
            single_set.append(int(s[j]))

    for num in single_set:
        multiply *= num
        if multiply > n:
            break

    if len(single_set) == 1:
        value_to_add += n//single_set[0]

    elif len(single_set) > 1:
        value_to_subtract += n//multiply

print(n - value_to_add + value_to_subtract)
