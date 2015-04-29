#!/usr/bin/env python

num_list = [10,20,30,9]

to_s_num_list = ''.join(map(str,num_list))
print to_s_num_list

increase = int(to_s_num_list) + 1

num_list_inc = map(int, str(increase))
print num_list_inc
