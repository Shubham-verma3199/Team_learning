def product(array):
    new_array = []
    for i in  range (len(array)):
        product = 1
        for j in range(len(array)):
            if i == j:
                continue
            product *= array[j]
         
        new_array.append(product)
    return new_array

print(product([1,2,3]))    
   
