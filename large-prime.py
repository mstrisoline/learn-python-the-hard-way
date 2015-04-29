#!/usr/bin/env python
primes = []
for n in range(1,600851475143):
  print n
  for i in 2,5:
    if n % i == 0:
      print i
      break
  else:
    for i in range(3,n):
      if n % i == 0:
        break
    else:
      primes.append(n)

print primes
