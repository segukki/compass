first, second = input(), input()
if first.isdigit() and second.isdigit():
    output = int(first) + int(second)
else:
    output = str(first) + str(second)
print(output)
