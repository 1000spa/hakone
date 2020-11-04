string = input()
count1 = 0
countI = 0
countl = 0
countisanghae = 0
for i in string:
	if i == '1':
		count1 += 1
	if i == 'I':
		countI += 1
	if i == 'l':
		countl += 1
	if i == '|':
		countisanghae += 1
print(f"""
{count1}
{countI}
{countl}
{countisanghae}
""")