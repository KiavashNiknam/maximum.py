
a = [10, 25, 7, 48, 16]

maximum = a[0]

for v in a[1:]:
    if v > maximum:
        maximum = v

print("Maximum =", maximum)
