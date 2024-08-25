num = 1234
reversed_number = 0    
while num > 0:
   
    remainder = num % 10 
    reversed_number = (reversed_number * 10)+ remainder 
    num = num // 10
    
print(reversed_number)