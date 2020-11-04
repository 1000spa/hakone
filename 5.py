string = input()
count = 0
array = []
array = string.split(' ')
for i in array:
	if array[i] != '':
		count += 1
print(count)