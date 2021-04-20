n,k = map(int,input().split())

if n>= k(k+1)/2:
  if k % 2 == 0:
    if n%k == k//2: print(k-1)
    else: print(k)
  else:
    if n%k == 0: print(k-1)
    else: print(k)
else:
  print(-1)
