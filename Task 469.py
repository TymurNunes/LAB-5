numbers = input("Enter numbers: ").split()
new_numbers = numbers[::-1]
print(int("".join(new_numbers)))