nums = eval(input())
s = 0
for n in nums:
    if n % 2 == 0:
        s += n
print(s)
