from random import seed, randrange, sample
import sys
from os import path


try: 
    for_seed, upper_bound, size =\
         (int(x) for x in input('Enter three nonnegative integers: ').split())
    if for_seed < 0 or upper_bound < 0 or size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
w = len(str(upper_bound - 1))
with open('mapping.txt', 'w') as mapping:
    for (a, b) in zip(sorted(randrange(upper_bound) for _ in range(size)),
                      (randrange(upper_bound) for _ in range(size))
                     ):
        print(f'{a:{w}}', '->', b, file=mapping)                
print('Here is the mapping that has been generated:')
with open('mapping.txt') as mapping:
    for line in mapping:
        print(line, end='')

valid_mapping = True
most_frequent_inputs = []
function = {}

# INSERT YOUR CODE HERE
import os
import random
import collections
l1=[]
l2=[]
list1=[]
with open('mapping.txt') as popq2:
    for line in popq2:
        list1=line.split(" -> ");
        l1.append(int(list1[0]))
        l2.append(int(list1[1]))
#         print(list1)
# print(l1)
# print(l2)
for i in range(len(l1)):
    for j in range(len(l1)):
        if (l1[i]==l1[j] and i!=j):
            if(l2[i]==l2[j]):
                valid_mapping=False
if not valid_mapping:
    print("Sorry, that's not a correct mapping.")
    exit(0)
else:
    print("Ok, that's a correct mapping.")
    d = collections.defaultdict(int)
    for i in l1:
        d[i] += 1
    maxfreq=max(d.values())
    k1=[]
    for k,v in d.items():
        if v==maxfreq:
            most_frequent_inputs.append(k)

    for k,v in d.items():
        if v==1:
            k1.append(k)
    print('The list of most frequent inputs is:\n\t', most_frequent_inputs)

    for i in k1:
        function[i]=l2[l1.index(i)]
    print('The function extracted from the mapping is:\n\t', function)
    
