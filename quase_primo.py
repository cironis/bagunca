def powerset(s):
    
    x = len(s)
    subtract_multipliers = []
    add_multipliers = []
    
    for i in range(1 << x):
    
        single_set = []
        multiply = 1
    
        for j in range(x):
            if i & (1 << j):
                single_set.append(s[j])
    
        for num in single_set:
            multiply *= num
        
        if len(single_set) == 1:
            add_multipliers.append(single_set[0])
            
        elif len(single_set) > 1:
            subtract_multipliers.append(multiply)
                
    print subtract_multipliers
    print add_multipliers
    

powerset([4,5,6])
