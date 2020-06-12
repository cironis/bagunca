linha1 = input().split()
linha2 = input().split()


n = int(linha1[0])
s = linha2


def powerset(s):
    
    x = len(s)
    multipliers = {
        "subtract" : [],
        "add" : []
    }     
    
    
    for i in range(1 << x):
    
        single_set = []
        multiply = 1
    
        for j in range(x):
            if i & (1 << j):
                single_set.append(int(s[j]))
    
        for num in single_set:
            multiply *= num
        
        if len(single_set) == 1:
            multipliers["add"].append(single_set[0])
            
        elif len(single_set) > 1:
            multipliers["subtract"].append(multiply)
    
    return multipliers

multiplicadores = powerset(s)

value_to_add = 0
value_to_subtract = 0

for num in multiplicadores["add"]:
    if num <= n:
        value_to_add += n//num
        
for num in multiplicadores["subtract"]:
    if num <= n:
        value_to_subtract += n//num
    
return n - value_to_add + value_to_subtract
