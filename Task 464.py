line = input("Enter line: ")
n = int(input("Enter number: "))
words = line.split()
print(f"The first character of the {n}-th word is: {words[n - 1][0]}")