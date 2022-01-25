fabo  = lambda n: 0 if n==0 else (1 if n == 1 else (fabo(n-1) + fabo(n-2)))
print(fabo(6))
