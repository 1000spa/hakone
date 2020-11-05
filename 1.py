def Palindrome(string):
    if string == '':
        return False
    i = 0
    p = len(string)-1
    while i != len(string)-1:
        if string[i] == string[p]:
            i += 1
            p -= 1
        else:
            return False
        return True

a = input()
arr = []
for i in range(0,len(a)+1):
	for j in range(i,len(a)+1):
		if Palindrome(a[i:j]):
			arr.append(len(a[i:j]))
print(arr)