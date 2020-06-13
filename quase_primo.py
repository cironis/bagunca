first_line = input().split()
second_line = input().split()


n = int(first_line[0])
list_of_primes = second_line

all_multiples_set = set()

for i in range(len(list_of_primes)):
    prime = int(list_of_primes[i])
    one_multiple_set = set(range(prime ,n if n % prime  != 0 else n + prime ,prime ))
    all_multiples_set = all_multiples_set.union(one_multiple_set)

print(n - len(all_multiples_set))
