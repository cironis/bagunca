linha1 = input().split()
linha2 = input().split()


n = int(linha1[0])
lista = linha2

all_multiples_set = set()

for i in range(len(lista)):
    interador = int(linha2[i])
    one_multiple_set = set(range(interador,n if n % interador != 0 else n + interador,interador))
    all_multiples_set = all_multiples_set.union(one_multiple_set)
    
print n - len(all_multiples_set)
