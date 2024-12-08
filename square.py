list=[1,5,8,6]

square=[]
odd=[]
even=[]
for i in list:
    x=i*i
    square.append(x)
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("Square of list is", square)
print("Square of list odd values  is", odd)
print("Square of list even values is", even)