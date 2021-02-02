# print numbers
'''
for i in range(1,5) :
    for j in range(1,5) :
        for k in range(1,5) :
            if i != j and j != k and k != i :
            	print(i,j,k)
'''

# fall down
'''
h = 100
r = h / 2

for i in range(2,11) :
	print(i)
	h += 2 * r
	r /= 2

print('Total road is ',h)
print('The tenth is ',r)
'''

# print Fibonacci sequence
'''
a = 0
b = 1
print(a)
print(b)

for i in range(1,9) :
	c = a + b
	a = b
	b = c
	print(c)
'''

# eat peach
'''
num = 1
for i in range(10-1):
    num = (num+1)*2
print(num)
'''

# sort the numbers
'''
numlist = [5,11,3,6,9]
for i in range(0,5) :
	for j in range(i+1,5) :
		if numlist[i] > numlist[j] :
			numlist[i],numlist[j] = numlist[j],numlist[i]
print(numlist)
'''

# search the bingo number in sorted numlist
'''
numlist = [2,4,6,8,10,12,14,16,18,20]
num = 20
i = 0
while i < 10 :
	if num == numlist[i] :
		print("found the number ",num," at item ",i+1)
		exit()
	i += 1
print("not found")
'''
