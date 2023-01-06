n = int(input())

inside = 0
outside = 0
for x in range(0, n):
    num = int(input())
    if (num >= 10) and (num <=20):
        inside +=1
    else:
        outside +=1
        
print()
print(f'{inside} in')
print(f'{outside} out')