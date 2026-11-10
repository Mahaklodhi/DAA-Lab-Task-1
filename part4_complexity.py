
count = 0

print("Single loop:")

for i in range(1, 6):
    print(i)
    count += 1

print("Total single loop runs:", count)

count = 0

print("Nested loop:")

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        count += 1

print("Total nested loop prints:", count)

n = 10

print("For n =", n)
print("Single loop runs:", n)
print("Nested loop runs:", n * n)
