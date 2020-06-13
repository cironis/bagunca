linha1 = input().split()
linha2 = input().split()


n = int(linha1[0])
k = linha1[1]
primos = linha2

count = 0

for num in range(2,n+1):
    num = int(num)
    loop_count = k
    for primo in primos:
        primo = int(primo)
        if num % primo == 0:
            break
        loop_count -= 1
    if loop_count != 0:
        count += 1

print(n - count)
