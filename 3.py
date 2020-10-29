#1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?
input_n = 1000
Sum = 0

for i in range(1, input_n +1):
	if i < 1000:
		if i % 3 == 0:
			Sum += i
		elif i % 5 == 0:
			Sum += i
print(Sum)