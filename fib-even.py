#!/usr/bin/env python
total = 0
fib1= 0
fib2 = 1

while fib2 < 4000000:
  if fib2 % 2 == 0:
    total += fib2
  fib1, fib2 = fib2, fib1 + fib2
print total
