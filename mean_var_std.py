import numpy as num

def calculate(data_list):
    
    # ubah input menjadi metrix
    data_matrix = num.array(data_list).reshape(3,3)

    data_mean = num.mean(data_matrix,axis=0).tolist(),num.mean(data_matrix,axis=1).tolist(),num.mean(data_matrix)
    data_var = num.var(data_matrix,axis=0).tolist(),num.var(data_matrix,axis=1).tolist(),num.var(data_matrix)
    data_std = num.std(data_matrix,axis=0).tolist(),num.std(data_matrix,axis=1).tolist(),num.std(data_matrix)
    data_max = num.max(data_matrix,axis=0).tolist(),num.max(data_matrix,axis=1).tolist(),num.max(data_matrix)
    data_min = num.min(data_matrix,axis=0).tolist(),num.min(data_matrix,axis=1).tolist(),num.min(data_matrix)
    data_sum = num.sum(data_matrix,axis=0).tolist(),num.sum(data_matrix,axis=1).tolist(),num.sum(data_matrix)

    print("mean:",data_mean)
    print("var :",data_var)
    print("std :",data_std)
    print("max :",data_max)
    print("min :",data_min)
    print("sum :",data_sum)
    

input_str = input("Enter numbers separated by space: ")

if len(input_str) < 9 :
    raise ValueError("Input must be a containing 9 digits.")
else:
   numbers = list(map(int, input_str.split()))
   calculate(numbers)

#calculate([0,1,2,3,4,5,6,7,8])