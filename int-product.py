#!/usr/bin/env python
mod_3_sum = 0
mod_5_sum = 0
i = 1
for i in range(1000):
  if i % 3 == 0:
    mod_3_sum += i
  if i % 5 == 0:
    mod_5_sum += i

total = mod_3_sum + mod_5_sum

print total
