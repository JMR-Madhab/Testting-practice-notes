'''
num = 5
count = 0

if num>1:
    for i in range(1, num+1):
        if (num%i) == 0:
            count = count+1
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not prime")
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(29))  # True