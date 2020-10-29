ListA = []
arr = []
for i in range(100, 999):
    for j in range(100,999):
        re = str(i*j)
        ListA.append(re)

for a in range(len(ListA)):
    RevListA = ListA[a][::-1]
    if RevListA == ListA[a]:
        a = int(RevListA)
        arr.append(a)
print(max(arr))
