def factorial(a):
    i = 1
    mul = 1
    while i <= a:
        mul *= i
        i += 1
    return mul
string = str(factorial(100))
sum = 0
for i in string:
    sum += int(i)

print(string)
print(sum)