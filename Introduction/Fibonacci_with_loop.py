prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for each in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo
